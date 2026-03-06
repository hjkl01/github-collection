
---
title: openevolve
---

### [codelion openevolve](https://github.com/codelion/openevolve)  ![GitHub Repo stars](https://img.shields.io/github/stars/codelion/openevolve?style=social)

OpenEvolve 是一个开源的进化编码代理项目，利用大语言模型（LLM）将代码转化为自主优化的智能体。主要功能包括：

1. **自主发现与优化**：结合 MAP-Elites 算法与 LLM，自动进化代码、算法及提示词，无需人工干预即可发现突破性解决方案。
2. **多场景应用**：支持 GPU 内核优化、数学问题求解、科学计算、竞赛编程等多语言（Python, Rust, Metal 等）领域。
3. **高效与可复现**：提供确定性进化流程，支持并行进化与多目标优化，比手动优化节省时间且结果可完全复现。
4. **灵活部署**：兼容 OpenAI、Gemini 及本地 LLM 模型，支持自定义评估器、提示词模板及进化参数配置。
5. **反馈与可视化**：通过执行反馈（Artifacts）形成优化闭环，并提供实时进化追踪与代码差异对比界面。