import faiss
import numpy as np

def query_faiss(index_path, query_vector, top_k=5):
    index = faiss.read_index(index_path)
    query_vector = np.array([query_vector], dtype='float32')
    assert query_vector.shape[1] == index.d, f"Query vector dimension mismatch: {query_vector.shape[1]} != {index.d}"
    distances, indices = index.search(query_vector, top_k)
    print("Query Results:")
    print("Distances:", distances)
    print("Indices:", indices)

if __name__ == "__main__":
    # 查询维度调整为 1536
    query_vector = [0.1] * 1536
    query_faiss("./faiss_index/faiss_index.index", query_vector)

