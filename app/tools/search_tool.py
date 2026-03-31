from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient()

@tool
def web_search(query: str) -> str:
    """Search the web for recent and factual information."""
    """
        Use this tool for:
        - latest news
        - recent model updates
        - benchmark releases
        - current events
        - internet facts after training cutoff
        """
    result = client.search(query=query, max_results=3)
    return str(result)