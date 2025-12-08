
---
title: moon-dev-ai-agents
---

### [moondevonyt moon-dev-ai-agents](https://github.com/moondevonyt/moon-dev-ai-agents)

### 项目核心内容总结

**项目功能**  
该项目是一个基于AI的交易代理系统，包含多个模块：  
1. **RBI代理**：自动将用户提供的交易策略（如“RSI<30时买入”）转换为可回测的Python代码，并使用20+市场数据源（如BTC、ETH、SOL）进行测试，筛选出年化收益超过1%的策略。  
2. **交易代理**：支持HyperLiquid永续合约交易，提供多模型共识交易（Swarm Consensus Trading）功能。  
3. **市场监控代理**：实时监控市场数据（如流动性、价格波动），并提供趋势分析、持仓规模调整等功能。  

**使用方法**  
1. **环境准备**：克隆项目仓库，配置`.env`文件，填写Anthropic、OpenAI、CoinGecko等API密钥。  
2. **依赖安装**：使用`pip install -r requirements.txt`安装依赖。  
3. **回测执行**：  
   - 通过`ideas.txt`输入策略，运行`rbi_agent_pp_multi.py`进行回测。  
   - 使用Web仪表板（`app.py`）可视化回测结果，查看收益、夏普比率、最大回撤等指标。  

**主要特性**  
- **多模型支持**：集成Claude、GPT、DeepSeek等AI模型，自动优化策略代码。  
- **并行处理**：使用18线程并行回测，提升效率。  
- **结果筛选**：仅保留年化收益>1%的策略，优化目标为50%年化收益。  
- **自定义数据源**：可添加自定义代币数据（如Solana合约地址）。  

**未来规划**  
- 扩展Polymarket、Base链等平台支持，增加预测市场交易、L2网络集成等功能。