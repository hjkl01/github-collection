
---
title: return-youtube-dislike
---

### [Anarios return-youtube-dislike](https://github.com/Anarios/return-youtube-dislike)

**项目核心内容总结：**  
Return YouTube Dislike 是一个开源扩展，用于恢复 YouTube 视频的“不喜欢”计数。该项目通过抓取数据和用户数据估算，弥补 Google 于 2021 年移除 YouTube 不喜欢计数后的空白。  

**功能与使用方法：**  
- 支持 Chrome 和 Firefox 浏览器作为扩展安装，其他浏览器可通过 JS 用户脚本使用。  
- 提供公开 API（`https://returnyoutubedislikeapi.com`），第三方可调用获取视频的点赞/不喜欢数（需遵守每分钟 100 次、每天 10,000 次的请求限制，并署名项目链接）。  
- API 示例：通过 `/votes?videoId=视频ID` 获取包含点赞数、估算不喜欢数等信息的 JSON 数据。  

**主要特性：**  
- 开源且跨平台支持（扩展 + 用户脚本）。  
- 数据来源结合抓取与用户行为分析。  
- 提供 Discord 社区、GitHub 问题跟踪及捐赠渠道。  
- 限制滥用的 API 调用规则（需署名、限速）。