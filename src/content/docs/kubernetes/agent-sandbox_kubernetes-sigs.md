
---
title: agent-sandbox
---

### [kubernetes-sigs agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/agent-sandbox?style=social)

Agent Sandbox 是一个基于 Kubernetes 的项目，通过自定义资源定义（CRD）和控制器管理隔离的、有状态的单例工作负载。核心 `Sandbox` 资源提供声明式 API，具备稳定身份、持久化存储及生命周期管理（创建、暂停、恢复）。项目包含扩展模块以支持模板复用、按需创建及预热池。适用于 AI 代理运行时、开发环境及单实例服务，特性涵盖强隔离安全、深度休眠、自动恢复及高效存储管理。