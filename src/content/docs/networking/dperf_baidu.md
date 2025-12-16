
---
title: dperf
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/baidu/dperf?style=social) ](https://github.com/baidu/dperf)
### [baidu dperf](https://github.com/baidu/dperf)

**dperf** 是一个基于 DPDK 的高性能网络流量生成和负载测试工具，主要用于模拟大规模网络流量以测试系统性能。其核心功能包括：  
- **高性能流量生成**：支持每秒生成数千万 HTTP 连接、数百 Gbps 传输速率及数十亿并发连接，适用于负载均衡器、网关等设备的稳定性测试。  
- **详细统计与监控**：实时输出流量数据（如 CPS、TPS、丢包率、HTTP 状态码等），支持故障排查。  
- **多场景应用**：可作为 HTTP 服务器/客户端、网络设备性能基准测试工具，或用于评估网卡与 CPU 的包处理能力。  

**主要特性**：  
- 基于 DPDK 实现，充分利用硬件资源提升性能；  
- 支持多种网络协议（HTTP、TCP 等）及复杂测试场景；  
- 提供全面的性能指标和错误日志，便于分析系统瓶颈。  

**适用场景**：云服务器网络性能测试、负载均衡器压力测试、网络设备（如 NIC、CPU）处理能力评估等。  

**使用方法**：需参考官方文档（[https://dperf.org/](https://dperf.org/)）配置测试参数并运行，具体命令及操作流程需结合实际需求调整。