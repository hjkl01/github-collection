### [liteparse](https://github.com/run-llama/liteparse) ![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/liteparse?style=social)

LiteParse 是一个开源、可本地运行的轻量级文档解析工具，核心定位是**快速、轻依赖的 PDF/文档解析**。它基于 PDFium 做空间文本提取，支持带边界框（bbox）的高质量文本定位，不依赖云服务或专有 LLM 功能。

主要功能包括：  
- 解析 PDF 及多种格式文档（Office、图片可先自动转 PDF）  
- OCR 识别（内置 Tesseract，开箱即用；也可接入 EasyOCR、PaddleOCR 或自定义 HTTP OCR 服务）  
- 输出结构化 JSON 或纯文本，并保留版面布局信息  
- 生成页面截图（便于 LLM/Agent 处理视觉信息）  
- 支持按页解析、批量目录解析、加密文档密码、并发 OCR 等 CLI 能力  

生态与兼容性：  
- 多语言支持：Rust、Node.js/TypeScript、Python、浏览器 WASM  
- 多平台支持：Linux、macOS（Intel/ARM）、Windows  
- 提供统一 `lit` CLI（npm/pip/cargo 安装均可使用）  

整体上，LiteParse 适合本地文档抽取与结构化处理场景；对超复杂版面（密集表格、多栏、手写、扫描件）则建议使用其云端产品 LlamaParse。