
---
title: logdy-core
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/logdyhq/logdy-core?style=social) ](https://github.com/logdyhq/logdy-core)
### [logdyhq logdy-core](https://github.com/logdyhq/logdy-core)

**Logdy 核心内容总结：**

**项目功能：**  
Logdy 是一个轻量级单二进制日志查看工具，支持将终端日志实时展示在 Web 浏览器中，功能类似 `grep`、`awk` 等命令行工具。支持多种输入方式（文件、标准输入、套接字、REST API），提供嵌入式 Web 界面进行日志过滤、解析和分析，完全本地运行保障安全隐私。

**主要特性：**  
- 零依赖单文件二进制，无需安装或编译  
- 实时日志查看、过滤与结构化解析（支持 TypeScript 自定义解析器）  
- 多输入模式（文件、stdin、socket、REST API）  
- 嵌入式 Web UI，支持多列展示、自定义字段  
- 支持作为 Go 语言库集成到应用中  
- 支持日志文件追加、实时转发、多端口监听  

**使用方法：**  
1. **独立工具模式：**  
   ```bash  
   tail -f file.log | logdy  
   logdy follow app-out.log --full-read  
   ```  
   访问 `http://localhost:8080` 查看 Web 界面。

2. **Go 库集成：**  
   ```go  
   logdyLogger := logdy.InitializeLogdy(Config{ServerIp: "127.0.0.1", ServerPort: "8080"}, nil)  
   logdyLogger.LogString("日志信息")  
   ```  

**安装方式：**  
- 脚本安装：`curl https://logdy.dev/install.sh | sh`  
- Homebrew（MacOS）：`brew install logdy`  
- 下载预编译二进制文件（GitHub 发布页）  

**文档与资源：**  
- 官网：[logdy.dev](https://logdy.dev)  
- 文档：[logdy.dev/docs](https://logdy.dev/docs)  
- 演示：[demo.logdy.dev](https://demo.logdy.dev)