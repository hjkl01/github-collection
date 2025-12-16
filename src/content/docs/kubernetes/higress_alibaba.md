
---
title: higress
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/higress?style=social) ](https://github.com/alibaba/higress)
### [alibaba higress](https://github.com/alibaba/higress)

**Higress 核心内容总结**  

**项目功能**  
Higress 是基于 Istio 和 Envoy 的云原生 API 网关，支持通过 Wasm 插件（Go/Rust/JS 编写）扩展功能，提供 AI、流量管理、安全防护等通用插件及开箱即用的控制台。核心能力包括：  
- **AI 网关**：统一连接所有大语言模型（LLM）提供商，支持多模型负载均衡、令牌限流、缓存及可观测性。  
- **MCP 服务器托管**：允许 AI 代理调用工具和服务，支持与主流模型提供商对接。  
- **Kubernetes 入口控制器**：兼容 K8s nginx 入口注解，支持 Gateway API 标准。  
- **微服务网关**：支持从 Nacos、ZooKeeper 等服务注册中心发现微服务，深度集成 Dubbo、Sentinel 等技术栈。  
- **安全网关**：支持 WAF、JWT、OAuth 等认证策略及 CC 防护。  

**使用方法**  
- **快速部署**：通过单条 Docker 命令启动，支持 K8s 部署及企业版安装。  
- **插件扩展**：使用官方插件库或自定义 Wasm 插件实现功能扩展，支持热更新。  

**主要特性**  
1. **生产级稳定性**：经阿里内部 2 年验证，支持百万级 QPS，配置变更毫秒级生效，无流量抖动。  
2. **流式处理**：支持请求/响应体全流式处理，降低高带宽场景（如 AI 业务）的内存开销。  
3. **扩展灵活**：90% 场景通过官方插件满足，Wasm 插件实现内存安全、多语言支持及独立升级。  
4. **安全易用**：内置 WAF、自动证书管理（Let's Encrypt），支持非 K8s 环境部署，提供图形化控制台。