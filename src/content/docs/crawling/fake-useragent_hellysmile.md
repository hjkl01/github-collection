
---
title: fake-useragent
---

### [hellysmile fake-useragent](https://github.com/hellysmile/fake-useragent)

**项目核心内容总结：**

**功能**  
生成随机User-Agent字符串，支持多种浏览器（如Chrome、Firefox、Edge等）和操作系统（Windows、Linux、Mac等），适用于爬虫或模拟不同设备访问。

**使用方法**  
1. 导入库并创建`UserAgent`实例。  
2. 调用方法生成User-Agent，如`ua.random`（随机生成）或指定浏览器/操作系统（如`ua.chrome`）。  
3. 可通过参数过滤（如`browsers=["Chrome"]`、`os=["Windows"]`、`platforms=["desktop"]`）。  
4. 支持获取完整数据字典（如`ua.getRandom()`返回包含详细信息的Python字典）。

**主要特性**  
- **多平台支持**：覆盖主流浏览器、操作系统及设备类型（桌面、移动、平板）。  
- **灵活过滤**：可自定义浏览器、操作系统、使用率等条件。  
- **数据管理**：支持本地缓存、自定义数据源路径及异常处理（如`fallback`备用浏览器）。  
- **扩展性**：提供`getBrowser()`方法获取特定浏览器数据，支持未来功能扩展。  
- **兼容性**：适配Python 3.7+，支持多种依赖库（如`importlib-resources`）。