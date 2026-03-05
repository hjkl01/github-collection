
---
title: wifi-densepose
---

### [ruvnet wifi-densepose](https://github.com/ruvnet/wifi-densepose)  ![GitHub Repo stars](https://img.shields.io/github/stars/ruvnet/wifi-densepose?style=social)

π RuView 是一款基于 WiFi 信号的非接触式感知系统，无需摄像头或可穿戴设备即可实现穿墙人体感知。系统通过采集信道状态信息 (CSI)，利用 Rust 高性能引擎和边缘智能技术，实时完成以下功能：

1.  **人体姿态估计**：重建身体位置和骨架，支持多人同时追踪。
2.  **生命体征监测**：检测呼吸率和心率，无需医疗设备。
3.  **存在检测**：毫秒级延迟识别人员活动。
4.  **灾难救援**：支持通过废墟探测幸存者及生命体征。

核心特性包括全本地隐私保护（无云端/互联网依赖）、穿墙工作能力、自学习模型适应不同环境，以及模块化边缘智能（ESP32 上运行 WASM 模块）。适用于医疗照护、智能家居、安防监控及应急搜救等场景。