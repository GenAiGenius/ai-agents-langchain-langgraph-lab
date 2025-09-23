# 02_rag — Retrieval Augmented Generation

Practice RAG patterns using LangChain + ChromaDB.

## Files
- **01_vector_store_setup.py** — Create embeddings and a Chroma vector store.
- **02_simple_rag.py** — Ask questions over a small knowledge base.
- **03_rag_with_memory.py** — Conversational RAG that remembers chat history.

## Quick start
```bash
pip install -r requirements.txt
cp .env.example .env   # Set OPENAI_API_KEY
python 02_rag/01_vector_store_setup.py
python 02_rag/02_simple_rag.py
python 02_rag/03_rag_with_memory.py
```

## Notes
- Persistence directory is `chroma_db/` (ignored by git).
- Replace the sample `docs` list with your own text or load files programmatically.
