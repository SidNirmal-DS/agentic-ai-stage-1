# agentic-ai-stage-1

Movie Recommender Agent (Stage 1)

Overview

This is a LangChain-powered agentic AI application that recommends movies based on the user’s mood. The project uses OpenAI’s GPT-3.5 Turbo as the LLM and DuckDuckGo search integration for fetching contextual results in real time.

⸻

Objective

To create an intelligent agent that understands natural language mood input (e.g., “romantic”, “sci-fi action”) and recommends 3 movies with short descriptions.

⸻

Key Features
	•	Accepts natural language mood as user input
	•	Uses a LangChain agent (React-style) to think, search, and respond
	•	Integrates DuckDuckGoSearchRun tool to enhance contextual search
	•	Uses OpenAI’s GPT-3.5 Turbo model via langchain_openai
	•	Agent output includes three movie titles with descriptions

⸻

Technology Stack
	•	Python (v3.12 recommended)
	•	LangChain (langchain, langchain_community, langchain_openai)
	•	DuckDuckGo Search Tool
	•	OpenAI GPT (3.5-turbo)
	•	dotenv for API key management

⸻

Folder Structure

movie-recommender-agent/
├── agent_recommender.py   # Core logic and agent setup
├── main.py                # CLI entry point for testing
├── config.py              # API key loading from .env
├── .env                   # Environment variables
├── requirements.txt       # Dependencies
└── README.md              # Project overview and documentation


⸻

.env File Format

OPENAI_API_KEY="your_openai_key_here"


⸻

Installation Steps

# Step 1: Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Step 2: Install dependencies
pip install -r requirements.txt

requirements.txt

langchain==0.1.20
langchain-community==0.0.38
langchain-openai==0.1.6
openai
duckduckgo-search
python-dotenv


⸻

How It Works
	1.	User inputs mood (e.g., “sci-fi action”)
	2.	LangChain agent decides to use the DuckDuckGo tool to find movie context
	3.	Based on context + user mood, the agent returns 3 relevant movie suggestions

⸻

Sample Run (CLI)

python main.py
Enter your current mood or genre preference: romantic

Returns:
	•	Movie 1: Title + description
	•	Movie 2: Title + description
	•	Movie 3: Title + description

⸻

Notes
	•	Make sure your .env file is correctly configured
	•	DuckDuckGo Search may occasionally hit rate limits (a 2-second delay has been added)
	•	LangChain hub is used to fetch prompt template (react-chat)

⸻

Next Steps

We will continue with Stage 2:
	•	Add multi-agent setup (Professor Agent + Search Agent)
	•	Use of TMDB API for movie posters
	•	Structured UI output for streaming recommendations

⸻


⸻
