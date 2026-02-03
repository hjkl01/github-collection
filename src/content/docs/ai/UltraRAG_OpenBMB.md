
---
title: UltraRAG
---

### [OpenBMB UltraRAG](https://github.com/OpenBMB/UltraRAG)  ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/UltraRAG?style=social)

**项目核心内容总结：**  

**功能**：UltraRAG 是基于 Model-as-a-Service (MCP) 架构的轻量级 RAG（检索增强生成）开发框架，支持复杂工作流的低代码编排，提供模块化组件（如检索器、生成模型）和统一评估工具，可快速构建交互式原型系统。  

**使用方法**：  
1. **安装**：支持源码安装（通过 pip 或 editable 模式）和 Docker 部署（提供 CPU/GPU 版本镜像）。  
2. **验证**：运行示例命令 `ultrarag run examples/sayhello.yaml` 检查环境是否正常。  
3. **启动**：Docker 容器启动后，通过浏览器访问 `http://localhost:5050` 使用 UltraRAG UI。  

**主要特性**：  
- **低代码工作流编排**：通过 YAML 配置文件定义流程，无需复杂编码。  
- **模块化扩展**：支持自定义组件集成，适配不同检索器和生成模型（如 AgentCPM-Report）。  
- **统一评估体系**：提供标准数据集和可视化分析工具，便于研究对比。  
- **快速原型生成**：内置演示系统（如 Deep Research 管道），可一键部署复杂应用场景。  

**适用场景**：学术研究（实验流程、数据集分析）与工业应用（交互式 UI 系统、大规模检索任务）。