
---
title: qmd
---

### [tobi qmd](https://github.com/tobi/qmd)  ![GitHub Repo stars](https://img.shields.io/github/stars/tobi/qmd?style=social)

### 项目核心内容总结

#### 项目名称：QMD - 查询标记文档

#### 项目功能：

QMD 是一个**本地运行的搜索引擎**，用于管理和搜索你所需的各类信息，包括 Markdown 笔记、会议记录、文档和知识库。它支持关键词搜索、语义搜索和 AI 重排序，所有操作均可在设备本地完成，无需联网。

#### 主要特性：

- **多模态搜索**：
  - **BM25 全文搜索**：快速关键词搜索。
  - **向量语义搜索**：基于语义理解的相似性搜索。
  - **LLM 重排序**：使用本地模型对结果进行质量排序。
  
- **本地运行**：使用 Bun 和 node-llama-cpp，支持 GGUF 模型，完全离线。

- **支持 AI 代理**：提供 JSON、CSV、MD 等格式输出，便于 AI 代理调用。

- **MCP 服务器集成**：支持与 Claude 等工具集成，提升交互效率。

- **多集合管理**：支持多个文档集合，每个集合可配置上下文描述，提升搜索准确性。

- **文档索引与更新**：自动或手动索引 Markdown 文件，支持更新与清理缓存。

- **结果融合策略**：
  - 使用**Reciprocal Rank Fusion (RRF)** 进行结果融合。
  - 加入**位置加权**、**重排序**，提升结果质量。

#### 使用方法：

1. **安装**：
   ```bash
   bun install -g https://github.com/tobi/qmd
   ```

2. **添加集合**：
   ```bash
   qmd collection add ~/notes --name notes
   ```

3. **添加上下文**：
   ```bash
   qmd context add qmd://notes "个人笔记和想法"
   ```

4. **生成向量嵌入**：
   ```bash
   qmd embed
   ```

5. **搜索文档**：
   ```bash
   qmd search "关键词"
   qmd vsearch "语义查询"
   qmd query "混合搜索"
   ```

6. **获取文档**：
   ```bash
   qmd get "notes/2024-01-15.md"
   qmd get "#abc123"  # 通过 docid 获取
   ```

7. **多文档获取**：
   ```bash
   qmd multi-get "journals/2025-05*.md"
   ```

8. **输出格式支持**：
   - `--json`、`--csv`、`--md`、`--xml` 等格式输出。

9. **与 AI 代理集成**：
   - 提供结构化输出，便于 AI 代理使用。
   - 支持 MCP 协议，可与 Claude 等工具集成。

#### 技术架构：

- **索引存储**：SQLite 数据库存储索引和文档信息。
- **模型支持**：
  - `embeddinggemma-300M` 用于嵌入。
  - `qwen3-reranker` 用于重排序。
  - `qmd-query-expansion` 用于查询扩展。
- **索引流程**：文档解析、分块、生成哈希 ID、存储索引。
- **查询流程**：查询扩展、多引擎检索、融合、重排序、最终结果输出。

#### 系统要求：

- **Bun >= 1.0.0**
- **macOS** 需安装 Homebrew 的 SQLite
- **依赖模型**：自动从 HuggingFace 下载并缓存。

#### 数据存储路径：

- 索引文件：`~/.cache/qmd/index.sqlite`
- 模型缓存：`~/.cache/qmd/models/`

#### 授权协议：MIT