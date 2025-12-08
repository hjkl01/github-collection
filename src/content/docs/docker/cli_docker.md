
---
title: cli
---

### [docker cli](https://github.com/docker/cli)

**核心内容总结：**

该项目是Docker命令行工具（CLI）的源代码仓库，提供Docker客户端的开发和构建功能。主要功能包括：  
- **构建方式**：支持通过`docker buildx bake`命令编译CLI，可构建多平台二进制文件（如`cross`目标）或指定平台（如`linux/arm64`），还支持动态二进制构建（通过`USE_GLIBC`环境变量）。  
- **开发与测试**：提供交互式容器开发环境（`make shell`）、代码检查（`lint shellcheck`）和测试运行（`test`目标）。  
- **特性**：基于Docker开发，支持跨平台编译，集成多种测试和代码质量工具。  
- **法律与许可**：遵循Apache 2.0许可证，使用和传输需遵守美国等政府的限制规定，具体见项目中的`NOTICE`文件。