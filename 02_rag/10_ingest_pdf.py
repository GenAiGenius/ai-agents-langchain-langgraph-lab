import os
from glob import glob
from utils.config import OPENAI_API_KEY
from utils.rag_helpers import get_embeddings, get_splitter, get_vector_store
from langchain_community.document_loaders import PyPDFLoader

DATA_DIR = os.environ.get("DATA_DIR", "data")
PERSIST_DIR = os.environ.get("PERSIST_DIR", "chroma_db")

def load_pdfs(data_dir: str):
    pdf_paths = sorted(glob(os.path.join(data_dir, "*.pdf")))
    docs = []
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())
    return docs

if __name__ == "__main__":
    pdf_docs = load_pdfs(DATA_DIR)
    if not pdf_docs:
        print(f"⚠️ No PDFs found in '{DATA_DIR}'. Drop some .pdf files there and re-run.")
        raise SystemExit(0)

    splitter = get_splitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(pdf_docs)

    embeddings = get_embeddings(api_key=OPENAI_API_KEY)
    vs = get_vector_store(persist_directory=PERSIST_DIR, embeddings=embeddings)
    vs.add_documents(chunks)
    print(f"✅ Ingested {len(chunks)} chunks from {len(pdf_docs)} PDF(s) into '{PERSIST_DIR}'.")
