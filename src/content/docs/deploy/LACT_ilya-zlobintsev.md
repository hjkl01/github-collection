
---
title: LACT
---

### [ilya-zlobintsev LACT](https://github.com/ilya-zlobintsev/LACT)  ![GitHub Repo stars](https://img.shields.io/github/stars/ilya-zlobintsev/LACT?style=social)

LACT 是一款 Linux 系统下的 GPU 控制应用程序，支持 AMD、Nvidia 和 Intel 显卡。

核心功能：
1. **硬件信息**：详细报告显卡型号、VRAM、VBIOS、驱动及硬件单元状态。
2. **性能监控**：提供功耗、温度、频率的历史图表记录及 CSV 数据导出。
3. **控制调节**：支持 GPU/VRAM 超频降压、功率限制、自定义风扇曲线及热目标设置。
4. **配置管理**：支持基于进程或游戏模式的自动配置切换及 OpenTelemetry 指标导出。
5. **架构特性**：采用后台系统服务，不依赖图形会话，支持无图形界面运行，提供 GUI、CLI 及远程 TCP 管理接口。