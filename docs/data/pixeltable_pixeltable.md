### [pixeltable pixeltable](https://github.com/pixeltable/pixeltable)  ![GitHub Repo stars](https://img.shields.io/github/stars/pixeltable/pixeltable?style=social)

Pixeltable 是一个开源 Python 库，为多模态 AI 应用提供声明式数据基础设施，实现数据的存储、转换、索引、检索和编排。

核心功能包括：
1. **多模态数据管理**：原生支持图像、视频、音频和文档，自动处理格式、缓存及云存储（S3、GCS 等）对接。
2. **声明式计算列**：定义一次逻辑后自动触发执行、缓存结果及重试失败，替代 Airflow 等外部编排工具。
3. **AI 集成与向量搜索**：内置数十种 AI 提供商和本地模型支持，提供嵌入索引及语义搜索功能，内置速率限制。
4. **版本控制**：自动记录数据与架构版本，支持时间旅行（Time Travel）和历史版本回溯。
5. **实验转生产**：支持样本实验与持久化部署无缝衔接，原型代码可直接转化为生产级管线。
6. **智能体支持**：支持 UDF、查询函数及 MCP 服务器注册为工具，辅助 LLM 决策与执行。

该项目通过单一工作流替代传统 AI 栈中的数据库、向量库、存储、编排引擎及 ETL 代码，专注于应用逻辑实现。