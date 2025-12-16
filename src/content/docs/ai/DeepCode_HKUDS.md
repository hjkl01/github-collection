
---
title: DeepCode
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/HKUDS/DeepCode?style=social) ](https://github.com/HKUDS/DeepCode)
### [HKUDS DeepCode](https://github.com/HKUDS/DeepCode)

**项目核心内容总结：**

DeepCode 是一个基于多智能体系统的代码生成工具，支持将研究论文、需求描述或网页链接自动转换为生产就绪的代码，并附带测试和文档。其主要功能包括：
- **论文转代码**：自动解析学术论文并生成可执行代码
- **图像处理**：提供背景移除、图像增强等功能
- **前端开发**：支持完整Web应用开发与部署

**使用方法：**
1. 安装后通过命令行启动（`deepcode`），默认访问地址为 http://localhost:8501
2. 上传研究论文、输入需求描述或粘贴URL作为输入
3. 系统自动分析并生成代码，输出包含完整实现、单元测试和开发文档

**主要特性：**
- 多智能体协同处理复杂任务
- 支持大文档智能分段处理（自动识别技术文档、论文等长文本）
- 自动化测试与代码质量验证
- 可扩展支持多种编程语言和框架
- 提供Web界面和CLI双模式操作
- 集成Brave/Bocha-MCP两种搜索引擎（需API密钥）