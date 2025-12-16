
---
title: markitdown
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/markitdown?style=social) ](https://github.com/microsoft/markitdown)
### [microsoft markitdown](https://github.com/microsoft/markitdown)

**项目核心内容总结：**  
MarkItDown 是一个轻量级 Python 工具，用于将多种文件格式（如 PDF、Word、Excel、图片、音频、视频等）转换为 Markdown，便于 LLM 和文本分析工具使用。  

**主要功能与特性：**  
1. **支持格式**：PDF、PPT、Word、Excel、图片（含 OCR）、音频（含语音转文字）、HTML、文本格式（CSV/JSON/XML）、ZIP、YouTube 视频转录、EPub 等。  
2. **保留结构**：转换时保留文档结构（如标题、列表、表格、链接等），适合 LLM 处理。  
3. **可选依赖**：通过 `[pdf]`、`[docx]` 等标签安装特定格式支持，或使用 `[all]` 安装全部依赖。  
4. **插件系统**：支持第三方插件，可通过 `--use-plugins` 启用。  
5. **Azure 集成**：支持 Azure 文档智能服务进行转换。  
6. **LLM 集成**：可结合大模型（如 GPT-4o）生成图像描述。  

**使用方法：**  
- **命令行**：`markitdown 文件路径 > 输出.md` 或使用 `-o` 指定输出文件。  
- **Python API**：通过 `MarkItDown` 类调用，支持参数如 `llm_client`、`docintel_endpoint` 等。  
- **Docker**：构建镜像后运行容器处理文件。  

**安装方式**：  
- `pip install 'markitdown[all]'` 或从源码安装。  

**注意事项**：  
- 0.1.0 版本后依赖分组管理，需用 `[all]` 保持兼容性；`convert_stream()` 仅支持二进制文件对象；`DocumentConverter` 接口调整，需更新插件代码。