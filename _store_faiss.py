import os
import faiss
import numpy as np

def store_to_faiss(embeddings, save_path):
    # 创建目标目录（如果不存在）
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # 初始化 Faiss 索引
    dimension = len(embeddings[0])
    faiss_index = faiss.IndexFlatL2(dimension)

    # 添加嵌入向量
    faiss_index.add(np.array(embeddings, dtype='float32'))

    # 保存索引到文件
    faiss.write_index(faiss_index, save_path)
    print(f"Faiss index saved to {save_path}.")



