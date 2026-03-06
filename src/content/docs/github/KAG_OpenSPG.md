
---
title: KAG
---

### [OpenSPG KAG](https://github.com/OpenSPG/KAG)  ![GitHub Repo stars](https://img.shields.io/github/stars/OpenSPG/KAG?style=social)

KAG（Knowledge Augmented Generation）是一个基于 OpenSPG 引擎和大语言模型构建的逻辑推理与问答框架，用于构建垂直领域知识库的解决方案。该项目旨在解决传统 RAG 的向量相似度歧义及 GraphRAG 的 OpenIE 噪声问题，支持逻辑推理和多跳事实问答。

主要功能包括：
1. 知识与块互索引结构，整合完整上下文文本信息。
2. 概念语义推理知识对齐，缓解知识提取噪声。
3. 模式约束知识构建，支持领域专家知识表示。
4. 逻辑形式引导的混合推理与检索，融合检索、知识图谱推理、语言推理和数值计算。

技术架构包含 kg-builder（友好 LLM 的知识表示构建）和 kg-solver（逻辑符号引导的推理引擎）。最新版本支持私有与公有知识库模式、MCP 协议集成、多模态数据索引及 KAG-Thinker 模型适配。项目提供产品模式与开发者工具两种使用方式，实现大模型与外部知识库的无缝集成。