# Fastreid 入门指南

## 准备预训练模型

如果你使用的是 Fastreid 支持的骨干网络，你无需做任何操作，Fastreid 会自动下载预训练模型。但如果你的网络未连接互联网，你可以手动下载预训练模型并将其放在 `~/.cache/torch/checkpoints` 目录下。

如果你想使用其他预训练模型，例如 MoCo 预训练模型，你可以自行下载，并在 `configs/Base-bagtricks.yml` 文件中设置预训练模型的路径。

## 使用 Cython 编译加速评估

```bash
cd fastreid/evaluation/rank_cylib; make all
```

## 命令行中的训练与评估

我们在 "tools/train_net.py" 提供了一个脚本，用于训练 Fastreid 中提供的所有配置文件。你可以参考它来编写自己的训练脚本。

要使用 "train_net.py" 训练模型，首先按照 [datasets/README.md](https://github.com/JDAI-CV/fast-reid/tree/master/datasets) 中的说明设置相应的数据集，然后运行：

```bash
python3 tools/train_net.py --config-file ./configs/Market1501/bagtricks_R50.yml MODEL.DEVICE "cuda:0"
```

这些配置文件是为单 GPU 训练设计的。

如果你想使用 4 个 GPU 训练模型，你可以运行：

```bash
python3 tools/train_net.py --config-file ./configs/Market1501/bagtricks_R50.yml --num-gpus 4
```

如果你想在多台机器上训练模型，你可以运行：

```bash
# 机器 1
export GLOO_SOCKET_IFNAME=eth0
export NCCL_SOCKET_IFNAME=eth0

python3 tools/train_net.py --config-file configs/Market1501/bagtricks_R50.yml \
--num-gpus 4 --num-machines 2 --machine-rank 0 --dist-url tcp://ip:port 

# 机器 2
export GLOO_SOCKET_IFNAME=eth0
export NCCL_SOCKET_IFNAME=eth0

python3 tools/train_net.py --config-file configs/Market1501/bagtricks_R50.yml \
--num-gpus 4 --num-machines 2 --machine-rank 1 --dist-url tcp://ip:port 
```

确保在不同的机器上数据集路径和代码相同，并且机器之间可以相互通信。

要评估模型的性能，可以使用以下命令：

```bash
python3 tools/train_net.py --config-file ./configs/Market1501/bagtricks_R50.yml --eval-only \
MODEL.WEIGHTS /path/to/checkpoint_file MODEL.DEVICE "cuda:0"
```

有关更多选项，请参见 `python3 tools/train_net.py -h`。