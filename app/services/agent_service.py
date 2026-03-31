# app/services/agent_service.py

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from app.tools.search_tool import web_search
from app.tools.calculator_tool import calculator
from app.tools.rag_tool import retrieve_user_docs

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

tools = [web_search, calculator, retrieve_user_docs]

agent = create_agent(
    tools=tools,
    model=llm,
)
