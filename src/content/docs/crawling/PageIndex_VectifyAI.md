
---
title: PageIndex
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/VectifyAI/PageIndex?style=social) ](https://github.com/VectifyAI/PageIndex)
### [VectifyAI PageIndex](https://github.com/VectifyAI/PageIndex)

**PageIndex 项目核心内容总结：**

**项目功能**  
PageIndex 是一个基于推理的 **检索增强生成（RAG）系统**，通过构建 **树状索引结构**，实现对复杂文档（如金融报告）的精准内容提取与问答。无需依赖传统向量数据库或分块处理，显著提升检索准确性。

**主要特性**  
1. **无向量数据库**：不依赖向量存储，降低技术复杂度。  
2. **无分块处理**：保留文档原始层级结构，避免信息割裂。  
3. **类人检索**：通过层级索引实现类似人类的文档导航能力。  
4. **透明过程**：支持节点ID、摘要等元数据添加，增强可追溯性。  
5. **OCR 支持**：专为复杂 PDF 设计的 OCR 模型，保留文档全局结构。  

**使用方法**  
1. 安装依赖：`pip3 install --upgrade -r requirements.txt`  
2. 配置 OpenAI API 密钥（通过 `.env` 文件）。  
3. 运行脚本生成树结构：  
   ```bash  
   python3 run_pageindex.py --pdf_path /path/to/document.pdf  
   ```  
   支持 Markdown 文件（需正确层级格式）：  
   ```bash  
   python3 run_pageindex.py --md_path /path/to/document.md  
   ```  

**部署选项**  
- **自托管**：本地运行脚本处理文档。  
- **云服务**：通过 API 集成（提供 OCR、树生成等服务）。  

**案例成果**  
在金融问答基准测试（FinanceBench）中，基于 PageIndex 的 **Mafin 2.5 系统** 达到 **98.7% 准确率**，显著优于传统向量 RAG 方法。  

**资源**  
提供教程、案例研究、API 文档及社区支持（Twitter/LinkedIn/Discord）。