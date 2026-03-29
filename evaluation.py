from rag_pipeline import rag_pipeline,retriever
from eval_data import eval_data
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from dotenv import load_dotenv
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)

load_dotenv()

retrieved = retriever()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
ragas_embeddings = LangchainEmbeddingsWrapper(embedding_model)

llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))

# collecting answers (prediction) and contexts (raw chunks)
questions = []
answers = []
contexts = []
ground_truths = []

for i in eval_data:
    ques = i["question"]
    gt = i["ground_truth"]

    search_results = retrieved.invoke(ques)
    retrieved_context = [item.page_content for item in search_results]
    
    ans = rag_pipeline(ques)

    questions.append(ques)
    answers.append(ans)
    contexts.append(retrieved_context)
    ground_truths.append(gt)


# Convert to dataset
dataset = Dataset.from_dict({
    "question": questions,
    "answer": answers,
    "contexts": contexts,
    "ground_truth": ground_truths
})


# Evaluate
result = evaluate(
    dataset,
    llm=llm,
    embeddings=ragas_embeddings,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,
    ]
)

print("\nFINAL SCORES:")
print(result)