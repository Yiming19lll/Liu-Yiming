import numpy as np
import faiss

# 加载索引
index_path = "C:/Users/86155/PycharmProjects/PythonProject2/faiss_index/faiss_index.index"
faiss_read_index = faiss.read_index(index_path)

# 假设索引是 1536 维
query_vector = np.random.rand(1536).astype("float32")

# 查询前 5 个相似向量
distances, indices = faiss_read_index.search(np.array([query_vector]).astype('float32'), k=5)

print(f"Indices of nearest neighbors: {indices}")
print(f"Distances: {distances}")

