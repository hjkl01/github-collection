
---
title: Retrieval-based-Voice-Conversion-WebUI
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/RVC-Project/Retrieval-based-Voice-Conversion-WebUI?style=social) ](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
### [RVC-Project Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

**项目核心内容总结：**

**功能**  
基于VITS的语音变声框架，支持训练和实时变声，可调用UVR5分离人声与伴奏，使用RMVPE音高提取算法优化音质，提供网页操作界面。

**主要特性**  
1. 通过检索技术避免音色泄漏，支持少量数据（建议10分钟低噪语音）训练；  
2. 适配N卡、A卡、I卡，支持低延迟（170ms或90ms）；  
3. 提供模型融合功能调整音色；  
4. 支持Windows/Linux/MacOS多平台，集成预训练模型（需从Hugging Face下载）；  
5. 使用InterSpeech2023-RMVPE算法解决哑音问题，资源占用低。

**使用方法**  
1. 安装Python 3.8+，通过pip或poetry安装依赖；  
2. 下载预训练模型（如hubert_base.pt、rmvpe.pt等）及ffmpeg工具；  
3. 启动方式：  
   - 直接运行`python infer-web.py`；  
   - Windows双击`go-web.bat`，MacOS执行`sh ./run.sh`；  
   - A卡/I卡用户需额外配置ROCM或IPEX环境。  

**注意事项**  
- 训练需准备低底噪语音数据；  
- 实时变声依赖ASIO设备实现更低延迟；  
- AMD显卡需安装ROCM驱动并配置环境变量。