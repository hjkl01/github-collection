### [nkaz001 hftbacktest](https://github.com/nkaz001/hftbacktest)  ![GitHub Repo stars](https://img.shields.io/github/stars/nkaz001/hftbacktest?style=social)

HftBacktest 是一款专注于高频交易和做市策略开发的高频回测框架。该工具基于 Python（Numba JIT）和 Rust，支持全订单簿（Level-2/Level-3）重建及逐笔模拟。其核心优势在于精确模拟真实市场环境，包括考虑数据流延迟、订单延迟及订单排队位置对成交的影响。项目支持多资产、多交易所回测，并允许使用相同算法代码将策略部署到 Binance Futures 和 Bybit 进行实盘交易，旨在提供接近实盘执行的高精度回测体验。