
---
title: PasteMD
---

### [RICHQAQ PasteMD](https://github.com/RICHQAQ/PasteMD)  ![GitHub Repo stars](https://img.shields.io/github/stars/RICHQAQ/PasteMD?style=social)

PasteMD 是一款 Windows 后台驻留工具，旨在解决 AI 生成内容（如公式、表格、富文本）复制到 Word/WPS/Excel 时格式错乱的问题。

**核心功能：**
1. **一键粘贴转换**：通过全局热键，将剪贴板中的 Markdown 或 HTML 内容转换为 DOCX 并自动插入 Word/WPS 光标位置。
2. **智能表格处理**：自动识别 Markdown 表格并粘贴至 Excel，保留原有格式。
3. **应用扩展配置**：支持按目标应用或窗口标题匹配（如语雀、QQ），自定义不同粘贴模式（HTML/Markdown/LaTeX/文件）。
4. **转换增强**：支持配置 Pandoc Filters，自动修复部分 LaTeX 语法与单 `$...$` 公式块。
5. **自动化辅助**：自动检测前台应用（Word/WPS/Excel），提供托盘菜单、系统通知及日志管理。

该工具基于 Python 和 Pandoc 开发，兼容主流 AI 对话网站内容。