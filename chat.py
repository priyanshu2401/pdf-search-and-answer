from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv(find_dotenv())
openai_client = OpenAI()

#Vector embedding
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    embedding=embedding_model,
    collection_name="learning_rag"
)

user_query = input("Ask something->  ")

search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([
    f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
    for result in search_results
])

SYSTEM_PROMPT = f"""
You are a helpful AI assistant who answers user query based on the available context retrieved from a PDF file along with page content and page number.

You ahould answer the user based on the following context and navigate the user to open the right page number to know more.

context = {context}
"""

response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":user_query}
    ]
)

print(response.choices[0].message.content)