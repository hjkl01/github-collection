
---
title: scrapydweb
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/my8100/scrapydweb?style=social) ](https://github.com/my8100/scrapydweb)
### [my8100 scrapydweb](https://github.com/my8100/scrapydweb)

**ScrapydWeb** 是一个用于管理 **Scrapyd 集群** 的 Web 应用，支持 **Scrapy 日志分析与可视化**。  

### **核心功能**  
- **集群管理**：支持所有 Scrapyd JSON API，可分组、过滤节点，并通过点击操作批量执行命令。  
- **日志分析**：提供统计图表、进度可视化、日志分类等功能。  
- **增强特性**：自动打包、集成日志分析工具 LogParser、定时任务、监控告警、移动端适配、基础认证等。  

### **使用方法**  
1. **安装**：通过 `pip install scrapydweb` 安装。  
2. **启动**：运行 `scrapydweb` 命令（首次启动会生成配置文件）。  
3. **访问**：浏览器打开 `http://127.0.0.1:5000`（推荐使用 Chrome）。  
4. **前提条件**：需先在所有主机上安装并启动 Scrapyd，配置 `bind_address = 0.0.0.0` 以允许远程访问。  

### **技术栈**  
- 前端：Element、ECharts  
- 后端：Flask  

### **其他**  
- 提供 Heroku 部署示例及测试方法。  
- 支持通过 GitHub 参与贡献。