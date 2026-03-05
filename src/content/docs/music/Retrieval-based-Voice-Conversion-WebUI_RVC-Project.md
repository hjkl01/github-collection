
---
title: Retrieval-based-Voice-Conversion-WebUI
---

### [RVC-Project Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)  ![GitHub Repo stars](https://img.shields.io/github/stars/RVC-Project/Retrieval-based-Voice-Conversion-WebUI?style=social)

该项目是一个基于 VITS 的开源变声框架（RVC），提供训练与推理的 WebUI 界面。核心功能包括：
1. 变声与训练：支持实时变声（延迟约 170ms），采用检索特征替换防止音色泄漏；低配显卡可快速训练，少量数据（推荐 10 分钟）即可生成高质量模型，支持模型融合改变音色。
2. 音频处理：集成 UVR5 模型实现人声与伴奏分离，使用 RMVPE 算法解决哑音问题。
3. 硬件兼容：支持 N 卡、A 卡、I 卡及 CPU 加速，兼容 Windows、Linux、MacOS 系统。