from langchain_openai import ChatOpenAI
from utils.config import OPENAI_API_KEY
from utils.logger import get_logger

logger = get_logger("HelloWorld")

# Initialize model
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

# Run query
response = llm.invoke("Hello! Explain LangChain in one line.")
logger.info(response.content)
