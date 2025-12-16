
---
title: PPTAgent
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/icip-cas/PPTAgent?style=social) ](https://github.com/icip-cas/PPTAgent)
### [icip-cas PPTAgent](https://github.com/icip-cas/PPTAgent)

**项目核心内容总结**  
PPTAgent 是一个基于文档自动生成高质量演示文稿的系统，采用两阶段方法：**分析阶段**从参考演示中学习模式，**生成阶段**创建结构化大纲并生成视觉连贯的幻灯片。配套的 **PPTEval** 评估框架从内容准确性、设计美观性和逻辑连贯性三个维度进行综合评估。  

**主要功能**  
- 支持从文本和图像动态生成幻灯片，无需人工标注参考演示；  
- 提供 Docker 镜像快速部署，支持 MCP 服务器集成；  
- 开源代码及模型（HuggingFace 可获取），包含实验版本和论文实现（EMNLP 2025 会议论文）。  

**使用方法**  
通过 Docker 镜像启动（详见 DOC.md），或参考文档中的 MCP 服务器配置指南。  

**核心特性**  
- 智能学习参考演示的结构与设计；  
- 多维度评估生成结果的质量；  
- 支持多种场景案例（如产品介绍、技术报告等）。