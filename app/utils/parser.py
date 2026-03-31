# app/utils/parser.py

def normalize_llm_content(content):
  if isinstance(content, list):
    return "\n".join(
      item.get("text", str(item))
      if isinstance(item, dict)
      else str(item)
      for item in content
    )
  return str(content)