
---
title: atlantis
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/runatlantis/atlantis?style=social) ](https://github.com/runatlantis/atlantis)
### [runatlantis atlantis](https://github.com/runatlantis/atlantis)

**项目核心内容总结：**  
Atlantis 是一个自托管的 Go 语言应用，通过监听 Terraform 拉取请求的 Webhook 事件，实现自动化操作。其功能包括远程执行 `terraform plan`、`import`、`apply` 等命令，并将执行结果以评论形式反馈到拉取请求中。  

**使用方法：**  
- 通过 [官网指南](https://www.runatlantis.io/guide) 和 [文档](https://www.runatlantis.io/docs) 部署和配置；  
- 从 [GitHub 发布页](https://github.com/runatlantis/atlantis/releases/latest) 下载最新版本；  
- 在 [Slack 社区](https://slack.cncf.io/) 的 `#atlantis` 频道获取帮助。  

**主要特性：**  
1. 使 Terraform 变更对团队全员可见；  
2. 支持非运维工程师参与 Terraform 协作；  
3. 标准化 Terraform 工作流程。