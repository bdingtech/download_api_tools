# X（Twitter）&YouTube直链解析

## 项目介绍
基于[totonyus/ydl_api_ng](https://hub.docker.com/r/totonyus/ydl_api_ng)的镜像，增加了X（Twitter）&YouTube直链解析功能。

## 使用方法

### 端口
api的内部端口是3000

### Docker-compose
只需将docker-compose.yml文件复制到您想要的位置，然后启动此命令：

> docker-compose pull # 拉取最新的镜像
> 
> docker-compose up # 启动容器

> docker-compose down # 停止容器

### 示例
> http://127.0.0.1:3000/video_info?url=https://www.youtube.com/watch?v=m4KJNjhUQ5c&ab_channel=%E5%8D%81%E4%B8%89%E9%82%80