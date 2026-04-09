from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from rank_bm25 import BM25Okapi

load_dotenv(find_dotenv())
file_path = Path(__file__).parent/"nodejs.pdf"

#Indexing (loading of the data)
loader = PyPDFLoader(file_path)
docs = loader.load()

#bm25 -> converting each doc to a list of words
tokenized_docs = [doc.page_content.split() for doc in docs]
bm25 = BM25Okapi(tokenized_docs)

#chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
chunks = text_splitter.split_documents(docs)

#vector embedding
embedding_model = OpenAIEmbeddings(model = "text-embedding-3-large")
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("indexing done....")