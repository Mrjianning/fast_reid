# 使用容器

```shell
cd docker/
# 构建镜像：
docker build -t=fastreid:v0 .
# 启动容器（需要 GPU 支持）
nvidia-docker run -v server_path:docker_path --name=fastreid --net=host --ipc=host -it fastreid:v0 /bin/sh
```

## 安装新依赖项

要使更改永久生效，请将以下内容添加到 `Dockerfile` 中：
```shell
RUN sudo apt-get update && sudo apt-get install -y vim
```

或者可以在容器内运行这些命令以临时安装新依赖项。

## 更完整的 Docker 容器

如果你希望使用包含更多有用工具的完整 Docker 容器，你可以查看我的开发环境 [Dockerfile](https://github.com/L1aoXingyu/fastreid_docker)。