
---
title: talk
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/vasanthv/talk?style=social) ](https://github.com/vasanthv/talk)
### [vasanthv talk](https://github.com/vasanthv/talk)

**项目核心内容总结：**

Hello 是一款基于 WebRTC 的网页端点对点视频通话工具，无需注册、下载或登录，支持主流浏览器直接使用。  

**主要功能与特性：**  
1. **即开即用**：无需账号密码，可即时创建或加入视频通话。  
2. **点对点传输**：通过 WebRTC 实现低延迟的音视频直连，多人通话采用“网状拓扑”（每人间直接连接）。  
3. **共享链接**：通过 `domain/channel-id` 格式链接快速分享通话。  
4. **嵌入支持**：可通过 `<iframe>` 将通话嵌入任意网页或应用。  
5. **无服务器中转**：媒体流不经过中央服务器，保障隐私且降低延迟。  

**使用限制**：  
- 通话质量受参与人数和网络速度影响，推荐 6-8 人以内使用（高速网络下效果更佳）。  
- 无服务器架构导致大规模群呼时可能性能下降。  

**其他信息**：  
- 开源项目，提供贡献指南和 MIT 许可证。