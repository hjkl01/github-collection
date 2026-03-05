
---
title: alive-progress
---

### [rsalmei alive-progress](https://github.com/rsalmei/alive-progress)  ![GitHub Repo stars](https://img.shields.io/github/stars/rsalmei/alive-progress?style=social)

alive-progress 是一个功能强大的 Python 进度条库，主要特性如下：

- **动态响应**：加载动画随实际处理速度实时调整快慢，直观反映任务状态，防止误判卡死。
- **高效低耗**：多线程智能刷新机制，低 CPU 占用，避免高频更新导致终端刷屏。
- **精准 ETA**：采用指数平滑算法计算预计完成时间，帮助用户有效规划工作。
- **智能挂钩**：自动增强 Python 的 print 和 logging 功能，输出中集成当前进度信息。
- **暂停恢复**：独特的暂停功能，支持中断处理流程返回解释器手动干预后无缝恢复进度。
- **最终收据**：任务结束时自动生成包含总项数、耗时及吞吐量的统计收据。
- **高度定制**：提供丰富预置样式，支持自定义动画、单位及自动缩放，兼容 Jupyter Notebook 等环境。
- **异常处理**：自动检测溢出或缺陷，支持标记跳过项以辅助断点续传和准确统计。