from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RAGEngine:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # dummy knowledge base (replace later)
        self.docs = [
            "EMI is calculated using principal, interest rate, and tenure.",
            "Late payment may attract penalty charges as per policy.",
            "Floating interest rates may change based on market conditions."
        ]

        embeddings = self.model.encode(self.docs)
        self.index = faiss.IndexFlatIP(embeddings.shape[1])
        self.index.add(np.array(embeddings).astype("float32"))

    def retrieve(self, query):
        q_emb = self.model.encode([query])
        scores, idx = self.index.search(np.array(q_emb).astype("float32"), 2)

        return [self.docs[i] for i in idx[0]]
