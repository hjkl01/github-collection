
---
title: hypertrace
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hypertrace/hypertrace?style=social) ](https://github.com/hypertrace/hypertrace)
### [hypertrace hypertrace](https://github.com/hypertrace/hypertrace)

**项目核心内容总结：**  
Hypertrace 是一个云原生的分布式追踪与可观测性平台，用于监控分布式系统的性能和故障。其主要功能包括：  
- **根因分析（RCA）**：快速定位系统故障原因；  
- **性能瓶颈分析**：识别慢操作（如API调用、数据库查询）；  
- **微服务依赖监控**：观察服务间调用关系及风险；  
- **版本对比**：监控新版本发布后的性能变化。  

**使用方法：**  
1. **快速启动**：通过 Docker Compose 部署，支持本地测试环境；  
2. **生产部署**：提供 Kubernetes Helm Charts，适用于云环境或私有集群；  
3. **兼容性**：支持已接入 Zipkin/Jaeger 的应用，或通过示例应用生成测试数据。  

**主要特性：**  
- 修复了 Log4j 安全漏洞（升级至 2.17 版本）；  
- 提供社区支持、月度技术会议及 Slack 讨论群；  
- 开源核心功能基于 Apache 2.0 许可，部分高级功能需社区许可。