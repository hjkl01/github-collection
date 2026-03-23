### [twitter the-algorithm](https://github.com/twitter/the-algorithm)  ![GitHub Repo stars](https://img.shields.io/github/stars/twitter/the-algorithm?style=social)

本项目是 X 的推荐算法系统，负责为 X 所有产品面（如关注时间线、搜索、探索、通知）提供帖子和内容流服务。

核心架构包含：
1. **数据层**：处理帖子读写、实时用户行为及信号检索。
2. **模型层**：涵盖社区嵌入、知识图谱嵌入、内容安全、交互预测、声誉计算及特征服务。
3. **框架层**：提供机器学习服务、Feed 构建、特征聚合及嵌入管理。

主要功能模块：
1. **For You Timeline**：包含候选源、排序（粗排/精排）及混合过滤服务。
2. **Recommended Notifications**：包含推荐推送及用户互动概率排序模型。

项目开源，欢迎社区贡献。