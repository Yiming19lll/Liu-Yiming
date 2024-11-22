# Project2: 简化后的离线链路

## 简介
`Project2` 是一个简化后的离线链路，支持：
- 读取数据。
- 将每行数据向量化
- 将向量写入faiss库
- 将数据导入到mysql


---

## 目录结构

```plaintext
Project2/
├── data/                          # 数据文件存储
│   ├── schema.sql                 # 数据库表结构
│   ├── ai_context.sql             # 数据插入 SQL 脚本
│   └── 运动鞋店铺知识库.txt        # 原始文本数据
├── faiss_index/                   # Faiss 索引存储
│   └── faiss_index.index          # 已生成的 Faiss 索引文件
├── src/                           # 源代码目录
│   ├── __init__.py                # 包初始化文件
│   ├── main.py                    # 主流程入口
│   ├── _read_data.py              # 数据读取模块
│   ├── _generate_embeddings.py    # 嵌入生成模块
│   ├── _store_faiss.py            # Faiss 存储模块
│   ├── _mysql_import.py           # MySQL 数据导入模块
│   ├── 01_write_to_faiss_test.py  # 测试 Faiss 索引代码
│   └── test.py                    # 在线查询服务测试代码
└── .venv/                         # 虚拟环境
