from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.agents import Tool
from utils.config import OPENAI_API_KEY
import math

# Define a simple tool
def square_root_tool(x: str) -> str:
    try:
        value = float(x)
        return str(math.sqrt(value))
    except Exception as e:
        return f"Error: {e}"

tools = [
    Tool(
        name="Square Root Calculator",
        func=square_root_tool,
        description="useful for when you need to calculate the square root of a number"
    )
]

# Initialize model
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

# Create agent with tool
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

if __name__ == "__main__":
    result = agent.run("What is the square root of 144?")
    print("Agent Answer:", result)
