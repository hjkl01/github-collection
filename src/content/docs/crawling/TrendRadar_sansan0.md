
---
title: TrendRadar
---

### [sansan0 TrendRadar](https://github.com/sansan0/TrendRadar)

**TrendRadar核心内容总结：**

**项目功能：**  
1. 自动爬取11+平台（如知乎、微博、B站等）的热点资讯  
2. 支持关键词筛选（含普通词/必须词/过滤词配置）  
3. 基于权重算法（排名60%+频次30%+热度10%）排序热点  
4. 生成HTML格式分析报告  
5. 多渠道推送通知（企业微信/飞书/钉钉/Telegram/邮件）  

**使用方法：**  
- **部署方式**：云端部署（GitHub Fork）或本地部署（Docker）  
- **配置步骤**：  
  ① 设置通知渠道及参数  
  ② 配置关键词文件（config/frequency_words.txt）  
  ③ 选择运行模式（daily/current/incremental）  
  ④ 设置推送时间窗口  

**主要特性：**  
- 支持多平台热点数据抓取  
- 灵活的关键词匹配与过滤机制  
- 自动化定时推送（可配置时间范围）  
- 开源协议：GPL-3.0 License