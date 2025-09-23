from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from utils.config import OPENAI_API_KEY

persist_dir = "chroma_db"

embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 3})

llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

# Conversational RAG keeps chat history and uses it to refine answers
crc = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)

chat_history = []

def ask(q):
    global chat_history
    result = crc.invoke({"question": q, "chat_history": chat_history})
    answer = result["answer"]
    chat_history.append((q, answer))
    print("\nUser:", q)
    print("Bot :", answer)

if __name__ == "__main__":
    ask("Remind me what RAG means.")
    ask("And how does LangGraph relate to it? Keep it short.")
    ask("Based on our chat, what DB are we using?")
