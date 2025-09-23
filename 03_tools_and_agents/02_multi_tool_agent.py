from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from utils.safe_math import eval_expr
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from utils.config import OPENAI_API_KEY
import os

# --- Tools ---
def calc_tool(q: str) -> str:
    """Evaluate a basic arithmetic expression. Supports +, -, *, /, **, %, //, parentheses."""
    try:
        return str(eval_expr(q))
    except Exception as e:
        return f"Calculator error: {e}"

def rag_search_tool(q: str) -> str:
    """Search an existing Chroma DB (created under ./chroma_db). Returns top document texts."""
    persist_dir = os.environ.get("PERSIST_DIR", "chroma_db")
    if not os.path.isdir(persist_dir):
        return "No vector DB found. Run 02_rag/01_vector_store_setup.py or 02_rag/10_ingest_pdf.py first."
    try:
        vs = Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings(api_key=OPENAI_API_KEY))
        docs = vs.similarity_search(q, k=3)
        return "\n---\n".join(d.page_content for d in docs)
    except Exception as e:
        return f"RAG search error: {e}"

tools = [
    Tool(
        name="Calculator",
        func=calc_tool,
        description="Useful for math questions. Input should be a valid arithmetic expression."
    ),
    Tool(
        name="RAGSearch",
        func=rag_search_tool,
        description="Search local knowledge base (Chroma) for relevant passages."
    ),
]

# --- Agent ---
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    q1 = "(12 * 9) / 3 + 5"
    print("Q1:", q1)
    print("A1:", agent.run(q1))

    q2 = "What is LangGraph and how is it different from LangChain? Use RAGSearch if helpful."
    print("\nQ2:", q2)
    print("A2:", agent.run(q2))
