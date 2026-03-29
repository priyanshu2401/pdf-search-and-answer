from rag_pipeline import rag_pipeline
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

user_query = input("Ask Something >>> ")

print(rag_pipeline(user_query))