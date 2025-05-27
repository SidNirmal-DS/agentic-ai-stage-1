from dotenv import load_dotenv
load_dotenv()

import time
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain import hub
from config import OPENAI_API_KEY

# ✅ Check API key
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set. Please check your .env file or environment variables.")

# ✅ Initialize LLM with API Key    
llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo",
    openai_api_key=OPENAI_API_KEY
)

# ✅ Add delay to avoid DuckDuckGo rate limits
class SafeSearchTool:
    def __init__(self, search_tool):
        self.search_tool = search_tool

    def run(self, query):
        time.sleep(2)  # delay to avoid rate-limit
        return self.search_tool.run(query)

safe_search_tool = SafeSearchTool(DuckDuckGoSearchRun())

tools = [
    Tool(
        name="MovieSearchTool",
        func=safe_search_tool.run,
        description="Search for movie titles and metadata based on user mood"
    )
]

# ✅ Load prompt and build agent
agent_prompt = hub.pull("hwchase17/react-chat")
agent = create_react_agent(llm=llm, tools=tools, prompt=agent_prompt)

# ✅ Wrap in executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# ✅ Define callable function
def get_movie_recommendations(user_mood):
    return agent_executor.invoke({
        "input": f"Recommend 3 movies for someone feeling '{user_mood}', with short descriptions.",
        "chat_history": []
    })

