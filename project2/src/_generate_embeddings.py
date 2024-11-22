from llama_index.embeddings.dashscope import DashScopeEmbedding, DashScopeTextEmbeddingModels, DashScopeTextEmbeddingType

# 替换 YOUR_DASHSCOPE_API_KEY 为实际的 API Key
DASHSCOPE_API_KEY = "sk-c977de3aa4db4b5a8733b3e377fa9355"

def generate_embeddings(text_list):
    # 初始化 Embedding 模型并传入 API Key
    embedder = DashScopeEmbedding(
        model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2,
        text_type=DashScopeTextEmbeddingType.TEXT_TYPE_DOCUMENT,
        api_key=DASHSCOPE_API_KEY  # 在此传入 API Key
    )
    embeddings = embedder.get_text_embedding_batch(text_list)
    print("Embeddings generated successfully.")
    return embeddings

if __name__ == "__main__":
    # 确保 `1_read_data` 模块的路径正确
    from _read_data import read_data

    # 读取数据
    data = read_data(r"C:\Users\86155\PycharmProjects\PythonProject2\data\运动鞋店铺知识库.txt")

    # 调用向量化方法
    embeddings = generate_embeddings(data['text'].tolist())
    print(f"Generated {len(embeddings)} embeddings.")

