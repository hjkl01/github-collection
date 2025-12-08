
---
title: VirtualWife
---

### [yakami129 VirtualWife](https://github.com/yakami129/VirtualWife)

**项目核心内容总结：**  
VirtualWife 是一个虚拟数字人项目，旨在通过 AI 技术提供情感陪伴服务，具备恋爱导师、心理咨询等功能。  

**主要功能：**  
- 支持通过 Docker 快速部署（兼容 Linux/Windows/MacOS）；  
- 可自定义角色设定及更换 VRM 模型；  
- 集成长短期记忆、多语言模型（含私有化模型）切换、文字驱动表情/动作；  
- 支持 B 站直播、中文语音（Edge/Bert-VITS2）、流式数据传输；  
- 提供角色扮演深化、情感模块优化等未来开发计划。  

**使用方法：**  
1. 安装 Docker 及 docker-compose；  
2. 进入项目目录，复制 `.env_example` 为 `.env` 并配置环境变量；  
3. 通过 `start.sh`（Linux）或 `start.bat`（Windows）启动服务；  
4. 访问 `http://localhost/` 进行角色及模型配置，保存后即可使用。  

**核心特性：**  
- 一键部署、跨平台兼容；  
- 多模型支持与记忆功能；  
- 语音/动作驱动及直播能力；  
- 开源协议（MIT）且提供中文技术文档。