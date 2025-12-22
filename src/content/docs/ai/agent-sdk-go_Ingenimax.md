
---
title: agent-sdk-go
---

### [Ingenimax agent-sdk-go](https://github.com/Ingenimax/agent-sdk-go)  ![GitHub Repo stars](https://img.shields.io/github/stars/Ingenimax/agent-sdk-go?style=social)

**项目核心内容总结：**

**GoAgents** 是一个基于 Go 语言的多功能 AI 代理 SDK，提供以下核心功能与特性：

---

### **主要功能**
1. **AI 代理开发框架**  
   支持构建具备记忆管理、任务执行、工具调用、多租户管理的 AI 代理系统，适用于自动化流程、智能助手等场景。

2. **多 LLM 集成**  
   兼容 OpenAI、Anthropic、DeepSeek、Google Vertex AI、Ollama、vLLM 等主流大模型，支持本地部署（如 Ollama/vLLM）与云端 API。

3. **MCP 服务器支持**  
   通过 Model Context Protocol（MCP）集成工具，如 AWS API、Kubernetes 管理（kubectl-ai）、文件系统操作等，实现代码与自然语言的交互。

4. **任务与流程管理**  
   支持 YAML 定义任务（如研究、搜索），提供执行计划、权限校验、复杂任务分步处理能力。

5. **向量存储与数据管理**  
   集成向量数据库（如 FAISS）和结构化数据存储（PostgreSQL/Supabase），支持语义搜索与数据持久化。

---

### **使用方法**
- **CLI 工具**  
  提供命令行交互，支持直接提问、任务执行、配置生成、MCP 服务器管理（如添加/导出 AWS API 服务器）。  
  示例：`agent-cli run "解释量子计算"` 或 `agent-cli task --agent-config agents.yaml --task=research_task`。

- **Go 代码集成**  
  通过 SDK 初始化代理、执行任务、调用工具，支持自定义 LLM 配置、MCP 工具链集成。

---

### **主要特性**
- **模块化架构**：解耦代理、LLM、记忆、工具等组件，灵活扩展。
- **多租户支持**：通过上下文隔离实现多用户/组织并发使用。
- **安全防护**：内置权限校验、危险操作拦截、内容过滤。
- **本地化部署**：支持 Ollama/vLLM 本地模型运行，降低隐私与成本。
- **动态工具发现**：MCP 服务器可自定义工具接口，无需硬编码。

---

**适用场景**：企业级 AI 应用开发、自动化运维、跨平台工具集成、多模型协作任务。