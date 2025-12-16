
---
title: IPTV
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Free-TV/IPTV?style=social) ](https://github.com/Free-TV/IPTV)
### [Free-TV IPTV](https://github.com/Free-TV/IPTV)

**项目核心内容总结：**

**功能**：提供全球免费电视频道的M3U播放列表，支持本地（如美国、英国等国家）和互联网（如Plex TV、Pluto TV等）的免费频道。  
**使用方法**：将IPTV播放器指向网址 `https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8`。  
**主要特性**：  
- **质量优先**：仅保留稳定、高清（HD）频道，每频道仅一个URL；  
- **仅限免费**：不包含付费订阅频道，仅收录官方免费渠道（如DVB-S、DVB-T等）；  
- **主流内容**：排除成人、宗教、政治类频道及地区性小众频道。  
**数据来源**：GitHub、YouTube、Dailymotion等平台。  
**格式规范**：通过 `make_playlist.py` 生成M3U8文件，每个 `.md` 文件对应一组频道，URL列以 `[>]` 标记有效频道，其他标记（如 `Ⓢ`、`Ⓖ`、`Ⓨ`）表示画质、地理限制或直播来源。  
**贡献规范**：  
- 提交修改需通过Pull Request，仅修改 `.md` 文件；  
- 新增频道需提供免费证明，使用Imgur托管Logo，无效频道标记为 `[x]()` 并归类至“Invalid”；  
- 删除频道需证明其为付费订阅内容。