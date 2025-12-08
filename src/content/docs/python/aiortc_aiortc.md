
---
title: aiortc
---

### [aiortc aiortc](https://github.com/aiortc/aiortc)

**项目核心内容总结：**

**功能**  
`aiortc` 是 Python 的 WebRTC 和 ORTC 实时通信库，基于 `asyncio` 异步 I/O 框架，支持音频、视频及数据通道传输，可实现浏览器间的实时音视频通信和数据交互。

**使用方法**  
通过 `pip install aiortc` 安装后，可直接调用其 API 实现通信功能，支持与 Chrome、Firefox 浏览器的互操作性测试。

**主要特性**  
1. **协议支持**：  
   - SDP 生成与解析、ICE（含半渐进式 trickle 和 mDNS）  
   - DTLS 密钥交换与加密（SCTP 用）、SRTP 密钥管理（RTP/RTCP 加密）  
   - 纯 Python SCTP 实现  
2. **媒体传输**：  
   - 音频（Opus/PCMU/PCMA）、视频（VP8/H.264）编解码  
   - 音视频与数据通道捆绑传输  
3. **扩展性**：  
   - 支持自定义音频/视频处理（如结合 OpenCV 实现计算机视觉算法）  
   - 提供完整测试套件，确保代码质量  
4. **开发友好**：  
   - API 设计贴近 JavaScript 对应库，但使用 Python 协程和 `pyee.EventEmitter` 事件机制  
   - 代码简洁易读，便于学习 WebRTC 内部原理或二次开发  

**许可证**  
采用 BSD 协议开源。