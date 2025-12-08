
---
title: hftbacktest
---

### [nkaz001 hftbacktest](https://github.com/nkaz001/hftbacktest)

HftBacktest 是一个高频交易回测工具，支持多资产、多交易所的策略模拟和实时交易部署。其核心功能包括：基于订单簿（Level-3 数据）的深度重建、订单延迟模拟、市场做市策略回测（如 GLFT 模型）、多市场同时交易，以及通过 Rust 实现的实时交易机器人。主要特性包括：  
1. 使用 Numba 的 JIT 加速技术实现高效回测；  
2. 支持 Tick-by-Tick 级别的精细模拟；  
3. 提供订单延迟数据集成与分析；  
4. 可扩展自定义数据源；  
5. 兼容 Binance Futures 等主流交易所。  

使用方法：通过 pip 安装 Python 包或克隆仓库，按文档准备数据后，参考示例代码（含 Python 和 Rust 实现）编写策略。教程涵盖从基础回测到复杂场景（如极端行情风控、多市场做市）的完整流程。