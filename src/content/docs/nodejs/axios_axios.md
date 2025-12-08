
---
title: axios
---

### [axios axios](https://github.com/axios/axios)

**axios核心内容总结：**

axios是一个基于Promise的HTTP客户端，支持浏览器和Node.js环境，用于发送HTTP请求。主要功能包括：

1. **功能特性**  
   - 支持多种适配器（如XMLHttpRequest、fetch、HTTP/2），兼容不同环境。  
   - 提供请求/响应拦截器、自动JSON序列化与反序列化、进度跟踪（上传/下载）。  
   - 支持自定义配置（如超时、响应类型、HTTP版本）。  
   - 内置对FormData、流式响应等处理能力。

2. **使用方法**  
   - 安装：`npm install axios`。  
   - 基本用法：通过`axios.get()`/`axios.post()`等方法发送请求，支持配置对象传参。  
   - 可创建自定义实例，配置默认参数（如适配器、基础URL）。  
   - 支持TypeScript类型定义及错误类型判断（如`axios.isAxiosError`）。

3. **主要优势**  
   - 兼容性强：适配Fetch API、Tauri等框架，支持自定义fetch函数。  
   - 扩展灵活：支持HTTP/2、流式响应、进度事件等高级功能。  
   - 生态完善：遵循Semver版本管理，提供详细的文档、示例及社区资源。

**适用场景**：适用于前后端数据交互、API调用、文件上传等需要HTTP通信的场景。