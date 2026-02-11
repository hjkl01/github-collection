
---
title: UI-TARS
---

### [bytedance UI-TARS](https://github.com/bytedance/UI-TARS)  ![GitHub Repo stars](https://img.shields.io/github/stars/bytedance/UI-TARS?style=social)

**项目核心内容总结：**

**项目名称：** UI-TARS-1.5，是一个开源的多模态智能体模型，能够自动执行图形用户界面（GUI）任务，包括电脑操作、网页浏览、手机应用交互和游戏等。

**主要功能：**
- 支持桌面环境（Windows、Linux、macOS）的 GUI 任务，如点击、拖拽、键盘输入、滚动等；
- 支持移动端（Android）的 GUI 任务，如长按、打开应用、返回操作等；
- 可用于游戏自动化（如 2048、Maze、Snake 等），并取得满分成绩；
- 可在 Minecraft 中完成挖矿、击杀怪物等任务；
- 提供本地部署版本（UI-TARS-desktop），可在个人设备上运行；
- 支持 Web 自动化，可结合 Midscene.js 使用。

**主要特性：**
- 基于视觉语言模型，具备推理能力，能先思考再行动；
- 提供多种提示模板（COMPUTER_USE、MOBILE_USE、GROUNDING）以适应不同平台；
- 提供坐标处理工具，便于模型输出与实际屏幕操作的映射；
- 在多个 GUI 基准测试中表现优异，超越现有 SOTA 模型；
- 支持 HuggingFace 模型部署，提供详细部署与推理文档；
- 提供代码解析工具，可将模型输出转换为 PyAutoGUI 可执行代码。

**使用方法：**
1. 从 HuggingFace 下载模型；
2. 参考 `README_deploy.md` 进行部署；
3. 使用 `ui_tars` Python 包解析模型输出为可执行操作；
4. 选择适合的提示模板进行任务执行；
5. 可通过 UI-TARS-desktop 在本地设备上运行。

**性能表现：**
- 在 OSWorld、Windows Agent Arena 等电脑任务中表现领先；
- 在 ScreenSpot、ScreenSpotPro 等视觉定位任务中表现优异；
- 在多种游戏和 Minecraft 任务中达到满分或接近满分；
- 模型性能随规模提升（如 72B 模型在部分任务中优于 7B）。

**限制：**
- 需较高计算资源；
- 存在幻觉风险，可能在复杂或模糊环境中出错；
- 有潜在被滥用的风险（如绕过 CAPTCHA），已进行安全评估；
- 7B 模型虽通用性强，但在游戏任务中仍优于其他模型。

**获取方式：**
- 模型：[HuggingFace](https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B)
- 代码：[GitHub](https://github.com/bytedance/UI-TARS)
- 论文：[arXiv](https://arxiv.org/abs/2501.12326)
- 最新版本：UI-TARS-2，支持更多任务和能力，详情见[技术报告](https://arxiv.org/abs/2509.02544)。