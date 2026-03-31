from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Safely evaluate arithmetic expressions."""
    try:
        allowed = "0123456789+-*/(). "
        if not all(c in allowed for c in expression):
            return "Invalid expression"

        result = eval(expression)
        return str(result)

    except Exception:
        return "Calculation failed"