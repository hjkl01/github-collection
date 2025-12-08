
---
title: keda
---

### [kedacore keda](https://github.com/kedacore/keda)

**核心内容总结：**  
KEDA 是一个基于 Kubernetes 的事件驱动自动扩展工具，支持根据事件负载对工作负载进行细粒度自动扩展（包括缩放至零）。其主要特性包括：  
- 作为 Kubernetes 指标服务器，通过自定义资源定义（Custom Resource）配置自动扩展规则；  
- 与 Kubernetes 原生组件（如 Horizontal Pod Autoscaler）无缝集成，无需外部依赖；  
- 支持云环境和边缘计算场景；  
- 由 CNCF（云原生计算基金会）孵化并毕业。  

**使用方法：**  
- 通过 Helm、Operator Hub 或 YAML 文件部署；  
- 提供多种快速入门示例（如 RabbitMQ、Azure Functions 等）；  
- 文档和社区资源可通过 [keda.sh](https://keda.sh) 获取。  

**其他信息：**  
- 提供贡献指南、测试策略及本地构建部署说明；  
- 社区支持通过 Kubernetes Slack 频道（#KEDA）及定期会议参与；  
- 可通过提交生产环境使用案例加入采用者名单。