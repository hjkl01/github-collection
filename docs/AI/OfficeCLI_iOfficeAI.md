### [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) ![GitHub Repo stars](https://img.shields.io/github/stars/iOfficeAI/OfficeCLI?style=social)

OfficeCLI 是一个面向 AI 智能体的开源 Office 命令行工具，可用单一二进制文件在 macOS/Linux/Windows 上直接创建、读取、分析、修改和重组 Word（.docx）、Excel（.xlsx）、PowerPoint（.pptx）文档，无需安装 Microsoft Office 或额外依赖。

核心能力包括：  
- 文档全生命周期操作：创建、查看、查询、编辑、删除、移动、交换、合并模板（`{{key}}`）  
- 结构化输出：所有命令支持 JSON，便于 AI 稳定调用与自动纠错  
- 三层操作模型：高级语义视图（L1）→ 元素级 DOM 操作（L2）→ 原始 XML/XPath 回退（L3）  
- 实时预览：`watch` 提供浏览器实时渲染与自动刷新（尤其适合 PPT/Excel 迭代）  
- 高性能自动化：支持驻留模式（内存常驻）和批处理（单次开关文件执行多操作）  
- 质量与健壮性：支持 OpenXML 校验、问题检测（如格式/结构错误）、标准化错误码与修复建议  

AI 集成能力突出：  
- 内置 MCP Server，可一键接入 Claude、Cursor、VS Code/Copilot、LM Studio 等  
- 自动识别并安装 AI 工具技能文件（SKILL.md），几乎零配置即可让智能体操作 Office 文档  
- 支持任意编程语言通过 CLI 调用，适用于脚本、服务端、CI/CD、容器化无头环境  

项目定位是“AI 原生的 Office 自动化标准 CLI”：以更少命令替代传统多库多代码方案，统一处理 Word/Excel/PPT，适合报告生成、批量处理、数据抽取、文档质检与团队文档流水线。