from rag_pipeline import rag_pipeline
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from rag_pipeline import sparse_retriever

load_dotenv()

user_query = input("Ask Something >>> ")

sparse_retriever(user_query)
print(rag_pipeline(user_query))