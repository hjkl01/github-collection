
---
title: ezbookkeeping
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mayswind/ezbookkeeping?style=social) ](https://github.com/mayswind/ezbookkeeping)
### [mayswind ezbookkeeping](https://github.com/mayswind/ezbookkeeping)

**项目核心内容总结：**

**项目功能**  
ezBookkeeping 是一款开源、自托管的个人财务管理应用，提供移动端和桌面端适配界面，支持 PWA（渐进式网页应用）实现类似原生应用的体验。具备双级账户分类、收支记录、图像附件、地理位置标记、重复交易、多语言/多货币支持、自动汇率转换、AI 收据识别等功能，支持 CSV、OFX、QIF 等多种数据格式的导入导出。

**使用方法**  
1. **Docker 安装**：通过单条命令部署，支持最新版本或每日构建版本。  
   示例：`docker run -p8080:8080 mayswind/ezbookkeeping`  
2. **二进制文件安装**：下载发布版本后，通过命令行启动（Linux/macOS：`./ezbookkeeping server run`；Windows：`.\ezbookkeeping.exe server run`）。  
3. **源码构建**：需安装 Go、Node.js 等工具，通过 `build.sh` 或 `build.bat` 脚本编译生成安装包或 Docker 镜像。

**主要特性**  
- 轻量高效：适配低资源设备（如树莓派）及高并发环境。  
- 安全性：支持 2FA、登录限制、应用锁（PIN/WebAuthn）。  
- 跨平台兼容：支持 Windows、macOS、Linux 及 x86/ARM 架构。  
- 扩展性：支持 SQLite、MySQL、PostgreSQL 数据库。  
- 本地化：支持 13 种语言、多时区、自定义日期/货币格式。  
- AI 集成：通过 MCP 协议支持 AI 功能扩展（如收据图像识别）。