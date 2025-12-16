
---
title: oha
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hatoo/oha?style=social) ](https://github.com/hatoo/oha)
### [hatoo oha](https://github.com/hatoo/oha)

**oha 核心内容总结**

**项目功能**  
oha 是一个基于 Rust 的 HTTP 负载生成工具，灵感来自 [rakyll/hey](https://github.com/rakyll/hey)，支持实时 TUI 界面，用于向 Web 应用发送负载并监控性能。

**主要特性**  
- **实时 TUI 监控**：显示请求速率、延迟、成功/失败统计等实时数据。  
- **灵活的负载控制**：支持通过 `-n`（请求数）、`-c`（并发连接数）、`-q`（QPS）等参数控制负载，可结合 `--burst-delay` 和 `--burst-rate` 实现突发流量模拟。  
- **多协议支持**：支持 HTTP/1.1、HTTP/2、HTTP/3（实验性），可禁用 Keep-Alive 以模拟真实用户行为。  
- **动态 URL 生成**：通过 `--rand-regex-url` 自动生成随机 URL，用于更真实的负载测试。  
- **多输出格式**：支持文本、JSON、CSV 格式输出，可记录成功请求至 SQLite 数据库。  
- **性能优化**：禁用 TUI 时采用更高效的实现，提升吞吐量。  

**使用方法**  
1. **安装**：通过 `cargo install oha` 或下载预编译二进制文件，支持 Arch Linux（`pacman`）、Homebrew（`brew`）、Windows（`winget`）等平台。  
2. **基本命令**：  
   ```bash  
   oha -c 100 -q 1000 http://example.com  
   ```  
   - `-c`：并发连接数  
   - `-q`：每秒查询数（QPS）  
   - `--latency-correction`：修正延迟统计（避免“协调遗漏问题”）  
   - `--disable-keepalive`：禁用 TCP 连接复用（模拟真实用户场景）  
3. **高级功能**：  
   - 从文件读取 URL：`--urls-from-file urls.txt`  
   - 动态 URL：`--rand-regex-url http://127.0.0.1/[a-z][a-z][0-9]`  
   - 输出 JSON：`--output-format json`  

**适用场景**  
- Web 服务器压力测试  
- 性能基准测试  
- 模拟真实用户访问模式（如突发流量、多页面请求）