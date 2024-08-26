# 模型部署

此目录包含以下内容：

1. 将 fastreid 模型转换为 Caffe/ONNX/TRT 格式的脚本。

2. 加载 Caffe/ONNX/TRT 中的 R50 基线模型并运行推理的示例。

## 教程

### Caffe 转换

<details>
<summary>逐步操作步骤：Caffe 模型转换</summary>

这是一个将 `meta_arch` 中的 fastreid 基线模型转换为 Caffe 模型的简单示例，如果你想转换更复杂的架构，则需要进行更多的自定义。

1. 运行 `caffe_export.py` 获取转换后的 Caffe 模型，

    ```bash
    python tools/deploy/caffe_export.py --config-file configs/market1501/bagtricks_R50/config.yml --name baseline_R50 --output caffe_R50_model --opts MODEL.WEIGHTS logs/market1501/bagtricks_R50/model_final.pth
    ```

    然后你可以在 `./caffe_R50_model` 中检查 Caffe 模型和 prototxt 文件。

2. 按以下三步修改 `prototxt`：

   1) 修改 `baseline_R50.prototxt` 中的 `MaxPooling` 并删除 `ceil_mode: false`。

   2) 在 `baseline_R50.prototxt` 中添加 `avg_pooling`：

        ```prototxt
        layer {
            name: "avgpool1"
            type: "Pooling"
            bottom: "relu_blob49"
            top: "avgpool_blob1"
            pooling_param {
                pool: AVE
                global_pooling: true
            }
        }
        ```

   3) 将最后一层的 `top` 名称更改为 `output`：

        ```prototxt
        layer {
            name: "bn_scale54"
            type: "Scale"
            bottom: "batch_norm_blob54"
            top: "output" # bn_norm_blob54
            scale_param {
                bias_term: true
            }
        }
        ```

3. （可选）你可以打开 [Netscope](https://ethereon.github.io/netscope/quickstart.html)，然后输入你的网络 `prototxt` 文件以可视化网络结构。

4. 运行 `caffe_inference.py`，使用输入图像保存 Caffe 模型特征

   ```bash
    python caffe_inference.py --model-def outputs/caffe_model/baseline_R50.prototxt \
    --model-weights outputs/caffe_model/baseline_R50.caffemodel \
    --input test_data/*.jpg --output caffe_output
   ```

6. 运行 `demo/demo.py`，使用相同的输入图像获取 fastreid 模型特征，然后验证 Caffe 和 PyTorch 是否计算出相同的网络值。

    ```python
    np.testing.assert_allclose(torch_out, ort_out, rtol=1e-3, atol=1e-6)
    ```

</details>

### ONNX 转换

<details>
<summary>逐步操作步骤：ONNX 模型转换</summary>

这是一个将 `meta_arch` 中的 fastreid 基线模型转换为 ONNX 模型的简单示例。据我所知，ONNX 支持 PyTorch 中的大多数操作符，如果某些操作符不受 ONNX 支持，则需要对这些操作符进行自定义。

1. 运行 `onnx_export.py` 获取转换后的 ONNX 模型，

    ```bash
    python onnx_export.py --config-file root-path/bagtricks_R50/config.yml --name baseline_R50 --output outputs/onnx_model --opts MODEL.WEIGHTS root-path/logs/market1501/bagtricks_R50/model_final.pth
    ```

    然后你可以在 `outputs/onnx_model` 中检查 ONNX 模型。

2. （可选）你可以使用 [Netron](https://github.com/lutzroeder/netron) 来可视化网络结构。

3. 运行 `onnx_inference.py`，使用输入图像保存 ONNX 模型特征

   ```bash
    python onnx_inference.py --model-path outputs/onnx_model/baseline_R50.onnx \
    --input test_data/*.jpg --output onnx_output
   ```

4. 运行 `demo/demo.py`，使用相同的输入图像获取 fastreid 模型特征，然后验证 ONNX Runtime 和 PyTorch 是否计算出相同的网络值。

    ```python
    np.testing.assert_allclose("pth_output", "onnx_output", rtol=1e-3, atol=1e-6)
    ```

</details>

### TensorRT 转换

<details>
<summary>逐步操作步骤：TRT 模型转换</summary>

这是一个将 `meta_arch` 中的 fastreid 基线模型转换为 TRT 模型的简单示例。

首先，你需要按照 [ONNX 转换](https://github.com/JDAI-CV/fast-reid#fastreid) 的步骤，将 PyTorch 模型转换为 ONNX 格式，并记住你的 `output` 名称。然后，你可以按照下面的指示将 ONNX 模型转换为 TensorRT。

1. 运行以下命令行，从 ONNX 模型中获取转换后的 TRT 模型，

    ```bash
    python trt_export.py --name baseline_R50 --output outputs/trt_model \
    --mode fp32 --batch-size 8 --height 256 --width 128 \
    --onnx-model outputs/onnx_model/baseline.onnx 
    ```

    然后你可以在 `outputs/trt_model` 中检查 TRT 模型。

2. 运行 `trt_inference.py`，使用输入图像保存 TRT 模型特征

   ```bash
    python3 trt_inference.py --model-path outputs/trt_model/baseline.engine \
    --input test_data/*.jpg --batch-size 8 --height 256 --width 128 --output trt_output 
   ```

3. 运行 `demo/demo.py`，使用相同的输入图像获取 fastreid 模型特征，然后验证 TensorRT 和 PyTorch 是否计算出相同的网络值。

    ```python
    np.testing.assert_allclose(torch_out, trt_out, rtol=1e-3, atol=1e-6)
    ```

注意：目前 TensorRT 运行时不支持 int8 模式，校准器存在一些问题，需要帮助解决！

</details>

## 致谢

感谢 JDAI 模型加速团队中的 [CPFLAME](https://github.com/CPFLAME)，[gcong18](https://github.com/gcong18)，[YuxiangJohn](https://github.com/YuxiangJohn) 和 [wiggin66](https://github.com/wiggin66) 在 PyTorch 模型转换过程中的帮助。