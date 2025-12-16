
---
title: diagrams
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mingrammer/diagrams?style=social) ](https://github.com/mingrammer/diagrams)
### [mingrammer diagrams](https://github.com/mingrammer/diagrams)

**项目核心内容总结：**

**功能**  
Diagrams 是一个通过 Python 代码生成云系统架构图的工具，支持 AWS、Azure、GCP、Kubernetes 等主流云服务商及本地部署、SaaS 等节点类型，适用于系统设计原型绘制和现有架构可视化。  

**使用方法**  
需 Python 3.9 及以上版本，安装 Graphviz 和 diagrams 库（支持 pip/pipenv/poetry 安装）。通过代码定义架构组件及关系，生成图表。  

**主要特性**  
- 支持多云服务商和本地/SaaS 组件；  
- 图表通过 Graphviz 渲染；  
- 可跟踪架构变更（兼容版本控制系统）；  
- 仅用于可视化，不管理实际云资源或生成 Terraform 等配置代码。  

**其他**  
- 提供示例模板（如事件处理、状态架构等）；  
- 被 Apache Airflow 等项目用于文档架构图生成；  
- 支持 Go 语言的替代实现（go-diagrams）。  

**许可证**  
MIT 开源协议。