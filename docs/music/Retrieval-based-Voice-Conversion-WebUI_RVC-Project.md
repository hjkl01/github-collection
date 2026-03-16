### [RVC-Project Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)  ![GitHub Repo stars](https://img.shields.io/github/stars/RVC-Project/Retrieval-based-Voice-Conversion-WebUI?style=social)

RVC（Retrieval-based-Voice-Conversion-WebUI）是一个基于 VITS 的检索式变声 WebUI 框架，核心功能包括：

1. **变声训练与推理**：支持使用少量低噪语音数据训练，通过特征检索防止音色泄漏，提供便捷的训练与推理界面。
2. **实时变声**：实现端到端低延迟（90ms-170ms）的实时变声，适用于直播或游戏场景。
3. **音频工具集成**：内置 UVR5 模型用于快速分离人声与伴奏，支持模型融合以调整音色。
4. **核心算法优化**：采用 RMVPE 音高提取算法，有效解决哑音问题且资源占用较低。
5. **多平台与硬件支持**：兼容 Windows、Linux、MacOS 系统，支持 NVIDIA、AMD 及 Intel 显卡加速。
6. **预置模型**：提供基于 VCTK 数据集训练的无版权顾虑底模。