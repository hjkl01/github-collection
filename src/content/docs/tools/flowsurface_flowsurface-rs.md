
---
title: flowsurface
---

### [flowsurface-rs flowsurface](https://github.com/flowsurface-rs/flowsurface)  ![GitHub Repo stars](https://img.shields.io/github/stars/flowsurface-rs/flowsurface?style=social)

**Flowsurface** 是一个开源的桌面图表应用，支持 Binance、Bybit、Hyperliquid 和 OKX 等交易所，用于实时查看和分析市场数据。

---

### **核心功能**

- **多种图表类型**：
  - **热力图（历史订单簿）**：通过实时交易和 L2 深度数据生成时间序列热力图，支持价格分组和时间聚合。
  - **蜡烛图**：支持传统时间间隔和自定义交易间隔的 K 线图。
  - **交易足迹图**：在蜡烛图上展示按价格分组的交易数据，支持不平衡与裸露 POC 分析。
  - **时间与交易列表**：滚动展示实时交易记录。
  - **DOM（市场深度）/ 价格阶梯图**：展示当前 L2 深度和最近交易量。
  - **对比图**：通过多个数据源的收盘价进行归一化对比。

- **实时声音效果**：交易流驱动的实时音效。
- **多窗口/多显示器支持**。
- **面板联动**：快速切换不同面板中的交易对。
- **布局和主题可定制**：支持持久化布局和可编辑的颜色调色板。

---

### **数据来源**

- 市场数据通过交易所的公共 REST API 和 WebSocket 实时获取。
- Binance 支持历史交易数据的回溯（通过 data.binance.vision 或 REST API）。
- Bybit/Hyperliquid 不支持历史数据回溯（无合适 API），OKX 尚在开发中。

---

### **安装方式**

1. **预编译二进制文件**  
   可在 [GitHub Releases 页面](https://github.com/flowsurface-rs/flowsurface/releases) 下载适用于 Windows、macOS 和 Linux 的安装包。

2. **从源码构建**  
   - 需要安装 Rust、Git 和系统依赖。
   - 使用 `cargo install` 或克隆仓库后编译运行。

---

### **致谢**

- 受 Kraken Desktop（原 Cryptowatch）启发。
- 借鉴了 Halloy 的开源项目架构。
- 使用了 iced GUI 库实现界面功能。