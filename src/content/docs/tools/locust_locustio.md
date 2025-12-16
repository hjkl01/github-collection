
---
title: locust
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/locustio/locust?style=social) ](https://github.com/locustio/locust)
### [locustio locust](https://github.com/locustio/locust)

**Locust核心内容总结：**

**项目功能**  
Locust是一款开源的性能/负载测试工具，支持HTTP及其他协议。用户可通过Python代码编写测试场景，支持通过命令行或Web界面启动测试，实时监控吞吐量、响应时间等指标，并可导出数据用于分析。

**使用方法**  
1. 编写Python测试脚本（如定义用户行为、请求逻辑）。  
2. 通过命令行或Web界面启动测试。  
3. 实时查看测试结果，支持动态调整负载参数。

**主要特性**  
1. **Python原生支持**：测试脚本使用普通Python代码编写，支持复杂逻辑（如循环、条件判断），可复用常规库。  
2. **分布式扩展**：基于gevent实现高并发，单机可处理数万虚拟用户，支持跨机器分布式测试。  
3. **Web界面**：提供实时统计图表，支持运行中调整负载参数。  
4. **高度可扩展**：通过插件机制支持自定义协议、实时数据导出（如Grafana集成）、自定义负载策略等。  
5. **通用性**：不仅限于Web服务，可通过自定义客户端测试任意系统或协议。  

**适用场景**  
适合需要高并发测试、需灵活编写测试逻辑、需实时监控及分析结果的性能测试需求。