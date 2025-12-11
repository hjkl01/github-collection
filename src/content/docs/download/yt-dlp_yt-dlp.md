
---
title: yt-dlp
---

### [yt-dlp yt-dlp](https://github.com/yt-dlp/yt-dlp)

**项目核心内容总结：**

yt-dlp 是一个基于 Python 的视频下载工具，支持从多个视频网站（如 YouTube、Bilibili 等）下载视频及音频，功能与 youtube-dl 兼容并扩展。其主要特性包括：

1. **功能**  
   - 支持 HLS、DASH 等主流视频格式，可下载加密视频（如 YouTube 加密链接）。  
   - 提供灵活的参数控制，如选择音视频格式、自定义输出文件名、过滤视频（如按标题、时长、观看数）。  
   - 支持 SponsorBlock 功能，可跳过广告或标记赞助内容。  

2. **使用方法**  
   - 命令行调用，基本格式为 `yt-dlp [参数] 视频链接`。  
   - 常用参数包括 `--format`（指定格式）、`-o`（自定义文件名）、`--match-filters`（过滤条件）、`--sponsorblock`（广告处理）。  

3. **主要特性**  
   - **兼容性**：提供 `--compat-options` 参数兼容旧版本功能（如 2021/2022/2023 等）。  
   - **安全性**：默认拒绝下载危险文件扩展名，可通过 `--allow-unsafe-ext`（需谨慎）覆盖。  
   - **灵活性**：支持自定义 HTTP 请求头（`--add-headers`）、限制下载速率（`--limit-rate`）、分段下载（`--playlist-start/end`）。  

**注意事项**：部分旧参数已弃用（如 `--list-formats-old`），推荐使用新语法；避免使用 `--allow-unsafe-ext` 以防安全风险。