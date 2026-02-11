
---
title: subfinder
---

### [projectdiscovery subfinder](https://github.com/projectdiscovery/subfinder)  ![GitHub Repo stars](https://img.shields.io/github/stars/projectdiscovery/subfinder?style=social)

**项目核心内容总结：**

Subfinder 是一个**快速的被动式子域名枚举工具**，用于通过被动在线资源获取目标网站的有效子域名。它具有简单、模块化架构，专为速度和轻量资源使用优化，适用于渗透测试和漏洞赏金猎人。

### 主要功能：
- 支持多种输出格式（JSON、文件、终端输出）
- 使用**经过筛选的被动式数据源**以提高结果质量
- 支持通过 STDIN/STDOUT 轻松集成到工作流中
- 提供强大的解析和通配符消除模块
- 支持递归子域名发现
- 支持配置 API 密钥、自定义解析器、代理等

### 使用方法：
1. 安装（需要 Go 1.24）：
   ```sh
   go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
   ```

2. 运行示例：
   ```sh
   subfinder -d example.com
   ```

3. 支持的常用参数：
   - `-d`：指定目标域名
   - `-dL`：从文件读取多个域名
   - `-s`：指定使用的数据源
   - `-all`：使用所有数据源（较慢）
   - `-o`：指定输出文件
   - `-json`：输出为 JSON 格式
   - `-ls`：列出所有可用数据源

4. 支持环境变量配置路径。

### 主要特性：
- 快速、轻量、高效
- 支持递归子域名查找
- 可作为 Go 库使用
- 支持多种过滤与匹配规则
- 可配置 API 密钥、代理、解析器等

### 注意事项：
- 部分数据源需要配置 API 密钥
- 支持多线程并发解析（默认 10 个）

Subfinder 由 [projectdiscovery](https://projectdiscovery.io) 团队开发，遵循开源协议，提供详细文档和社区支持。