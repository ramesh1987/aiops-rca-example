import faiss
import numpy as np

dimension = 3  # 3 features
index = faiss.IndexFlatL2(dimension)
id_to_metadata = {}

def add_vector(vector, metadata, doc_id):
    vector_np = np.array([vector]).astype('float32')
    index.add(vector_np)
    id_to_metadata[index.ntotal - 1] = metadata

def search_similar(vector, top_k=2):
    vector_np = np.array([vector]).astype('float32')
    D, I = index.search(vector_np, k=top_k)
    results = [id_to_metadata.get(i, {'incident': 'unknown'}) for i in I[0]]
    return results
