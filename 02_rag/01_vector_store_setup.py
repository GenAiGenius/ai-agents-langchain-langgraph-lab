from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from utils.config import OPENAI_API_KEY
import os

# --- Sample corpus (replace with your own content) ---
docs = [
    "LangChain is a framework to compose LLM apps with prompts, chains, tools and memory.",
    "LangGraph builds on LangChain to create stateful, loop-capable, multi-agent workflows.",
    "RAG stands for Retrieval-Augmented Generation, combining vector search with generation.",
    "Chroma is a lightweight vector database often used for dev & prototypes."
]

# 1) Chunk the docs
splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
documents = splitter.create_documents(docs)

# 2) Create embeddings
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

# 3) Create / persist Chroma DB
persist_dir = "chroma_db"
os.makedirs(persist_dir, exist_ok=True)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=persist_dir
)

print("✅ Vector store created.")
print("Collection count:", vector_store._collection.count())
print(f"Persisted at: {persist_dir}")
