import numpy as np
import os

def load_feature(file_path):
    """
    加载单个 .npy 文件并返回特征向量。
    """
    return np.load(file_path).squeeze()  # 使用 squeeze 将特征从 (1, 2048) 转换为 (2048,)

def compute_cosine_similarity(feature1, feature2):
    """
    计算两个特征向量之间的余弦相似度。
    """
    similarity = np.dot(feature1, feature2) / (np.linalg.norm(feature1) * np.linalg.norm(feature2))
    return similarity

if __name__ == "__main__":
    # 设置两个 .npy 文件的路径
    file1_path = "gallery_dir/ljn.npy"  # 替换为第一个 .npy 文件的路径
    file2_path = "gallery_dir/lxy.npy"  # 替换为第二个 .npy 文件的路径

    # 加载两个特征向量
    feature1 = load_feature(file1_path)
    feature2 = load_feature(file2_path)

    # 计算两个特征向量之间的相似度
    similarity_score = compute_cosine_similarity(feature1, feature2)

    print(f"{os.path.basename(file1_path)} 和 {os.path.basename(file2_path)} 之间的相似度: {similarity_score:.4f}")
