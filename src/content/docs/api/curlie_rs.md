
---
title: curlie
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/rs/curlie?style=social) ](https://github.com/rs/curlie)
### [rs curlie](https://github.com/rs/curlie)

**项目功能**  
Curlie 是一个基于 `curl` 的增强工具，结合了 `HTTPie` 的易用性和 `curl` 的强大功能，提供更友好的交互界面与完整的功能支持。  

**使用方法**  
支持多种安装方式（如 Homebrew、Go、包管理器等）。基本用法为：  
`curlie [CURL选项...] [方法] URL [参数...]`  
支持自定义请求方法、请求头、JSON 数据，交互模式下默认美化输出 JSON，使用 `--pretty` 可强制启用美化输出。  

**主要特性**  
- 保留 `curl` 的全部功能，但通过语法糖简化操作；  
- 输出不缓冲，实时格式化，便于调试流数据；  
- 头部信息输出至 `stderr`（与 `HTTPie` 不同）；  
- 支持通过 `--curl` 选项打印实际执行的 `curl` 命令；  
- 默认支持 JSON 美化输出。  

**许可证**  
采用 MIT 开源协议。