
---
title: OpenBB
---

### [OpenBB-finance OpenBB](https://github.com/OpenBB-finance/OpenBB)  ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBB-finance/OpenBB?style=social)

**项目核心内容总结：**  
Open Data Platform by OpenBB（ODP）是一个开源工具集，用于整合专有、授权和公开数据源，供AI助手、研究仪表板等下游应用使用。其核心特性是“连接一次，到处使用”的架构，支持通过Python环境、Excel、AI代理和REST API等多种方式访问数据。  

**功能与使用方法：**  
1. **数据整合**：支持多数据源接入，提供统一的数据接口。  
2. **Python集成**：通过`pip install openbb`安装后，可直接调用API（如示例代码`obb.equity.price.historical("AAPL")`获取股票历史价格）。  
3. **本地API服务**：安装`openbb[all]`后运行`openbb-api`命令，启动本地FastAPI服务（地址`127.0.0.1:6900`），供其他应用调用。  
4. **与OpenBB Workspace集成**：通过填写服务地址（`http://127.0.0.1:6900`）完成后台连接，实现数据与AI代理的可视化交互。  

**主要特性：**  
- 跨平台数据分发（Python、Excel、AI代理、REST API）。  
- 提供CLI命令行工具，支持快速安装与操作。  
- 开源架构，兼容企业级应用与AI集成。