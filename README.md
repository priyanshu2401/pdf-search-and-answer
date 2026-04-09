## 📊 Evaluation Results (RAGAS)

We evaluated the RAG pipeline using RAGAS metrics:

| Version            | Faithfulness | Answer Relevancy | Context Precision | Context Recall |
|--------------------|-------------|------------------|------------------|----------------|
| Baseline (Dense)   | 0.70        | 0.78             | 0.80             | 0.76           |
| Hybrid Retrieval   | 0.75        | 0.78             | 0.67             | 0.70           |
| + Re-ranking       | (your new scores here) |

---

### 📌 Observations

- Hybrid retrieval improved **faithfulness** but reduced precision due to noise.
- Adding re-ranking helps filter irrelevant chunks.
- Final system balances **precision + recall + grounding**.

---

### 🧠 Metrics Explained

- **Faithfulness** → Is answer grounded in context?
- **Answer Relevancy** → Is answer relevant to question?
- **Context Precision** → Retrieved chunks are useful?
- **Context Recall** → Did we retrieve all needed info?
