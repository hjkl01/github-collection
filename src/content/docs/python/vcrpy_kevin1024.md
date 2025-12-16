
---
title: vcrpy
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kevin1024/vcrpy?style=social) ](https://github.com/kevin1024/vcrpy)
### [kevin1024 vcrpy](https://github.com/kevin1024/vcrpy)

VCR.py 是一个 Python 库，用于录制和重放 HTTP 请求与响应，从而简化和加速涉及网络请求的测试。其核心功能是通过拦截 HTTP 交互，首次运行时将请求和响应保存为 YAML 格式的“磁带文件”（cassette），后续运行时直接读取该文件模拟网络响应，无需实际发送请求。主要特性包括：支持离线测试、保证测试结果的确定性、提升测试执行速度。当被测服务的 API 发生变更时，只需删除原有磁带文件并重新运行测试即可更新录制内容。使用时可结合 Pytest，通过第三方库 pytest-recording 提供的 fixture 实现集成。