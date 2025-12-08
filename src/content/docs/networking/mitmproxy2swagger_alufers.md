
---
title: mitmproxy2swagger
---

### [alufers mitmproxy2swagger](https://github.com/alufers/mitmproxy2swagger)

**mitmproxy2swagger** 是一个将 mitmproxy 捕获的 HTTP 流量自动转换为 OpenAPI 3.0 规范的工具，可用于逆向工程 REST API。  

**核心功能**  
- 通过 mitmproxy 捕获流量，生成 OpenAPI 文档；  
- 支持从浏览器 DevTools 导出的 HAR 文件作为输入。  

**使用方法**  
1. **mitmproxy 方式**  
   - 用 mitmproxy 捕获流量并保存为 flow 文件；  
   - 运行工具两次：第一次生成路径模板，第二次生成完整接口描述（可选添加示例数据）；  
   - 需指定 API 基础路径（如 `https://api.example.com/v1`）。  

2. **HAR 文件方式**  
   - 从浏览器 DevTools 导出 HAR 文件，后续处理方式与 mitmproxy flow 文件相同。  

**主要特性**  
- 支持多次运行合并不同流量数据；  
- 可自定义忽略路径或调整参数；  
- 提供示例数据（需注意敏感信息风险）；  
- 支持 Docker 安装与运行。  

**安装**  
通过 pip 安装或 Docker 构建镜像。