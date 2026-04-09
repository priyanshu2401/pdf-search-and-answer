from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from index import bm25,docs

load_dotenv(find_dotenv())
openai_client = OpenAI()

# dense retriever, based on embedding
def dense_retriever():
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
    vector_db = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        embedding=embedding_model,
        collection_name="learning_rag"
    )

    return vector_db.as_retriever(search_kwargs={"k":4})

# sparse retriever, based on keywords 
def sparse_retriever(query:str):
    tokenized_query = query.split()
    scores = bm25.get_scores(tokenized_query)

    top_k_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:4]

    return [docs[i] for i in top_k_indices]

#hybrid retriever -> dense + sparse
def hybrid_retriever(query:str):
    dense_retrieved = dense_retriever()
    dense_results = dense_retrieved.invoke(query)

    sparse_results = sparse_retriever(query)
    combined = dense_results + sparse_results

    unique_docs = {doc.page_content: doc for doc in combined}

    return list(unique_docs.values())


def rag_pipeline(query:str):

    search_results = hybrid_retriever(query)

    print(f"\nTotal retrieved: {len(search_results)}")

    for i, doc in enumerate(search_results):
        print(f"----Result {i+1}----")
        print(doc.page_content[:200])
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

