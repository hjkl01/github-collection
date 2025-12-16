
---
title: moviepy
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Zulko/moviepy?style=social) ](https://github.com/Zulko/moviepy)
### [Zulko moviepy](https://github.com/Zulko/moviepy)

MoviePy 是一个用于视频编辑的 Python 库，支持常见音视频格式（包括 GIF），可在 Windows/Mac/Linux 平台上运行（需 Python 3.9+）。其核心功能包括：剪辑、拼接、添加文字标题、视频合成（非线性编辑）、音视频处理及自定义效果。  

**使用方法**：通过代码加载视频文件，提取片段、调整音量、生成文字图层并合成，最终导出为新文件。例如，可使用 `VideoFileClip` 加载视频，`subclipped` 提取片段，`TextClip` 创建文字图层，`CompositeVideoClip` 合成后保存为新文件。  

**主要特性**：将媒体转换为 Python 对象（如 numpy 数组），实现像素级操作；支持多片段混合（拼接、叠加、透明度控制等）；导出为 MP4/WebM/GIF 等格式。由于依赖数据导入导出操作，性能较直接使用 ffmpeg 更慢，但灵活性高。  

**版本说明**：v2.0 版本有重大变更，需参考官方文档更新代码。