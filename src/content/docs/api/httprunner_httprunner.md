
---
title: httprunner
---

### [httprunner httprunner](https://github.com/httprunner/httprunner)

**HttpRunner** 是一个开源测试框架，最初用于 API 接口和性能测试，后扩展为支持 UI 自动化（Android/iOS/Harmony/Browser）、API 测试（HTTP/HTTPS/WebSocket/RPC）、负载测试等的通用智能自动化测试框架。v5 版本引入大模型技术，采用纯视觉驱动（OCR/CV/VLM）方案，追求低性能损耗和跨平台统一 API，支持 Golang 技术栈二进制部署。

**使用方法**  
安装后通过 `hrp` 命令行工具操作，支持运行测试（`hrp run`）、生成 HTML 报告（`hrp report`）、管理设备（`adb`/`ios`）、转换测试用例格式（`convert`）等。测试用例支持 JSON/YAML/GoTest/Pytest 等格式，提供自然语言驱动场景、SDK API（支持 IDE 自动补全）和 CI/CD 友好集成（JSON 日志、HTML 报告）。

**主要特性**  
- 多端统一 API，降低学习成本  
- 基于 Golang，二进制分发，跨平台（macOS/Linux/Windows）  
- 插件系统、分布式测试支持  
- 复用开源生态组件，兼容 HAR、Allure 等工具  
- 支持 API/负载测试（并发执行）及 UI 自动化测试