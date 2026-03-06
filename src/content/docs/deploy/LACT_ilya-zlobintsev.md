
---
title: LACT
---

### [ilya-zlobintsev LACT](https://github.com/ilya-zlobintsev/LACT)  ![GitHub Repo stars](https://img.shields.io/github/stars/ilya-zlobintsev/LACT?style=social)

本项目是 Linux 系统下的 GPU 控制应用（LACT），支持 AMD、Nvidia 和 Intel 显卡。主要功能包括：

*   **信息报告**：详细显示 GPU 型号、制造商、VBIOS、VRAM 及硬件单元信息。
*   **监控**：生成功耗、温度、频率的历史图表，记录节流信息并支持 CSV 导出。
*   **电源与散热**：限制电源功率，配置电源状态（AMD），设置自定义风扇曲线及热/声学目标。
*   **超频控制**：调整 GPU/显存频率，支持显卡降压（AMD 直接，Nvidia 间接）。
*   **自动化配置**：支持基于运行进程或游戏模式状态自动切换配置文件。
*   **部署方式**：提供后台系统服务（支持无头模式）、图形界面、命令行工具及远程管理功能，支持 OpenTelemetry 指标导出。

适配多种 Linux 发行版，需依赖相应显卡驱动。