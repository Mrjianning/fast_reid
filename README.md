以下是 FastReID 的中文注释：

---

<img src=".github/FastReID-Logo.png" width="300" >

[![Gitter](https://badges.gitter.im/fast-reid/community.svg)](https://gitter.im/fast-reid/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Gitter: [fast-reid/community](https://gitter.im/fast-reid/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

微信:

<img src=".github/wechat_group.png" width="150" >

FastReID 是一个实现最先进再识别算法的研究平台。它是先前版本 [reid strong baseline](https://github.com/michuanhaohao/reid-strong-baseline) 的全新重写版本。

## 更新内容

- [2021年9月] [DG-ReID](https://github.com/xiaomingzhid/sskd) 已更新，您可以查看 [论文](https://arxiv.org/pdf/2108.05045.pdf)。
- [2021年6月] 支持 [Contiguous parameters](https://github.com/PhilJd/contiguous_pytorch_params)，现在可以加速约20%。
- [2021年5月] 支持 Vision Transformer 骨干网络，详见 `configs/Market1501/bagtricks_vit.yml`。
- [2021年4月] [FastFace](projects/FastFace) 中支持部分 FC。
- [2021年1月] [FastRT](projects/FastRT) 中发布了 TRT 网络定义 API！感谢 [Darren](https://github.com/TCHeish) 的贡献。
- [2021年1月] 基于 fastreid 的 NAIC20（reid track）[1-等奖方案](projects/NAIC20) 已发布！
- [2021年1月] FastReID V1.0 已发布！🎉
  支持除 reid 以外的许多任务，如图像检索和人脸识别。详见 [发布说明](https://github.com/JDAI-CV/fast-reid/releases/tag/v1.0.0)。
- [2020年10月] 基于 fastreid 的 [Hyper-Parameter Optimization](projects/FastTune) 已添加。详见 `projects/FastTune`。
- [2020年9月] 基于 fastreid 的 [person attribute recognition](projects/FastAttr) 已添加。详见 `projects/FastAttr`。
- [2020年9月] 支持 `apex` 的自动混合精度训练。设置 `cfg.SOLVER.FP16_ENABLED=True` 开启该功能。
- [2020年8月] 支持 [Model Distillation](projects/FastDistill)，感谢 [guan'an wang](https://github.com/wangguanan) 的贡献。
- [2020年8月] 支持 ONNX/TensorRT 转换器。
- [2020年7月] 支持多 GPU 分布式训练，训练速度显著加快。
- 包含更多功能，如圈损失（circle loss）、丰富的可视化方法和评估指标、在传统、跨域、部分和车辆 re-id 上的 SoTA 结果、同时在多个数据集上进行测试等。
- 可以作为库使用，支持基于其构建的[不同项目](projects)。我们将以这种方式开源更多研究项目。
- 移除了 [ignite](https://github.com/pytorch/ignite)（一个高级库）依赖，并基于 [PyTorch](https://pytorch.org/) 进行构建。

我们撰写了关于此工具箱的 [fastreid 介绍](https://l1aoxingyu.github.io/blogpages/reid/fastreid/2020/05/29/fastreid.html) 和 [fastreid v1.0](https://l1aoxingyu.github.io/blogpages/reid/fastreid/2021/04/28/fastreid-v1.html) 。

## 更新日志

有关详细信息和发布历史，请参阅 [changelog.md](CHANGELOG.md)。

## 安装

请参阅 [INSTALL.md](INSTALL.md)。

## 快速入门

设计的架构遵循此指南 [PyTorch-Project-Template](https://github.com/L1aoXingyu/PyTorch-Project-Template)，您可以自行查看每个文件夹的用途。

请参阅 [GETTING_STARTED.md](GETTING_STARTED.md)。

在我们的 [文档](https://fast-reid.readthedocs.io/) 中了解更多内容。另请参阅 [projects/](projects) 以了解一些基于 fastreid 构建的项目。

## 模型库和基线

我们提供了一大套基线结果和训练模型，可以在 [Fastreid Model Zoo](MODEL_ZOO.md) 中下载。

## 部署

我们在 [Fastreid deploy](tools/deploy) 中提供了一些示例和脚本，以将 fastreid 模型转换为 Caffe、ONNX 和 TensorRT 格式。

## 许可证

Fastreid 根据 [Apache 2.0 许可证](LICENSE) 发布。

## 引用 FastReID

如果您在研究中使用了 FastReID，或希望引用模型库中发布的基线结果，请使用以下 BibTeX 条目。

```BibTeX
@article{he2020fastreid,
  title={FastReID: A Pytorch Toolbox for General Instance Re-identification},
  author={He, Lingxiao and Liao, Xingyu and Liu, Wu and Liu, Xinchen and Cheng, Peng and Mei, Tao},
  journal={arXiv preprint arXiv:2006.02631},
  year={2020}
}
```

---