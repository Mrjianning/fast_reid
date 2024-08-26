# 设置内置数据集

Fastreid 支持一些内置数据集。假定数据集存在于由环境变量 `FASTREID_DATASETS` 指定的目录中。在此目录下，fastreid 期望数据集的结构符合下文描述的形式。

你可以通过 `export FASTREID_DATASETS=/path/to/datasets/` 设置内置数据集的位置。如果未设置，默认目录为当前工作目录下的 `datasets/`。

[模型库](https://github.com/JDAI-CV/fast-reid/blob/master/MODEL_ZOO.md) 包含了使用这些内置数据集的配置文件和模型。

## [Market1501](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Zheng_Scalable_Person_Re-Identification_ICCV_2015_paper.pdf) 数据集的期望结构

1. 从 [百度网盘](https://pan.baidu.com/s/1ntIi2Op) 或 [Google Drive](https://drive.google.com/file/d/0B8-rUzbwVRk0c054eEozWG9COHM/view) 下载数据集到 `datasets/` 目录
2. 解压数据集。数据集的结构如下：

```bash
datasets/
    Market-1501-v15.09.15/
        bounding_box_test/
        bounding_box_train/
```

## [DukeMTMC-reID](https://openaccess.thecvf.com/content_ICCV_2017/papers/Zheng_Unlabeled_Samples_Generated_ICCV_2017_paper.pdf) 数据集的期望结构

1. 下载数据集到 `datasets/` 目录
2. 解压数据集。数据集的结构如下：

```bash
datasets/
    DukeMTMC-reID/
        bounding_box_train/
        bounding_box_test/
```

## [MSMT17](https://arxiv.org/abs/1711.08565) 数据集的期望结构

1. 下载数据集到 `datasets/` 目录
2. 解压数据集。数据集的结构如下：

```bash
datasets/
    MSMT17_V2/
        mask_train_v2/
        mask_test_v2/
```
