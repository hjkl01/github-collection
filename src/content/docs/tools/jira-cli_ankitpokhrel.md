
---
title: jira-cli
---

### [ankitpokhrel jira-cli](https://github.com/ankitpokhrel/jira-cli)  ![GitHub Repo stars](https://img.shields.io/github/stars/ankitpokhrel/jira-cli?style=social)

**项目核心内容总结：**  
该项目是一个用于与 Atlassian Jira 平台交互的命令行工具，支持问题管理、冲刺（Sprint）、版本（Release）、项目等操作。  

**主要功能：**  
- **问题管理**：创建、编辑、删除问题，支持批量操作（如添加/移除问题到冲刺、史诗），可按状态、优先级、负责人等筛选问题。  
- **冲刺管理**：查看当前、历史或计划中的冲刺，添加或移除问题，统计冲刺内问题数量及负责人分布。  
- **版本管理**：列出项目版本（Release），支持版本相关操作。  
- **数据统计**：通过脚本统计每日创建问题数、冲刺问题数、负责人数量等，支持输出为纯文本或表格格式。  
- **脚本支持**：提供 `--plain` 参数，便于在 Shell 脚本中处理输出数据。  

**使用方法：**  
- 通过命令行执行操作，如 `jira issue list`（列出问题）、`jira sprint add`（添加问题到冲刺）、`jira release list`（列出版本）。  
- 支持参数过滤（如 `--created month` 按创建时间筛选）、表格视图（`--table`）和纯文本视图（`--plain`）。  

**主要特性：**  
- 支持 Jira 云和本地实例。  
- 提供交互式界面和非交互式脚本模式。  
- 可扩展性：通过社区讨论提交功能需求，优先实现易实现或高频需求。  

**注意事项：**  
- 部分 Jira 节点格式可能未完全适配。  
- 需要 Jira 账号及 API 访问权限。