
---
title: ai-hedge-fund
---

### [virattt ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)  ![GitHub Repo stars](https://img.shields.io/github/stars/virattt/ai-hedge-fund?style=social)

**核心内容总结：**  
该项目是一个用于教育和研究的AI对冲基金原型，模拟多位投资专家（如巴菲特、格雷厄姆等）的策略，通过多个协同代理（如估值分析、情绪分析、风险控制等）生成交易信号，但**不实际进行交易**。  

**功能与特性：**  
- **多策略协同**：整合18个投资代理（如价值投资、成长投资、技术分析等），综合生成交易决策。  
- **数据支持**：依赖API获取金融数据（部分免费，如AAPL、GOOGL等），支持本地LLM（如Ollama）运行。  
- **两种运行方式**：  
  - **命令行界面**：通过Python脚本运行，支持指定股票、时间范围及回测功能。  
  - **网页应用**：提供可视化界面（需参考`app`目录说明）。  
- **教育用途**：明确声明不提供投资建议，不承担财务风险，仅用于学习和研究。  

**使用方法：**  
1. 克隆仓库并配置API密钥（如OpenAI、金融数据API）。  
2. 安装依赖（需Poetry），通过命令行运行脚本或启动回测。  
3. 网页应用需额外参考文档说明。