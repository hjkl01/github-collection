
---
title: hftbacktest
---

### [nkaz001 hftbacktest](https://github.com/nkaz001/hftbacktest)  ![GitHub Repo stars](https://img.shields.io/github/stars/nkaz001/hftbacktest?style=social)

HftBacktest 是一款专为高频交易和做市策略开发设计的回测框架。它基于完整订单簿和逐笔交易数据进行市场回放，利用 Numba JIT 加速，旨在提供高精度的策略验证环境。核心功能包括支持基于时间或事件的逐 tick 模拟、Level-2 和 Level-3 数据重建订单簿、模拟行情与订单延迟及订单队列位置填充，以及支持多资产和多交易所回测。此外，该框架支持使用相同算法代码部署实盘交易机器人（当前支持 Binance Futures 和 Bybit，实盘部分使用 Rust）。项目强调回测的准确性，确保模拟结果真实反映实盘执行情况，避免过度悲观或乐观的偏差，为策略验证及优化提供可靠基础。