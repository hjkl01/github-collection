### [charmbracelet vhs](https://github.com/charmbracelet/vhs)  ![GitHub Repo stars](https://img.shields.io/github/stars/charmbracelet/vhs?style=social)

VHS 是一个通过代码生成终端 GIF 动图的开源工具，主要用于演示命令行工具和进行集成测试。它利用 `.tape` 脚本控制虚拟终端，支持模拟键盘输入、调整终端样式（字体、主题、尺寸）、等待、截图等操作，可输出 GIF、MP4、WebM 等格式。项目支持录制终端行为生成脚本、提供 SSH 远程执行服务、发布 GIF 至服务器，并支持在持续集成流程中自动化测试。运行时需依赖 `ttyd` 和 `ffmpeg`。