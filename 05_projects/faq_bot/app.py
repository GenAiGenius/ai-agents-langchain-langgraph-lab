from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from utils.config import OPENAI_API_KEY

# Sample documents
docs = [
    "LangChain helps you chain LLM calls.",
    "LangGraph helps you build agent workflows with loops and state."
]

# Split
splitter = RecursiveCharacterTextSplitter(chunk_size=50)
chunks = splitter.create_documents(docs)

# Embeddings + VectorDB
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
db = Chroma.from_documents(chunks, embeddings, persist_directory="chroma_db")
retriever = db.as_retriever()

# Model
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

# Retrieval QA
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Ask
query = "Which framework is good for workflows with loops?"
print("Q:", query)
print("A:", qa.run(query))
