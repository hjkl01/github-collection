### [ppt-master](https://github.com/hugohe3/ppt-master) ![GitHub Repo stars](https://img.shields.io/github/stars/hugohe3/ppt-master?style=social)

PPT Master 是一个开源 AI 演示文稿生成工具，可将 PDF、DOCX、URL、Markdown 等内容一键生成**可原生编辑的 PPTX**（真实形状、文本框、图表，而非图片截图）。其核心特点是：输出文件可直接在 PowerPoint 中逐元素编辑、成本透明（主要为所用 AI 模型费用）、数据尽量本地处理（除模型通信外流程在本机运行）、不绑定单一平台（支持 Claude Code、Cursor、VS Code Copilot 等及多种模型）。

项目使用门槛低：仅需 Python 3.10+，安装依赖后即可使用；支持将素材文件放入 `projects/` 目录或直接粘贴文本生成；最终导出到 `exports/`，包含可编辑 `.pptx` 和 `_svg.pptx` 参考版本。另提供可选 AI 配图能力（支持 Gemini/OpenAI 等多后端）、Windows 专项安装文档、FAQ、示例项目与完整技术文档。