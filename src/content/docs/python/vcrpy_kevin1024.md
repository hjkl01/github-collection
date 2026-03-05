
---
title: vcrpy
---

### [kevin1024 vcrpy](https://github.com/kevin1024/vcrpy)  ![GitHub Repo stars](https://img.shields.io/github/stars/kevin1024/vcrpy?style=social)

VCR.py 是 Ruby VCR 库的 Python 实现，用于简化并加速涉及 HTTP 请求的测试。首次运行时，它记录所有 HTTP 交互并保存为 cassette 文件；后续运行时，它会读取文件拦截请求并返回记录响应，无需实际产生 HTTP 流量。该工具支持离线测试，确保测试结果确定性强，并显著提升执行速度。若服务端 API 变更，只需删除 cassette 文件重新运行测试即可更新记录。此外，项目支持通过 pytest-recording 与 Pytest 集成。