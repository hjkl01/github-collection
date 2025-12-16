
---
title: autocut
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mli/autocut?style=social) ](https://github.com/mli/autocut)
### [mli autocut](https://github.com/mli/autocut)

**项目功能**：AutoCut 是一个基于字幕自动剪切视频的工具。它能够自动为视频生成字幕，用户可以选择需要保留的句子，AutoCut 会根据这些句子对视频进行裁剪并保存，无需使用专业视频编辑软件，只需编辑文本文件即可完成剪切。

**使用方法**：
- 安装方式包括 pip 安装、本地安装、Docker 安装（支持 CPU 和 GPU）。
- 使用命令行运行 `autocut -d [视频文件夹]`，AutoCut 会自动为文件夹中的视频生成字幕文件（`.md` 或 `.srt`），用户可在 `.md` 文件中选择保留的句子，AutoCut 会自动剪切生成新的视频文件（如 `xxx_cut.mp4`）。
- 支持通过 `autocut -t [视频文件]` 转录视频生成字幕，通过 `autocut -c [视频] [字幕] [md文件]` 进行剪切。

**主要特性**：
- 支持多种 Whisper 模型（如 large-v3-turbo、small、medium、large）及 OpenAI API。
- 支持通过 Markdown 文件选择保留内容，方便编辑。
- 支持生成紧凑版 `.srt` 文件，便于手动编辑。
- 支持多种安装方式，包括 Python pip、本地安装和 Docker（支持 CPU 和 GPU）。
- 支持自定义编码格式（如 gbk）以兼容不同编辑器。
- 支持 GPU 加速转录（需 PyTorch 和 Nvidia 显卡）。
- 提供代码结构和开发指引，支持贡献和测试。