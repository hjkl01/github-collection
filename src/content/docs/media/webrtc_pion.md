
---
title: webrtc
---

### [pion webrtc](https://github.com/pion/webrtc)  ![GitHub Repo stars](https://img.shields.io/github/stars/pion/webrtc?style=social)

Pion WebRTC 是一个纯 Go 实现的 WebRTC API，支持实时音视频通信和数据通道传输。项目提供完整的 PeerConnection 接口（包括数据通道、音视频收发、重协商等）、ICE 连接协议（含 STUN/TURN 服务器支持）、媒体处理（支持 Opus、H264、VP8/VP9 等编码格式）及安全功能（DTLS/SRTP 加密）。  

使用时需通过 Go Modules 引入 `github.com/pion/webrtc/v4`，并配合示例代码（如音视频传输、 simulcast、带宽估算等）进行开发。项目支持跨平台（Windows/macOS/Linux/FreeBSD/iOS/Android/WebAssembly）且无需 Cgo，构建速度快（示例项目构建耗时约 0.28 秒）。  

主要特性包括：支持 Plan-B 和 Unified Plan 架构、RTP/RTCP 直接访问、硬件加速的加密套件、NACK 丢包补偿、TWCC 拥塞控制反馈，以及与 GStreamer、x264 等工具链的集成。