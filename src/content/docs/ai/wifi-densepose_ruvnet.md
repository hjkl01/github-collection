
---
title: wifi-densepose
---

### [ruvnet wifi-densepose](https://github.com/ruvnet/wifi-densepose)  ![GitHub Repo stars](https://img.shields.io/github/stars/ruvnet/wifi-densepose?style=social)

### 项目核心内容总结

**WiFi DensePose** 是一个基于 WiFi 信号的人体姿态估计系统，通过 **信道状态信息（CSI）** 和 **机器学习** 实现无摄像头的实时隐私保护式姿态检测。

---

### 项目功能

1. **实时人体姿态检测**：利用 WiFi 信号实现每秒 30 帧（FPS）的实时姿态估计。
2. **多人跟踪**：支持最多同时追踪 10 人。
3. **隐私保护**：无需摄像头，通过 WiFi 信号进行检测，保障用户隐私。
4. **多场景支持**：适用于医疗、健身、智能家居、安防等场景。
5. **灾害响应模块（WiFi-Mat）**：专为搜索与救援设计，可检测埋在废墟下的幸存者，包括：
   - 生命体征检测（呼吸、心跳）
   - 3D 定位（最大深度 5 米）
   - 自动分类伤员（立即/延迟/轻微/死亡）
   - 实时警报与优先级通知

---

### 使用方法

1. **安装**：
   - 使用 pip 安装（推荐）：`pip install wifi-densepose`
   - 或从源码安装：`git clone https://github.com/ruvnet/wifi-densepose.git` 并运行 `pip install -e .`
   - 使用 Docker：`docker run -p 8000:8000 ruvnet/wifi-densepose:latest`

2. **快速启动**：
   - 初始化系统：`from wifi_densepose import WiFiDensePose`，调用 `system.start()` 开始检测。
   - 使用 REST API 启动服务：`wifi-densepose start`
   - 使用 WebSocket 实时流获取姿态数据。

3. **配置**：
   - 支持通过 `.env` 文件设置网络接口、硬件参数、姿态置信度阈值等。
   - 提供 CLI 命令管理 API 服务、数据库、任务等。

---

### 主要特性

- **隐私优先**：不依赖摄像头，使用 WiFi 信号进行检测。
- **高性能**：通过 Rust 实现的 v2 版本，处理速度比 Python 快数百倍，全流程延迟低至 18.47 微秒。
- **多平台支持**：支持 Linux、macOS、Windows，硬件兼容主流 WiFi 路由器。
- **WebSocket 流式传输**：实时传输姿态数据，适用于直播类应用。
- **企业级 API**：支持认证、限流、监控等功能，适合生产环境部署。
- **100% 测试覆盖率**：包含单元测试、集成测试、端到端测试和性能测试。
- **灾害响应支持**：专为地震、塌方、雪崩等灾害场景设计的模块，支持实时定位与生命体征检测。

---

### 硬件要求

- 支持 CSI 提取的 WiFi 路由器（如 ASUS AX6000、Netgear Nighthawk AX12）
- 支持 CSI 提取的 WiFi 卡（如 Intel 5300、Atheros AR9300）
- 推荐使用 GPU 加速（如 NVIDIA GPU）以提升性能。

---

### 总结

WiFi DensePose 是一个基于 WiFi 的实时人体姿态估计系统，具有高精度、低延迟、隐私保护和多场景适应能力。项目提供完整的 API 和 CLI 工具，支持多种部署方式，适合医疗、安防、灾害救援等应用。通过 Rust 实现的高性能版本极大提升了处理速度，适合对性能有高要求的场景。