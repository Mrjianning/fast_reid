# FastReID 演示

我们提供了一个命令行工具，用于运行内置模型的简单演示。

你可以运行以下命令来获取不同图像之间的余弦相似度：

```bash
python demo/visualize_result.py --config-file logs/dukemtmc/mgn_R50-ibn/config.yaml \
--parallel --vis-label --dataset-name DukeMTMC --output logs/mgn_duke_vis \
--opts MODEL.WEIGHTS logs/dukemtmc/mgn_R50-ibn/model_final.pth
```

### 参数说明：

- **`--config-file`**：指定模型的配置文件路径，在这个例子中是 `logs/dukemtmc/mgn_R50-ibn/config.yaml`。
- **`--parallel`**：启用并行处理以加快特征提取速度。
- **`--vis-label`**：可视化查询图像的标签信息。
- **`--dataset-name`**：指定使用的数据集名称，这里是 `DukeMTMC`。
- **`--output`**：指定结果保存的路径，输出文件将保存到 `logs/mgn_duke_vis` 目录中。
- **`--opts`**：附加选项，用于指定模型权重文件路径。在这个例子中，权重文件位于 `logs/dukemtmc/mgn_R50-ibn/model_final.pth`。

通过执行这个命令，FastReID 将会计算不同图像之间的余弦相似度，并将结果保存到指定的输出路径中。