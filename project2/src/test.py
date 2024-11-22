import numpy as np
import faiss
import pandas as pd

# 加载索引
def load_faiss_index(index_path):
    try:
        index = faiss.read_index(index_path)
        print(f"Index loaded successfully. Number of vectors: {index.ntotal}, Dimension: {index.d}")
        return index
    except Exception as e:
        print(f"Failed to load index: {e}")
        return None

# 查询索引
def query_faiss_index(index, query_vector, k=5):
    try:
        # 确保查询向量的维度正确
        query_vector = np.array([query_vector], dtype='float32')
        assert query_vector.shape[1] == index.d, f"Query vector dimension mismatch: {query_vector.shape[1]} != {index.d}"

        distances, indices = index.search(query_vector, k=k)
        return distances, indices
    except Exception as e:
        print(f"Query failed: {e}")
        return None, None

# 加载原始数据
def load_original_data(data_path):
    try:
        data = pd.read_csv(data_path, sep=':', header=None, names=['category', 'text'], encoding='utf-8')
        print(f"Original data loaded successfully. Total rows: {len(data)}")
        return data
    except Exception as e:
        print(f"Failed to load original data: {e}")
        return None

if __name__ == "__main__":
    # 配置文件路径
    index_path = "C:/Users/86155/PycharmProjects/PythonProject2/faiss_index/faiss_index.index"
    data_path = "C:/Users/86155/PycharmProjects/PythonProject2/data/运动鞋店铺知识库.txt"

    # 加载索引
    faiss_index = load_faiss_index(index_path)

    # 加载原始数据
    original_data = load_original_data(data_path)

    if faiss_index and original_data is not None:
        # 生成随机查询向量
        query_vector = np.random.rand(faiss_index.d).astype("float32")

        # 查询前 5 个最近邻
        distances, indices = query_faiss_index(faiss_index, query_vector, k=5)

        if distances is not None and indices is not None:
            print("\nQuery Results:")
            for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
                print(f"Rank {i + 1}:")
                print(f"  Index: {idx}")
                print(f"  Distance: {dist}")
                if idx < len(original_data):
                    print(f"  Original Text: {original_data['text'][idx]}")
                else:
                    print("  Original Text: Index out of range.")
