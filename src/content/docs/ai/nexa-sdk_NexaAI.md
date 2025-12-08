
---
title: nexa-sdk
---

### [NexaAI nexa-sdk](https://github.com/NexaAI/nexa-sdk)

**项目核心内容总结：**  
NexaSDK 是一个支持在多种硬件（NPUs、GPUs、CPUs）上运行 AI 模型的跨平台工具，基于自研的 NexaML 引擎。其核心功能包括：  
1. **多硬件与格式支持**：兼容 GGUF、MLX 和自研 .nexa 格式模型，支持 macOS、Windows、Linux 等系统，尤其强调对 NPU（如 Qualcomm、Apple）的优化。  
2. **跨平台与多模态能力**：覆盖桌面、移动设备、汽车及 IoT 场景，支持文本、图像、音频等多模态模型（如 Qwen3-VL、Gemma3n）。  
3. **快速部署与易用性**：通过 CLI 命令（如 `nexa infer`）一键运行模型，支持从 Hugging Face 拉取模型，并提供本地文件导入功能。  
4. **特性优势**：相比其他工具，NexaSDK 在 NPU 支持、Android SDK、多模态模型兼容性方面表现突出，且提供 OpenAI 兼容的 REST 服务接口。  

**使用方法**：  
- 下载对应操作系统的 CLI（提供 macOS、Windows、Linux 的安装脚本）。  
- 使用 `nexa infer <模型仓库名>` 运行模型，支持 GGUF、MLX 和 Qualcomm NPU 模型。  
- 通过 `nexa pull` 缓存模型，`nexa list/remove` 管理本地模型，`nexa serve` 启动服务接口。  
- 部分 Pro 模型需注册账号并配置访问令牌。  

**主要特性**：  
- 一行代码部署模型，支持拖拽图片/音频直接交互。  
- 社区驱动的模型需求投票（[Nexa Wishlist](https://sdk.nexa.ai/wishlist)）。  
- 支持 Qualcomm NPU（需 Snapdragon X Elite 芯片）和 Apple Neural Engine 的专属优化模型。