
---
title: ComfyUI-Manager
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI-Manager?style=social) ](https://github.com/Comfy-Org/ComfyUI-Manager)
### [Comfy-Org ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager)

**核心内容总结：**

ComfyUI-Manager 是一个用于管理 ComfyUI 自定义节点的工具，支持安装、更新、卸载节点及依赖项，提供多种网络模式（公共、私有、离线）和安全策略配置。主要功能包括：

1. **节点管理**  
   - 支持通过 Git、pip 或预设通道安装节点，提供缓存机制优化下载。  
   - 自动检测缺失节点并推荐安装，支持修复旧工作流中的节点错误。  

2. **配置与自定义**  
   - 通过 `config.ini` 文件设置 Git 路径、SSL 绕过、日志记录、安全级别（强/正常/弱）等。  
   - 支持自定义 pip 安装映射、黑名单（防止降级或安装特定包）及自动恢复依赖版本。  

3. **网络与安全**  
   - 支持私有网络或离线环境，通过 `channel_url` 配置私有节点数据库。  
   - 安全策略限制高风险操作（如 Git 安装、pip 安装），根据级别（强/正常/弱）控制功能可用性。  

4. **便捷操作**  
   - 双击节点标题可复制连接或自动匹配输入输出，提升工作流编辑效率。  
   - 支持通过环境变量（如 GITHUB_ENDPOINT）配置代理，适配受限网络环境。  

**使用方法**：  
- 安装后通过 `config.ini` 配置基础参数，启动 ComfyUI 后使用管理界面安装/更新节点。  
- 高级用户可通过 `scan.sh` 脚本更新节点映射和 GitHub 统计数据，需设置 GitHub Token 避免 API 限速。  

**主要特性**：  
- 支持多平台（Windows、Linux），兼容不同网络环境。  
- 提供日志记录、节点自动修复、自定义快捷操作（如双击节点复制连接）。  
- 通过安全级别控制功能风险，保障使用安全。