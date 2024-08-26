import numpy as np
import os

def load_features_from_directory(directory):
    """
    从指定目录加载所有 .npy 文件并返回字典，键为文件名，值为特征。
    """
    features = {}
    for file_name in os.listdir(directory):
        if file_name.endswith('.npy'):
            file_path = os.path.join(directory, file_name)
            features[file_name] = np.load(file_path).squeeze()  # 使用squeeze将特征从(1, 2048)转换为(2048,)
    return features

def compute_cosine_similarity(query_feature, gallery_features):
    """
    计算查询特征与画廊特征之间的余弦相似度。
    """
    similarities = {}
    for file_name, gallery_feature in gallery_features.items():
        # 计算余弦相似度
        similarity = np.dot(query_feature, gallery_feature) / (np.linalg.norm(query_feature) * np.linalg.norm(gallery_feature))
        similarities[file_name] = similarity
    return similarities

def find_most_similar(similarities):
    """
    根据相似度字典，找到最相似的文件名。
    """
    most_similar_file = max(similarities, key=similarities.get)
    return most_similar_file, similarities[most_similar_file]

if __name__ == "__main__":
    # 设置查询特征和画廊特征的目录路径
    query_dir = "query_dir"  # 替换为查询特征的目录路径
    gallery_dir = "gallery_dir"  # 替换为画廊特征的目录路径

    # 加载查询特征和画廊特征
    query_features = load_features_from_directory(query_dir)
    gallery_features = load_features_from_directory(gallery_dir)

    # 遍历查询特征
    for query_file_name, query_feature in query_features.items():
        print(f"查询文件: {query_file_name}")

        # 计算相似度
        similarities = compute_cosine_similarity(query_feature, gallery_features)

        # 找到最相似的画廊文件
        most_similar_file, similarity_score = find_most_similar(similarities)

        print(f"最相似的画廊文件: {most_similar_file}，相似度: {similarity_score:.4f}\n")
