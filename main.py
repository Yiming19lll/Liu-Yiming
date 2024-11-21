import sys
import os

# 添加项目根目录到模块搜索路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src._read_data import read_data
from src._generate_embeddings import generate_embeddings
from src._store_faiss import store_to_faiss
from src._mysql_import import import_to_mysql


def main():
    # Step 1: 数据读取
    data = read_data("./data/运动鞋店铺知识库.txt")

    # Step 2: 向量化
    embeddings = generate_embeddings(data['text'].tolist())

    # Step 3: 存储到 Faiss
    store_to_faiss(embeddings, "./faiss_index/faiss_index.index")

    # Step 4: 导入 MySQL
    import_to_mysql("./data/schema.sql", "./data/ai_context.sql")

if __name__ == "__main__":
    main()
