
---
title: pex
---

### [pex-tool pex](https://github.com/pex-tool/pex)

**PEX核心内容总结**  
PEX是一个用于生成可执行Python环境（.pex文件）的工具，支持跨平台部署，简化Python应用的分发。  

**功能与特性**  
- 生成包含依赖的可执行文件，支持Linux和OS X跨平台运行。  
- 通过`pex`命令快速构建虚拟环境或独立可执行文件（如`pex flask -- webserver.py`）。  
- 支持从`requirements.txt`冻结依赖并生成PEX文件，便于部署。  
- 可指定Python解释器（如PyPy）或入口点生成独立二进制文件。  
- 与构建工具（如Pants、Buck）集成，支持自动化构建流程。  

**使用方法**  
1. 安装：`pip install pex` 或通过`uv`构建源码。  
2. 示例：  
   - 创建环境：`pex requests flask -o myenv.pex`  
   - 运行脚本：`pex flask -- webserver.py`  
   - 生成独立可执行文件：`pex "pex>=2.1.35" --console-script pex-tools -o tool.pex`  

**其他**  
- 开发依赖`uv`和`dev-cmd`，支持类型检查、测试等流程。  
- 采用Apache2许可证。