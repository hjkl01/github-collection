
---
title: cagent
---

### [docker cagent](https://github.com/docker/cagent)  ![GitHub Repo stars](https://img.shields.io/github/stars/docker/cagent?style=social)

**项目核心内容总结：**

该项目是一个名为 **Docker cagent** 的工具，用于快速创建、运行和管理多智能体（Agent）系统。其主要功能包括：

- **创建智能体**：通过命令 `cagent new`，可以基于自然语言描述快速生成单个智能体或智能体团队。
- **运行智能体**：支持使用 OpenAI、Anthropic、Google 等 API，或本地模型（如通过 DMR 运行的模型）来运行智能体。
- **多策略检索（RAG）**：支持基于文档的语义检索、BM25 关键词检索，以及混合检索策略（如 RRF 融合）。
- **智能体团队协作**：可以定义多个智能体协同工作，支持工具调用、循环控制、结果重排序等。
- **模型集成**：支持多种大语言模型（如 GPT、Claude、Gemini）以及本地模型（DMR）。
- **知识库接入**：通过 RAG 功能，智能体可以访问并检索知识库中的文档，增强回答的准确性。
- **部署与共享**：支持通过 Docker Hub 推送和拉取智能体配置文件，方便团队协作和分享。

**使用方法：**

- 安装并配置 API 密钥（如 OpenAI、Anthropic、Google）或设置本地模型。
- 使用 `cagent new` 命令生成智能体配置文件。
- 使用 `cagent run` 命令运行智能体。
- 使用 `cagent push` 和 `cagent pull` 命令进行智能体配置文件的推送和拉取。

**主要特性：**

- 支持多种模型和检索策略，灵活适用不同场景。
- 提供智能体团队协作、工具调用、检索增强等能力。
- 支持本地模型运行（DMR）和云端模型调用。
- 提供完整的 RAG 检索系统，提升智能体的回答质量。
- 支持 Docker 镜像打包和共享，便于团队协作。