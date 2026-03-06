
---
title: keploy
---

### [keploy keploy](https://github.com/keploy/keploy)  ![GitHub Repo stars](https://img.shields.io/github/stars/keploy/keploy?style=social)

Keploy 是一款开发者中心的 API 和集成测试工具，利用 eBPF 技术在网络层捕获流量，无需修改代码即可将真实 API 调用、数据库查询和流事件自动转换为测试用例和数据 Mock。

主要功能特性：
1. **无侵入录制回放**：直接录制真实 API 及集成流程，支持时间冻结以实现确定性重放。
2. **基础设施虚拟化**：虚拟数据库（如 MySQL、MongoDB）、消息队列（如 Kafka）及外部 API 依赖。
3. **AI 增强测试**：基于现有记录分析覆盖缺口，自动生成边界值、异常类型等测试用例。
4. **多维度覆盖分析**：同时提供代码语句/分支覆盖及 API Schema/业务用例覆盖率统计。
5. **CI/CD 与多环境支持**：支持本地、CI 流水线及 Kubernetes 部署，提供统一报告和管理控制台。
6. **全语言协议支持**：通过网络层拦截支持任意语言、框架及协议（HTTP、gRPC 等），无需 SDK。