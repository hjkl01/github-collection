
---
title: AreaCity-JsSpider-StatsGov
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/xiangyuecn/AreaCity-JsSpider-StatsGov?style=social) ](https://github.com/xiangyuecn/AreaCity-JsSpider-StatsGov)
### [xiangyuecn AreaCity-JsSpider-StatsGov](https://github.com/xiangyuecn/AreaCity-JsSpider-StatsGov)

**项目核心内容总结：**  
该项目提供中国及部分地区的行政区划数据采集、处理与格式化工具，支持省市区县、乡镇等多级数据，包含拼音标注、坐标边界信息。  

**功能与特性：**  
1. **数据采集**：通过JavaScript在Chrome控制台运行脚本，从统计局、民政部等网站抓取行政区划数据，支持处理乱码、验证码限制及多编码格式转换。  
2. **数据处理**：  
   - 自动转换拼音并校正多音字读音（如“宕昌县”“洪洞县”）。  
   - 支持自定义排序规则（如拼音首字母+名称组合）。  
   - 提供坐标与边界信息采集工具（基于高德地图API）。  
3. **工具支持**：包含数据格式化脚本、拼音转换接口（公网+本地结合）、数据修正功能。  

**使用方法：**  
- 按顺序在Chrome控制台执行1-3开头的JS文件，完成数据采集与转换。  
- 使用`map_geo.js`脚本在高德地图测试页面采集坐标和边界数据。  
- 需注意统计局请求限制，启用浏览器缓存以提高效率。