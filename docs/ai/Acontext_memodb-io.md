### [memodb-io Acontext](https://github.com/memodb-io/Acontext)  ![GitHub Repo stars](https://img.shields.io/github/stars/memodb-io/Acontext?style=social)

Acontext 是一个开源的 AI 智能体技能记忆层，旨在自动捕获智能体运行经验并将其存储为 Markdown 文件。与传统存储对话或静态文档的记忆方案不同，它专注于记录智能体的行为及结果（如 SOP、偏好、警告），支持跨智能体和框架复用，无厂商锁定。

主要功能包括：
1. **技能文件化**：以人类可读、可编辑的 Markdown 格式存储知识，支持跨模型、IDE 及 Git 管理。
2. **工具化检索**：智能体通过工具调用（如 `get_skill`）获取完整技能单元，而非基于向量语义搜索。
3. **自动学习**：基于任务完成或失败的结果，自动提取经验并生成或更新技能文件。
4. **灵活部署**：提供 Python 和 TypeScript SDK，支持云端 API 或 Docker 私有化部署。
5. **扩展能力**：集成沙箱、虚拟磁盘、上下文工程及各类智能体工具，便于构建具备长期记忆能力的应用。