
---
title: lighter-python
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/elliottech/lighter-python?style=social) ](https://github.com/elliottech/lighter-python)
### [elliottech lighter-python](https://github.com/elliottech/lighter-python)

**核心内容总结：**  
Lighter Python 是一个用于与 Lighter 平台交互的 Python SDK，提供账户管理、订单操作、交易查询、市场数据获取等功能。  

**使用方法：**  
1. 安装：通过 `pip install git+https://github.com/elliottech/lighter-python.git` 安装。  
2. 调用：导入 `lighter` 模块，使用异步方式创建 `ApiClient` 并调用相关 API（如 `AccountApi` 获取账户信息）。  
3. 示例：包含获取信息、同步订单簿、创建/取消订单等脚本（如 `examples/get_info.py`）。  

**主要特性：**  
- **API 覆盖全面**：涵盖账户、区块、订单簿、交易、蜡烛图数据等模块，支持 GET/POST 请求。  
- **模型定义清晰**：提供丰富的数据模型（如 `Account`、`OrderBook`、`Tx` 等）描述 API 返回的数据结构。  
- **异步支持**：通过 `asyncio` 实现异步调用，确保连接正确关闭。  
- **无需授权**：所有 API 端点无需鉴权，直接调用即可。