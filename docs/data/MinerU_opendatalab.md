### [opendatalab MinerU](https://github.com/opendatalab/MinerU)  ![GitHub Repo stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=social)

MinerU 是一款将 PDF 转换为机器可读格式（如 Markdown、JSON）的工具，旨在解决科学文献中的内容提取与符号转换问题。

核心功能：
1. **结构化解析**：去除页眉、页脚等噪声，保持标题、段落、列表结构及语义连贯的阅读顺序。
2. **多模态提取**：自动提取图像、表格（转 HTML）、公式（转 LaTeX）及脚注。
3. **OCR 识别**：支持扫描版及乱码 PDF，识别 109 种语言。
4. **灵活输出**：支持多语言 Markdown、JSON 等格式，提供布局与元素可视化。
5. **广泛兼容**：支持 CPU/GPU/NPU/MPS 加速，兼容 Windows/Linux/macOS 及国产计算平台，提供命令行、API 和 WebUI 接口。