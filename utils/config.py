import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("⚠️ Please set OPENAI_API_KEY in your .env file")
