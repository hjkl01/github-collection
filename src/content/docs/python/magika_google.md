
---
title: magika
---

### [google magika](https://github.com/google/magika)

**核心内容总结：**  
Magika 是一个基于 AI 的高效文件类型识别工具，利用深度学习模型在几毫秒内准确识别文件类型（支持 200+ 内容类型，准确率约 99%），模型体积仅数 MB，可在单核 CPU 上快速运行。  

**功能与使用方法：**  
- 提供命令行工具（Rust 编写）、Python API 及 JavaScript/TypeScript、Go 的绑定，支持通过 `pipx`、`pip`、`npm` 等方式安装。  
- 命令行支持递归扫描目录、输出 JSON 格式结果、控制预测置信度模式（如 `high-confidence`、`best-guess`）等。  
- Python 示例可通过 `identify_bytes`、`identify_path` 等方法直接调用。  

**主要特性：**  
- 推理时间短（加载模型后约 5ms/文件），且与文件大小无关；  
- 支持文本与二进制文件识别，提供 MIME 类型、扩展名、置信度等详细输出；  
- 开源且跨平台，集成于 VirusTotal 等工具，适用于大规模文件分析场景。