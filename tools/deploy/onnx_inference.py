# 编码: utf-8
"""
@作者:  xingyu liao
@联系: sherlockliao01@gmail.com
"""

import argparse
import glob
import os

import cv2  # 导入OpenCV库，用于图像处理
import numpy as np  # 导入NumPy库，用于数值计算
import onnxruntime  # 导入ONNX Runtime库，用于加载和运行ONNX模型
import tqdm  # 导入tqdm库，用于显示进度条


def get_parser():
    parser = argparse.ArgumentParser(description="ONNX模型推理")

    parser.add_argument(
        "--model-path",
        default="onnx_model/baseline.onnx",
        help="ONNX模型路径"
    )
    parser.add_argument(
        "--input",
        nargs="+",
        help="一个空格分隔的输入图像列表；"
             "或者一个单一的glob模式，如 'directory/*.jpg'",
    )
    parser.add_argument(
        "--output",
        default='onnx_output',
        help='保存转换后的Caffe模型的路径'
    )
    parser.add_argument(
        "--height",
        type=int,
        default=256,
        help="图像的高度"
    )
    parser.add_argument(
        "--width",
        type=int,
        default=128,
        help="图像的宽度"
    )
    return parser


def preprocess(image_path, image_height, image_width):
    original_image = cv2.imread(image_path)
    # 模型期望RGB格式的输入
    original_image = original_image[:, :, ::-1]

    # 对图像应用预处理操作。
    img = cv2.resize(original_image, (image_width, image_height), interpolation=cv2.INTER_CUBIC)
    img = img.astype("float32").transpose(2, 0, 1)[np.newaxis]  # 转换为 (1, 3, h, w) 的形状
    return img


def normalize(nparray, order=2, axis=-1):
    """沿指定轴对N维NumPy数组进行归一化。"""
    norm = np.linalg.norm(nparray, ord=order, axis=axis, keepdims=True)
    return nparray / (norm + np.finfo(np.float32).eps)


if __name__ == "__main__":
    args = get_parser().parse_args()

    ort_sess = onnxruntime.InferenceSession(args.model_path)

    input_name = ort_sess.get_inputs()[0].name

    if not os.path.exists(args.output): os.makedirs(args.output)

    if args.input:
        if os.path.isdir(args.input[0]):
            args.input = glob.glob(os.path.expanduser(args.input[0]))
            assert args.input, "未找到输入路径"
        for path in tqdm.tqdm(args.input):
            image = preprocess(path, args.height, args.width)
            feat = ort_sess.run(None, {input_name: image})[0]
            feat = normalize(feat, axis=1)
            np.save(os.path.join(args.output, path.replace('.jpg', '.npy').split('/')[-1]), feat)
