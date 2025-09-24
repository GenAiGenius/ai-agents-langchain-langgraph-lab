from langchain_openai import ChatOpenAI
from langchain.tools import Tool
import math
from utils.config import OPENAI_API_KEY
from langgraph.prebuilt import create_react_agent

# Tool
def square_root_tool(x: str) -> str:
    try:
        return str(math.sqrt(float(x)))
    except Exception as e:
        return f"Error: {e}"

tools = [
    Tool(
        name="square_root",  # <-- no spaces or special chars
        func=square_root_tool,
        description="Calculate the square root of a number."
    )
]

# Initialize model
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

app = create_react_agent(llm, tools)

if __name__ == "__main__":
    result = app.invoke({"messages": [("user", "What is the square root of 144?")]})
    final = result["messages"][-1].content
    print("Agent Answer:", final)
