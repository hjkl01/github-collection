### [whatcable](https://github.com/darrylmorley/whatcable) ![GitHub Repo stars](https://img.shields.io/github/stars/darrylmorley/whatcable?style=social)

WhatCable 是一款 macOS 菜单栏工具（含 CLI），用于直观判断每个插入 Mac 的 USB-C 线缆和端口“实际能做什么”，并诊断“为什么充电变慢”。

核心功能包括：
- 按端口显示状态：Thunderbolt/USB4、普通 USB 设备、仅充电、慢速线缆、未连接等。
- 充电瓶颈分析：判断是线缆限速、Mac 当前仅请求较低功率，还是已正常满速充电。
- 读取并展示线缆 e-marker 信息：速率（USB 2.0 到 80Gbps）、电流/功率能力（3A/5A、60W/100W/240W）、芯片厂商。
- 提供“线缆可信度信号”：当 e-marker 数据异常（如 VID 异常、保留位模式等）时给出风险提示（提示“可疑”而非直接判定假货）。
- 显示充电器 PDO 电压档位及当前协商档位。
- 解析连接设备身份（PD Discover Identity）与挂载 USB 设备及协商速率。
- 显示当前活动传输类型：USB2/USB3/Thunderbolt/DisplayPort。
- 可切换查看底层 IOKit 原始属性（面向工程调试）。

配套能力：
- 提供 `whatcable` 命令行：支持人类可读摘要、JSON 输出、实时监听、原始数据输出。
- 本地运行、无私有 API、无守护进程；主要依赖 IOKit 读取 USB-C/PD 状态。
- 支持通过 Homebrew 或手动安装。

适用范围与限制：
- 仅支持 macOS 14+，且实际功能面向 Apple Silicon。
- 低功率 USB-C 线缆可能没有 e-marker，信息会有限。
- 结果依赖线缆芯片上报，软件无法验证线材内部真实做工。