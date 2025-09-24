from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from utils.config import OPENAI_API_KEY

# Load existing vector store (created by 01_vector_store_setup.py)
persist_dir = "chroma_db"

embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

retriever = db.as_retriever(search_kwargs={"k": 3})
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

queries = [
    "What is LangGraph used for?",
    "Explain RAG in one line.",
    "Which vector DB is used here?"
]

for q in queries:
    print("\nQ:", q)
    print("A:", qa.run(q))
