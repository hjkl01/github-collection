### [rsalmei alive-progress](https://github.com/rsalmei/alive-progress)  ![GitHub Repo stars](https://img.shields.io/github/stars/rsalmei/alive-progress?style=social)

alive-progress 是一款功能强大的 Python 进度条库，主要功能如下：

1. **动态响应**：实时旋转动画随实际处理速度变化，直观反映任务状态。
2. **高效低耗**：多线程更新机制，自动控制刷新频率，降低 CPU 占用并避免终端刷屏。
3. **精准预估**：采用指数平滑算法计算准确的预计完成时间（ETA）。
4. **暂停恢复**：支持暂停处理流，返回 Python 交互界面手动修复或调整数据后无缝恢复进度。
5. **深度集成**：自动挂钩 print 和 logging 函数，支持 Jupyter Notebook 环境及迭代器适配器（alive_it）。
6. **高度定制**：提供丰富的动画样式、单位自动缩放、双行文本及自定义动画工厂。
7. **统计收据**：任务结束时自动输出包含总项数、耗时和吞吐量的最终统计信息。