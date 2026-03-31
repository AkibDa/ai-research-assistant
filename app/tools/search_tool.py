from langchain.tools import tool
import requests

@tool
def web_search(query: str) -> str:
    """Search the web for recent information."""
    # Replace later with SerpAPI / Tavily
    return f"Recent web results for: {query}"