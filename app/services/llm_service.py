from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from app.utils.memory_store import get_user_messages, save_message

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


def get_response(query: str, user: str):
  memory = get_user_messages(user)

  messages = memory + [{"role": "user", "content": query}]

  response = llm.invoke(messages)

  save_message(user, "user", query)
  save_message(user, "assistant", response.content)

  return response.content