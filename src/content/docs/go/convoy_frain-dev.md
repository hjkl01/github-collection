
---
title: convoy
---

### [frain-dev convoy](https://github.com/frain-dev/convoy)

**项目核心内容总结：**  
Convoy 是一个开源的高性能 Webhook 网关，用于安全地接收、存储、调试、传递和管理数百万事件，支持重试、限速、静态 IP、熔断等特性。  

**主要功能：**  
- 作为 Webhook 网关，隔离内部系统与公网，实现事件的内外传输；  
- 水平扩展架构，包含 API 服务器、工作节点、调度器等独立组件；  
- 安全特性：负载签名、Bearer Token 认证、静态 IP 限制；  
- 支持事件多端点路由（扇出）、自定义速率限制规则；  
- 提供重试机制（固定时间/指数退避）及批量重试功能；  
- 客户端仪表盘（支持 iframe 嵌入），可调试事件、配置端点；  
- 端点故障时自动禁用并触发邮件/Slack 通知。  

**使用方法：**  
- 安装方式支持 Docker 或 Kubernetes（Helm 模板）；  
- 参考文档链接：[https://docs.getconvoy.io](https://docs.getconvoy.io)。  

**许可证：**  
遵循 [Elastic License v2.0](https://github.com/frain-dev/convoy/blob/main/LICENSE)。