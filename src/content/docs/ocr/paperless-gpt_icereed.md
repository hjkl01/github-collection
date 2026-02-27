
---
title: paperless-gpt
---

### [icereed paperless-gpt](https://github.com/icereed/paperless-gpt)  ![GitHub Repo stars](https://img.shields.io/github/stars/icereed/paperless-gpt?style=social)

**项目名称**：paperless-gpt

**项目简介**：  
paperless-gpt 是一个与 paperless-ngx 配合使用的 AI 文档管理工具，通过大型语言模型（LLM）增强 OCR 功能，实现更高质量的文本提取，自动为文档生成标题、标签、日期等元数据，提升文档整理效率。

---

### **主要功能**：

1. **LLM 增强 OCR**  
   使用 OpenAI 或 Ollama 等 LLM 提取图像中的文本，比传统 OCR 更准确，尤其适合复杂或模糊的扫描件。

2. **OCR 服务支持**  
   - LLM OCR（OpenAI/Ollama）
   - Google Document AI
   - Azure Document Intelligence
   - Docling Server（自托管）

3. **自动文档处理**  
   - 自动生成文档标题、标签、创建日期等
   - 自动识别并生成发件人信息
   - 自定义字段提取（支持三种写入模式：追加、更新、替换）

4. **生成可搜索 PDF**  
   将 OCR 结果与原始文档结合，生成带有透明文本层的 PDF，实现内容可搜索和可选中。

5. **灵活的配置选项**  
   - 通过 Web UI 自定义 AI 提示模板（标题、标签、发件人等）
   - 支持手动和自动处理模式
   - 可选择 OCR 模式（图像模式、PDF 模式、整个 PDF 模式）

6. **简单部署**  
   通过 Docker Compose 快速部署，与 paperless-ngx 集成。

---

### **使用方法**：

1. **安装依赖**  
   - 安装 Docker
   - 搭建 paperless-ngx 实例
   - 准备 LLM API 密钥或运行 Ollama 本地模型

2. **部署方式**  
   - 使用 Docker Compose 配置 `docker-compose.yml` 文件
   - 或手动克隆项目并构建 Docker 镜像

3. **配置 OCR 提供商**  
   根据需求选择 OCR 服务（如 Google、Azure 或 LLM OCR）并填写相应 API 密钥

4. **使用 Web UI**  
   - 访问 `http://localhost:8080`
   - 为文档添加标签（如 `paperless-gpt-auto`）以自动处理
   - 查看 AI 生成的标题、标签等建议并应用

5. **OCR 处理**  
   - 上传或标记需要 OCR 的文档
   - 生成增强版 PDF 或上传至 paperless-ngx
   - 可选择是否替换原始文档（需谨慎操作）

---

### **主要特性**：

- **高精度 OCR**：LLM OCR 提供比传统 OCR 更准确的结果
- **多 OCR 服务支持**：兼容 Google、Azure、Docling 等多种 OCR 服务
- **自定义提示模板**：支持在 Web UI 中自定义 AI 提示，提升处理准确性
- **PDF 文本层生成**：仅 Google Document AI 支持，生成可搜索 PDF
- **安全机制**：防止重复处理、支持备份、可跳过已有 OCR 的文档
- **灵活部署**：Docker Compose 快速部署，支持本地和云服务

---

### **注意事项**：

- 使用 Google Document AI 生成 PDF 文本层时效果最佳
- 替换原始文档（`PDF_REPLACE: "true"`）操作不可逆，需谨慎
- 建议先用 `PDF_REPLACE: "false"` 测试流程
- 可通过 `TOKEN_LIMIT` 控制 LLM 输入长度，防止超出上下文限制