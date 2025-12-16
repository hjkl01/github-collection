
---
title: python-user-agents
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/selwin/python-user-agents?style=social) ](https://github.com/selwin/python-user-agents)
### [selwin python-user-agents](https://github.com/selwin/python-user-agents)

**核心内容总结**  

**项目功能**  
`python-user-agents` 是一个 Python 库，通过解析用户代理字符串（User Agent String），识别设备类型（如手机、平板、PC）、操作系统、浏览器信息，并判断设备是否具备触摸能力或为爬虫。  

**使用方法**  
1. 安装：`pip install user-agents`（需依赖 `ua-parser`）。  
2. 用法示例：  
   - 解析用户代理字符串：  
     ```python  
     from user_agents import parse  
     user_agent = parse("Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) ...")  
     ```  
   - 获取信息：  
     ```python  
     user_agent.browser.family  # 浏览器名称（如 "Mobile Safari"）  
     user_agent.os.version      # 操作系统版本（如 (5, 1)）  
     user_agent.device.brand    # 设备品牌（如 "Apple"）  
     ```  

**主要特性**  
- 提供 `is_mobile`、`is_tablet`、`is_pc`、`is_touch_capable`、`is_bot` 等属性，精准识别设备类型及能力。  
- 支持主流设备（如 iPhone、iPad、Android、Windows 8、Kindle 等）的检测。  
- 可通过 `str(user_agent)` 获取简洁的字符串描述（如 `"iPhone / iOS 5.1 / Mobile Safari 5.1"`）。