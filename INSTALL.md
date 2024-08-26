# 安装指南

## 环境要求

- Linux 或 macOS，Python 版本 ≥ 3.6
- PyTorch 版本 ≥ 1.6
- 与 Pytorch 版本匹配的 torchvision。你可以在 [pytorch.org](https://pytorch.org/) 上一起安装它们，以确保版本匹配。
- [yacs](https://github.com/rbgirshick/yacs)
- Cython（可选，用于编译评估代码）
- tensorboard（可视化需要）：`pip install tensorboard`
- gdown（用于自动下载预训练模型）
- sklearn
- termcolor
- tabulate
- [faiss](https://github.com/facebookresearch/faiss) `pip install faiss-cpu`

# 使用 Conda 设置环境
```shell
conda create -n fastreid python=3.7
conda activate fastreid
conda install pytorch==1.6.0 torchvision tensorboard -c pytorch
pip install -r docs/requirements.txt
```

# 使用 Docker 设置环境

请查看 [docker 文件夹](docker) 了解详细信息。