
---
title: buildozer
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kivy/buildozer?style=social) ](https://github.com/kivy/buildozer)
### [kivy buildozer](https://github.com/kivy/buildozer)

**核心内容总结：**  
Buildozer 是一个将 Python 应用打包为多平台二进制安装包的工具，支持 Android、iOS、Windows、macOS 和 Linux。开发者通过配置 `buildozer.spec` 文件定义应用信息和依赖，Buildozer 自动处理构建流程。  

**主要功能与特性：**  
1. **跨平台支持**：一键生成对应平台的安装包（如 Android APK、iOS IPA 等）。  
2. **依赖管理**：自动下载并准备构建所需依赖（如 Android SDK/NDK）。  
3. **Docker 集成**：提供 Docker 镜像简化环境配置，支持缓存加速构建。  
4. **CI/CD 支持**：通过 GitHub Action 实现自动化构建。  
5. **配置灵活**：支持通过环境变量覆盖 `buildozer.spec` 中的配置项。  

**使用方法：**  
- 安装：推荐通过官方文档安装，或使用 Docker 镜像（如 `docker run kivy/buildozer`）。  
- 初始化：运行 `buildozer init` 生成 `buildozer.spec` 文件。  
- 构建命令示例：`buildozer android debug`（调试模式构建 Android 应用）。  
- 支持命令包括 `clean`、`update`、`deploy`、`run` 等，可组合使用（如 `debug deploy run`）。