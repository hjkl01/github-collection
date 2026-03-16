### [linebender vello](https://github.com/linebender/vello)  ![GitHub Repo stars](https://img.shields.io/github/stars/linebender/vello?style=social)

Vello 是一款基于 Rust 编写的 GPU 计算密集型 2D 渲染引擎。它利用 wgpu 进行 GPU 访问，通过并行化算法将排序和裁剪等任务卸载到 GPU，从而以交互性能渲染大型 2D 场景。Vello 提供类似 PostScript 的 API，支持渲染形状、图像、渐变和文本，可作为 Xilem GUI 工具包等应用的渲染后端。目前处于 Alpha 状态，依赖支持计算着色器的 GPU（WebGPU 标准），支持跨平台集成。