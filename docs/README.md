# 阅读文档：

从此目录构建的最新文档可以在 [detectron2.readthedocs.io](https://detectron2.readthedocs.io/) 上查看。此目录中的文档不适合在 GitHub 上阅读。

# 构建文档：

1. 按照 [INSTALL.md](https://github.com/facebookresearch/detectron2/blob/master/INSTALL.md) 中的说明安装 Detectron2。
2. 安装构建文档所需的额外库：
   - docutils==0.16
   - Sphinx==3.0.0
   - recommonmark==0.6.0
   - sphinx_rtd_theme
   - mock

3. 在此目录下运行 `make html` 命令以生成 HTML 格式的文档。