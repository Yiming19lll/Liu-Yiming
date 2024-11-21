import pandas as pd

def read_data(file_path: str):
    data = pd.read_csv(file_path, sep=':', header=None, names=['category', 'text'], encoding='utf-8')
    print(f"Data read successfully: {len(data)} rows.")
    return data

if __name__ == "__main__":
    data = read_data("../data/运动鞋店铺知识库.txt")
    print(data.head())
