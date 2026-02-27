
---
title: chrome-devtools-mcp
---

### [ChromeDevTools chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)  ![GitHub Repo stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social)

**核心内容总结：**  
该项目是一个用于连接和调试Chrome浏览器的工具（`chrome-devtools-mcp`），支持通过MCP客户端（如Gemini、Qwen等）与Chrome实例交互，实现性能分析、网络监控等功能。  

**功能与使用方法：**  
1. **连接方式**：支持自动连接（Chrome 144+）和手动连接（通过`--browser-url`指定远程调试端口）。  
2. **配置管理**：通过JSON文件定义MCP服务器配置，例如：  
   ```json  
   {  
     "mcpServers": {  
       "chrome-devtools": {  
         "command": "npx",  
         "args": ["chrome-devtools-mcp@latest", "--channel=canary", "--headless=true"]  
       }  
     }  
   }  
   ```  
3. **高级特性**：支持WebSocket连接（可添加自定义认证头）、隔离用户数据目录（`--isolated=true`）、禁用特定功能模块（如`--categoryPerformance=false`）。  

**主要特性：**  
- 支持Chrome多版本（如`--channel=canary`）。  
- 可在沙盒环境中运行，通过`--browser-url`连接外部Chrome实例。  
- 提供用户数据目录管理，避免数据冲突。  

**注意事项：**  
- 手动连接时需启用Chrome远程调试端口（如`--remote-debugging-port=9222`），并指定非默认用户数据目录。  
- 沙盒环境可能限制Chrome启动权限，需通过`--browser-url`绕过或关闭沙盒。