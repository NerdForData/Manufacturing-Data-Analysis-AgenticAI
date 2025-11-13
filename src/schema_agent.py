from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SchemaAgent:
    def __init__(self, model_name: str = "all-mpnet-base-v2", device: str = "cpu"):
        try:
            self.model = SentenceTransformer(model_name, device=device)
        except Exception:
            self.model = None

    def embed_texts(self, texts):
        if self.model:
            return self.model.encode(texts, convert_to_numpy=True)
        rng = np.random.RandomState(0)
        return rng.rand(len(texts), 384)

    def propose_mappings(self, cols_a, cols_b, threshold: float = 0.6):
        ea = self.embed_texts(cols_a)
        eb = self.embed_texts(cols_b)
        sims = cosine_similarity(ea, eb)
        mappings = {}
        for i, a in enumerate(cols_a):
            j = int(np.argmax(sims[i]))
            score = float(sims[i, j])
            if score >= threshold:
                mappings[a] = {"match": cols_b[j], "score": round(score, 3)}
        return mappings
