
---
title: olmocr
---

### [allenai olmocr](https://github.com/allenai/olmocr)  ![GitHub Repo stars](https://img.shields.io/github/stars/allenai/olmocr?style=social)

**项目核心内容总结：**

olmOCR 是一个用于从 PDF 文档中提取自然文本的工具，能够处理数百万份 PDF 文件，并通过批处理推理流水线实现高效处理。该项目基于视觉语言模型（VLM）进行文档 OCR，支持多种功能，包括文本提取、语言过滤、SEO 垃圾内容去除等。

**主要功能：**
- 从 PDF 中提取高质量的自然文本；
- 支持多语言 PDF 的过滤和处理；
- 提供 Markdown 格式的输出，保留输入 PDF 的文件结构；
- 可通过 VLLM 进行大规模模型推理；
- 支持本地、S3 和 Beaker 集群等多种运行环境。

**使用方法：**
- 可通过命令行运行，支持多种参数配置；
- 支持 Docker 镜像进行快速部署；
- 可连接外部 VLLM 服务，或在 Beaker 集群上运行。

**主要特性：**
- 高效处理大规模 PDF 数据；
- 支持多种模型（如 allenai/olmOCR-7B-0725-FP8）；
- 提供灵活的配置选项，如页面分组、重试机制、GPU 内存使用率等；
- 可通过 Beaker 进行分布式计算任务调度。

**适用场景：**
- 大规模 PDF 文档处理与文本提取；
- 用于训练语言模型的数据准备；
- 需要从非结构化文档中提取结构化信息的场景。