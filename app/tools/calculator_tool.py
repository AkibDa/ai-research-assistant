from langchain.tools import tool
from sympy import sympify

@tool
def calculator(expression: str) -> str:
    """Use for arithmetic, algebra, symbolic math, and simplification."""
    try:
        result = sympify(expression)
        return str(result)
    except Exception:
        return "Calculation failed"