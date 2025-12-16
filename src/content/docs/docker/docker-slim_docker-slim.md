
---
title: docker-slim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/docker-slim/docker-slim?style=social) ](https://github.com/docker-slim/docker-slim)
### [docker-slim docker-slim](https://github.com/docker-slim/docker-slim)

**项目核心内容总结：**

**功能：**  
DockerSlim 是一个用于优化 Docker 容器镜像的工具，通过动态分析容器运行时行为，构建应用依赖图谱，生成体积更小的镜像，并自动生成安全配置（如 Seccomp、AppArmor 策略）。

**使用方法：**  
1. **安装方式**：支持通过 Docker 容器构建（无需本地安装 Go）或本地编译（需 Go 1.21+）。  
2. **基本命令**：使用 `slim build` 指令分析镜像，通过参数（如 `--include-path`、`--path-perms`）处理用户权限、文件权限问题。  
3. **常见问题处理**：如 Nginx 因临时目录缺失报错，需通过 `--include-path` 添加路径并设置权限。

**主要特性：**  
- 支持非默认用户场景，保留文件权限（`--keep-perms`）或自定义权限（`--path-perms`）。  
- 动态分析选项：可替换容器入口点收集数据，或使用内核级工具（如 runC）无侵入式分析。  
- 自动生安全策略，提升容器运行安全性。  
- 兼容复杂场景（如多用户、权限控制），但需依赖 Linux 内核特性（如命名空间）。