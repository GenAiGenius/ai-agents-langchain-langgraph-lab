from typing import Optional
import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_embeddings(api_key: Optional[str] = None):
    return OpenAIEmbeddings(api_key=api_key)

def get_splitter(chunk_size: int = 800, chunk_overlap: int = 80):
    return RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

def get_vector_store(persist_directory: str = "chroma_db", embeddings=None):
    os.makedirs(persist_directory, exist_ok=True)
    if embeddings is None:
        embeddings = get_embeddings()
    return Chroma(persist_directory=persist_directory, embedding_function=embeddings)
