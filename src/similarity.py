import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class SimilarityEngine:
    def __init__(self, dataset_path, threshold=0.85):
        self.threshold = threshold
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        with open(dataset_path, "r") as f:
            self.data = json.load(f)

        self.questions = [item["input"] for item in self.data]
        self.responses = [item["output"] for item in self.data]

        embeddings = self.model.encode(self.questions)
        self.index = faiss.IndexFlatIP(embeddings.shape[1])
        self.index.add(np.array(embeddings).astype("float32"))

    def search(self, query):
        q_emb = self.model.encode([query])
        scores, idx = self.index.search(np.array(q_emb).astype("float32"), 1)

        score = float(scores[0][0])
        best_idx = int(idx[0][0])

        if score >= self.threshold:
            return True, self.responses[best_idx], score

        return False, None, score
