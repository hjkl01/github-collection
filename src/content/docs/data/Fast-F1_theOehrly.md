
---
title: Fast-F1
---

### [theOehrly Fast-F1](https://github.com/theOehrly/Fast-F1)  ![GitHub Repo stars](https://img.shields.io/github/stars/theOehrly/Fast-F1?style=social)

FastF1 是一个 Python 库，用于获取和分析 Formula 1 的比赛结果、赛程、计时数据及遥测数据。其核心功能包括：  
1. **数据获取**：通过兼容 Ergast 的 jolpica-f1 API 访问当前及历史 F1 数据，支持计时、遥测、会话结果等信息。  
2. **数据处理**：以扩展的 Pandas DataFrame 格式提供数据，内置自定义函数简化 F1 数据分析流程。  
3. **可视化**：集成 Matplotlib 实现数据可视化。  
4. **性能优化**：所有 API 请求均支持缓存，提升脚本运行效率。  

**使用方法**：  
- 通过 `pip install fastf1` 或 `conda install -c conda-forge fastf1` 安装。  
- 在 Pyodide 等 WASM 环境中需参考额外指南安装。  

**其他**：  
- 提供官方文档（[docs.fastf1.dev](https://docs.fastf1.dev)）。  
- 支持通过 GitHub 赞助或打赏支持项目。  
- 项目为非官方第三方工具，与 Formula 1 公司无关联。