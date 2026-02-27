
---
title: vitess
---

### [vitessio vitess](https://github.com/vitessio/vitess)  ![GitHub Repo stars](https://img.shields.io/github/stars/vitessio/vitess?style=social)

**项目名称：Vitess**

**项目功能：**  
Vitess 是一个围绕 MySQL 构建的云原生、可水平扩展的分布式数据库系统。它通过通用分片实现无限扩展，允许应用程序代码和数据库查询对数据分布保持透明。Vitess 支持在需求增长时对分片进行拆分与合并，切换过程仅需数秒即可完成。

**使用方法：**  
Vitess 可作为数据库中间层部署在 MySQL 之上，应用程序通过 JDBC 或其他数据库连接方式访问 Vitess，无需直接操作 MySQL 节点。Vitess 会自动处理分片逻辑和数据路由。

**主要特性：**  
- **云原生与水平扩展**：支持大规模 MySQL 集群的分布式部署，实现无限制的水平扩展。  
- **分片管理**：支持分片的动态拆分与合并，切换过程快速且原子化。  
- **透明查询**：应用程序无需感知数据分布，查询逻辑对用户透明。  
- **高可用与稳定性**：由 YouTube 早期使用，经过大规模生产环境验证。  
- **活跃社区与文档**：提供社区支持、路线图、博客和文档，便于开发者参与和学习。  
- **安全性**：支持漏洞报告机制，并经过第三方安全审计。  

**项目背景：**  
Vitess 最初是 YouTube 的核心数据库组件，自 2015 年起被 Slack、Square（现 Block）、京东等大型企业广泛采用。  

**项目主页：**  
[vitess.io](https://vitess.io)