
---
title: DouyinLiveWebFetcher
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/saermart/DouyinLiveWebFetcher?style=social) ](https://github.com/saermart/DouyinLiveWebFetcher)
### [saermart DouyinLiveWebFetcher](https://github.com/saermart/DouyinLiveWebFetcher)

**项目核心内容总结：**  
该项目用于抓取抖音网页版直播间的弹幕数据，包括用户进场、送礼、点赞、聊天等行为信息。  

**功能特性：**  
- 支持实时抓取弹幕消息（如用户进入直播间、礼物赠送、点赞统计等）；  
- 持续更新维护，适配最新接口（如2025年更新WebSocket协议、新增`a_bogus`参数等）；  
- 提供测试记录，验证代码在多时间点的稳定性。  

**使用方法：**  
- 环境要求：Python 3.7+、Node.js v18.2.0、`protoc`版本`libprotoc 25.1`；  
- 通过代码实现数据抓取，需自行处理反爬机制（如签名生成）。  

**注意事项：**  
项目仅用于学习交流，禁止用于商业或非法用途，涉及侵权可联系作者删除代码。