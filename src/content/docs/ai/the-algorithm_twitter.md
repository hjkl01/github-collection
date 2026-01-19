
---
title: the-algorithm
---

### [twitter the-algorithm](https://github.com/twitter/the-algorithm)  ![GitHub Repo stars](https://img.shields.io/github/stars/twitter/the-algorithm?style=social)

**核心内容总结：**  
该项目是X（原Twitter）的推荐算法系统，负责为所有产品界面（如“为你推荐”时间线、搜索、探索、通知等）生成内容流。其核心功能包括：  

1. **架构组成**：  
   - **数据层**：包含核心数据服务（如tweetypie处理推文读写、unified-user-actions实时追踪用户行为、user-signal-service获取用户信号）。  
   - **模型层**：涵盖社区检测（SimClusters）、知识图谱嵌入（TwHIN）、内容安全检测（trust-and-safety-models）、用户互动预测（real-graph）、用户声誉计算（tweepcred）等模型。  
   - **软件框架**：包括高性能模型服务（navi）、内容流构建框架（product-mixer）、图特征服务（graph-feature-service）等。  

2. **核心产品功能**：  
   - **For You Timeline**：通过候选源（如搜索索引、用户-推文图谱）、轻量/重量级排序模型（light-ranker/heavy-ranker）、混合过滤服务（home-mixer）等组件生成个性化内容流。  
   - **推荐通知**：通过pushservice服务结合轻量/重量级排序模型（pushservice-light/heavy-ranker）生成通知内容。  

3. **开发与协作**：  
   - 使用Bazel构建工具，部分组件需自行配置构建系统。  
   - 社区可通过GitHub提交问题和代码改进，安全问题需通过HackerOne提交。  

**主要特性**：  
- 模块化设计，支持多种内容源和排序模型；  
- 结合图算法（如GraphJet）和嵌入模型（如TwHIN）实现复杂推荐逻辑；  
- 包含内容过滤与安全机制（如visibility-filters）。