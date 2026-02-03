
---
title: mistral.rs
---

### [EricLBuehler mistral.rs](https://github.com/EricLBuehler/mistral.rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/EricLBuehler/mistral.rs?style=social)

**项目名称**：mistral.rs

**项目简介**：  
mistral.rs 是一个高性能、多功能的大型语言模型（LLM）推理框架，支持多种模型架构和量化方式，适用于文本、视觉、语音等多种任务。项目提供 Python 和 Rust SDK，方便开发者快速构建和部署模型应用。

---

**核心功能**：

- **支持多种模型**：包括主流的文本、视觉、语音、图像生成和嵌入模型，支持 HuggingFace 上的大多数模型，无需转换或上传。
- **多模态支持**：支持图像、语音、文本等多种输入输出。
- **自动配置与运行**：通过 CLI 工具，可一键运行模型，自动检测模型架构、量化格式和聊天模板。
- **内置 Web UI**：通过 `mistralrs serve --ui` 命令即可启动带 Web 界面的服务，方便用户交互。
- **硬件自适应**：支持 CUDA、Metal、多 GPU 并行，可根据硬件自动选择最优配置。
- **量化控制**：支持多种量化格式（如 GGUF、GPTQ、AWQ、FP8 等），并提供自定义量化功能。
- **SDK 支持**：提供 Python 和 Rust SDK，方便开发者集成到自己的项目中。

---

**使用方法**：

- **安装**：
  - Linux/macOS：`curl` 安装脚本
  - Windows：PowerShell 安装脚本

- **运行模型**：
  ```bash
  mistralrs run -m Qwen/Qwen3-4B
  ```

- **启动带 UI 的服务**：
  ```bash
  mistralrs serve --ui -m google/gemma-3-4b-it
  ```

- **Python SDK 示例**：
  ```python
  from mistralrs import Runner, Which, ChatCompletionRequest
  runner = Runner(which=Which.Plain(model_id="Qwen/Qwen3-4B"), in_situ_quant="4")
  res = runner.send_chat_completion_request(ChatCompletionRequest(...))
  ```

- **Rust SDK 示例**：
  ```rust
  use mistralrs::{IsqType, TextMessageRole, TextMessages, VisionModelBuilder};
  let model = VisionModelBuilder::new("google/gemma-3-4b-it").with_isq(IsqType::Q4K).build().await?;
  ```

---

**主要特性**：

- **快速推理**：基于 FlashAttention、PagedAttention 等技术优化性能。
- **灵活部署**：支持本地运行、多 GPU 并行、Docker 容器部署。
- **量化优化**：支持多种量化方式，可自定义每层的量化策略。
- **扩展性强**：支持 LoRA、X-LoRA、Mixture-of-Experts（MoE）等模型结构。
- **工具集成**：支持工具调用、Web 搜索、MCP 客户端等高级功能。

---

**文档与资源**：

- 官方文档：https://ericlbuehler.github.io/mistral.rs/
- Python SDK：https://ericlbuehler.github.io/mistral.rs/PYTHON_SDK.html
- Rust SDK：https://crates.io/crates/mistralrs
- 模型支持列表：docs/SUPPORTED_MODELS.md
- Docker 部署：支持容器化部署

---

**项目定位**：  
mistral.rs 旨在为开发者提供一个高效、灵活、易于使用的 LLM 推理框架，支持从模型加载、量化、部署到应用构建的全流程。