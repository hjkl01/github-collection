
---
title: live
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/fanmingming/live?style=social) ](https://github.com/fanmingming/live)
### [fanmingming live](https://github.com/fanmingming/live)

**核心内容总结：**  
该项目提供一个**永久免费、开源、支持IPv4/IPv6直连访问**的电视/广播台标库及配套工具，包含以下功能：  

1. **台标资源**  
   - 电视/广播图标库可通过 `https://live.fanmingming.cn/tv/{name}.png` 和 `https://live.fanmingming.cn/radio/{name}.png` 直接访问，支持自定义频道Logo上传。  

2. **工具服务**  
   - **EPG接口**：提供节目表数据（来源：112114.xyz）。  
   - **M3U生成**：通过编辑 `demo.m3u` 文件替换直播源链接，上传至GitHub Pages生成订阅链接。  
   - **在线工具**：支持M3U/TXT格式转换、Bing每日图片获取、M3U8在线下载及播放。  

3. **使用方式**  
   - 下载示例 `demo.m3u` 文件，替换直播源后上传至GitHub Pages，通过播放器订阅生成的链接。  

4. **特性**  
   - 所有资源由GitHub自动构建，主域名 `live.fanmingming.com` 通过Cloudflare提供CDN防护，镜像域名 `live.fanmingming.cn` 由Cloudflare Pages托管。  
   - 支持用户提交缺失的台标，审核通过后署名发布。  

**注意事项：**  
- 项目不存储流媒体内容，资源有效性及法律风险由用户自行承担。  
- EPG接口准确性依赖第三方站点，部分直播源可能失效。  
- 所有工具均为公益性质，不记录用户数据。  
- 资源问题可通过Telegram [@AirfoneBot](https://t.me/AirfoneBot) 反馈。