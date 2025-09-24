from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from utils.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

prompt = ChatPromptTemplate.from_template("Give me 3 benefits of {tech}.")

# Runnable pipeline: prompt -> llm -> parse to string
chain = prompt | llm | StrOutputParser()

if __name__ == "__main__":
    print(chain.invoke({"tech": "LangGraph"}))