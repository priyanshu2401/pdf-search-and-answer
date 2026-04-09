## 📊 Evaluation Results (RAGAS)

We evaluated the RAG pipeline using RAGAS metrics across different stages.

| Version            | Faithfulness | Answer Relevancy | Context Precision | Context Recall |
|--------------------|-------------|------------------|------------------|----------------|
| Baseline (Dense)   | 0.70        | 0.78             | 0.80             | 0.76           |
| Hybrid Retrieval   | 0.75        | 0.78             | 0.67             | 0.70           |
| + Re-ranking       | 0.76        | 0.78             | 0.72             | 0.93           |

---

### 📌 Observations

- Hybrid retrieval significantly improved **context recall**, ensuring more relevant information is retrieved.
- Initial hybrid approach introduced noise, reducing precision.
- LLM-based re-ranking improved **context precision** by filtering low-quality chunks.
- Final system achieves a strong balance between **recall and precision**, improving answer grounding.

---

### 🧠 Metrics Explained

- **Faithfulness** → How well the answer is grounded in retrieved context  
- **Answer Relevancy** → How relevant the answer is to the query  
- **Context Precision** → Proportion of retrieved chunks that are relevant  
- **Context Recall** → Ability to retrieve all relevant information  

---

## 🔍 System Architecture

1. **Dense Retrieval** → Semantic search using embeddings (Qdrant)  
2. **BM25 Retrieval** → Keyword-based retrieval  
3. **Hybrid Search** → Combines dense + sparse retrieval  
4. **Re-ranking** → LLM-based scoring and filtering of documents  
5. **Answer Generation** → LLM generates response using filtered context  

---

## 🚀 Key Features

- Hybrid Retrieval (Dense + BM25)
- LLM-based Re-ranking
- Evaluation using RAGAS
- Metric-driven improvements
- Modular pipeline design
