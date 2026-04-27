### [pdf-inspector](https://github.com/firecrawl/pdf-inspector) ![GitHub Repo stars](https://img.shields.io/github/stars/firecrawl/pdf-inspector?style=social)

pdf-inspector 是一个高性能的 Rust PDF 处理库，核心用于**PDF 类型分类**与**文本提取并转 Markdown**，且**不依赖 OCR/ML**。它可在本地快速判断 PDF 是文本型、扫描型、图像型或混合型，并返回置信度及需 OCR 的页码列表，实现按页智能路由。

项目主要功能包括：带坐标和字体信息的文本提取、多栏阅读顺序还原、CID/ToUnicode 字体解码、编码异常检测、双模式表格识别（图形矩形+文本对齐启发式）、以及结构化 Markdown 转换（标题、列表、代码块、表格、粗斜体、链接、分页等）。文档仅加载一次并在检测与提取间复用，避免重复解析，整体速度快（200 份文档约 4 秒）。

支持 Rust、Python、Node.js/Bun 和 CLI，用于大规模 PDF 流水线中先快速分类，再决定本地提取或送 OCR，从而显著降低延迟与成本。