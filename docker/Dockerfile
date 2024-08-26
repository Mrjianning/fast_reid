FROM nvidia/cuda:10.1-cudnn7-devel

# 修复可能由于 NVIDIA docker 资源列表导致的问题
# 参见 https://github.com/NVIDIA/nvidia-docker/issues/1632
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list

# 设置非交互模式以避免在安装软件包时出现提示
ENV DEBIAN_FRONTEND noninteractive

# 更新 apt 包列表，并安装必要的软件包
RUN apt-get update && apt-get install -y \
	python3-opencv ca-certificates python3-dev git wget sudo ninja-build

# 将 python3 的符号链接创建为 python
RUN ln -sv /usr/bin/python3 /usr/bin/python

# 创建一个非 root 用户
ARG USER_ID=1000
RUN useradd -m --no-log-init --system  --uid ${USER_ID} appuser -g sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# 切换到新创建的非 root 用户
USER appuser
WORKDIR /home/appuser

# 为了解决某些依赖问题，设置 PATH 环境变量
# 参见 https://github.com/facebookresearch/detectron2/issues/3933
ENV PATH="/home/appuser/.local/bin:${PATH}"

# 下载并安装 pip（适用于 Python 3.6）
RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py && \
	python3 get-pip.py --user && \
	rm get-pip.py

# 安装依赖项
# 如果你使用不同版本的 CUDA，请参见 https://pytorch.org/ 获取其他安装选项
RUN pip install --user tensorboard cmake   # apt-get 提供的 cmake 版本太旧
RUN pip install --user torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/cu101/torch_stable.html

# 通过 Tsinghua 镜像源安装 Python 包以加速下载
RUN pip install --user -i https://pypi.tuna.tsinghua.edu.cn/simple tensorboard opencv-python cython yacs termcolor scikit-learn tabulate gdown gpustat faiss-gpu ipdb h5py
