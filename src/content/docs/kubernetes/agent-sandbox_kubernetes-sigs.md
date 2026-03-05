
---
title: agent-sandbox
---

### [kubernetes-sigs agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/agent-sandbox?style=social)

Agent Sandbox 是为 Kubernetes 提供的声明式 API 和控制器，用于管理孤立、有状态、单例的工作负载（如 AI 代理运行时、开发环境）。核心功能包括：为 Pod 提供稳定的网络身份和持久化存储；管理生命周期（创建、暂停、恢复）；通过扩展模块实现模板复用、按需创建及预热池。该项目旨在提供一种类似轻量级 VM 的体验，解决单实例服务管理复杂性问题，支持强隔离、深度休眠及编程式交互。