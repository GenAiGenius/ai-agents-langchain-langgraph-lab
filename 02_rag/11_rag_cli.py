from utils.config import OPENAI_API_KEY
from utils.rag_helpers import get_embeddings, get_vector_store
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

PERSIST_DIR = "chroma_db"

if __name__ == "__main__":
    embeddings = get_embeddings(api_key=OPENAI_API_KEY)
    vs = get_vector_store(persist_directory=PERSIST_DIR, embeddings=embeddings)

    retriever = vs.as_retriever(search_kwargs={"k": 4})
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    print("🔎 RAG CLI (type 'exit' to quit)")
    while True:
        try:
            q = input("Q> ").strip()
        except EOFError:
            break
        if not q or q.lower() in {"exit", "quit"}:
            break
        print("A>", qa.run(q))
