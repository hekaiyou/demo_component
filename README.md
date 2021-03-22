# Rainbond Python Demo组件

## 项目介绍

本项目是一个使用 Flask 框架编写的简单的 Python 云原生组件示例，最小的目录结构如下：

```
.
├── app.py
├── Dockerfile
├── requirements.txt
```

由 *app.py*（主程序）、*Dockerfile*（容器配置）和 *requirements.txt*（依赖关系）三个文件组成。

## 本地开发与测试

Python 云原生组件项目 Rainbond 平台上通过 [gunicorn](https://gunicorn.org/) 运行。

而 Gunicorn 是一个 Python WSGI UNIX 的 HTTP 服务器，只支持 Linux 系统，因此如果你使用的不是 Linux 操作系统，你也可以通过其他方式运行，例如：

- 通过 [VirtualEnv](https://virtualenv.pypa.io/en/latest/) 创建一个独立的 Python 运行环境并在里面测试项目。
- 通过 Windows 10 应用商店自带的 Linux 子系统来运行项目。

```
# 开发调试
$ python app.py
# 测试调试
$ pip install -r requirements.txt
$ gunicorn app:app
```

如果准备发布，为了确保组件在 Rainbond 平台上能正确部署，需要在本地测试组件的 Docker 镜像打包过程。

```
$ docker build -t devdocker .
$ docker run devdocker
```

## 存储组件

在云原生的体系中，数据库是一个独立的组件，是原生运行在容器云平台里的一个分布式数据库，真正做到了存储和计算的完全分离。

在 **计算组件** 和 **存储组件** 分离的情况下，**计算组件** 需要通过 **存储组件** 的 *依赖 > 组件连接信息* 中的数据库连接信息来访问 **存储组件**。这个Demo使用的是 MongoDB 数据库，需要 **2** 个标准的 MongoDB 依赖信息：

- MONGODB_HOST: 连接地址
- MONGODB_PORT: 端口

Rainbond 应用商店的 MongoDB 版本过低，为了更好的体验，建议从 [Docker Hub](https://hub.docker.com/_/mongo?tab=tags&page=1&ordering=last_updated) 获取镜像，在 “镜像地址” 栏输入 `mongo`，自动安装最新版本的 MongoDB 数据库组件。

在 MongoDB 组件的 *依赖 > 端口列表* 中找到 `27017` 端口，开放 “对内服务”，修改 “使用别名” 为 `MONGODB`。接下来，就可以在 *依赖 > 组件连接信息* 中看到 `MONGODB_HOST` 和 `MONGODB_PORT` 两个变量。
