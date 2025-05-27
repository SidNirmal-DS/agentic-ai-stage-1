import time
from langchain_community.tools import DuckDuckGoSearchRun
from duckduckgo_search.exceptions import DuckDuckGoSearchException

class SmartSearchTool:
    def __init__(self, retries=3, delay=3, backend="lite"):
        self.retries = retries
        self.delay = delay
        self.backend = backend
        self.search_tool = DuckDuckGoSearchRun(backend=self.backend)

    def run(self, query):
        for attempt in range(self.retries):
            try:
                return self.search_tool.run(query)
            except DuckDuckGoSearchException:
                print(f"[Retry {attempt+1}] Rate limit or error. Retrying in {self.delay} sec...")
                time.sleep(self.delay)
        return "Sorry, search is currently unavailable. Please try again later."