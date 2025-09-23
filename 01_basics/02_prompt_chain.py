from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from utils.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

prompt = ChatPromptTemplate.from_template("Give me 3 benefits of {tech}.")
chain = LLMChain(prompt=prompt, llm=llm)

if __name__ == "__main__":
    print(chain.run("LangGraph"))
