from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv(find_dotenv())
openai_client = OpenAI()

def retriever():
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
    vector_db = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        embedding=embedding_model,
        collection_name="learning_rag"
    )

    return vector_db.as_retriever(search_kwargs={"k":4})

def rag_pipeline(query:str):

    retrieved = retriever()
    search_results = retrieved.invoke(query)

    print(len(search_results))

    for i,doc in enumerate(search_results):
        print(f"----Result {i+1}----")
        print(doc.page_content)
        print("==========================")

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
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":query}
        ]
    )

    return response.choices[0].message.content

