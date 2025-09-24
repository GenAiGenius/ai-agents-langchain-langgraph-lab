# 03_tools_and_agents/02_multi_tool_agent_langgraph.py
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.tools import tool
from utils.config import OPENAI_API_KEY
from utils.safe_math import eval_expr
import os

# ---- Tools ----

@tool("calculator")
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression. Returns the result in a sentence."""
    try:
        result = eval_expr(expression)
        return f"The result of the expression ({expression}) is {result}."
    except Exception as e:
        return f"Calculator error: {e}"

@tool("rag_search")
def rag_search(query: str) -> str:
    """Search an existing Chroma DB under ./chroma_db and return top passages."""
    persist_dir = os.environ.get("PERSIST_DIR", "chroma_db")
    if not os.path.isdir(persist_dir):
        return "No vector DB found. Run 02_rag/01_vector_store_setup.py or 02_rag/10_ingest_pdf.py first."
    try:
        vs = Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings(api_key=OPENAI_API_KEY))
        docs = vs.similarity_search(query, k=3)
        return "\n---\n".join(d.page_content for d in docs)
    except Exception as e:
        return f"RAG search error: {e}"

# ---- LLM + Agent ----
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
app = create_react_agent(llm, tools=[calculator, rag_search])

if __name__ == "__main__":
    # Q1: calculator
    res1 = app.invoke({"messages": [("user", "(12 * 9) / 3 + 5")]})
    print("A1:", res1["messages"][-1].content)

    # Q2: RAG
    res2 = app.invoke({"messages": [("user", "What is LangGraph and how is it different from LangChain? Use rag_search if helpful.")]} )
    print("A2:", res2["messages"][-1].content)
