
---
title: metube
---

### [alexta69 metube](https://github.com/alexta69/metube)  ![GitHub Repo stars](https://img.shields.io/github/stars/alexta69/metube?style=social)

**项目核心内容总结**  
Metube 是一个基于 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 的视频下载工具，提供图形化界面，支持通过 Docker 部署。其核心功能包括：  
1. **视频下载管理**：通过 UI 界面调用 yt-dlp 实现视频、音频等内容的下载，支持自定义下载路径、文件命名规则等。  
2. **配置灵活性**：可通过环境变量配置 HTTPS、反向代理（如 Nginx、Apache、Caddy）、下载目录、yt-dlp 参数（如 `YTDL_OPTIONS`）等。  
3. **反向代理支持**：提供反向代理配置示例（Nginx、Apache、Caddy），支持子路径或子域名部署，并兼容 WebSocket 通信。  
4. **HTTPS 支持**：可通过证书文件（`CERTFILE`、`KEYFILE`）启用 HTTPS 模式，或通过反向代理实现。  
5. **自动更新**：依赖 yt-dlp 的持续更新，建议通过 Watchtower 等工具定期拉取最新镜像以保持功能兼容性。  
6. **调试与问题排查**：提供在容器内直接运行 yt-dlp 命令的调试方法，建议优先通过 yt-dlp 本体测试问题。  

**使用方法**  
- **Docker 部署**：通过 `docker-compose` 或 `docker build` 构建镜像，挂载下载目录及证书文件，配置环境变量（如 `HTTPS=true`）。  
- **反向代理配置**：根据 Nginx、Apache 或 Caddy 的示例配置文件，设置代理路径及 WebSocket 支持。  
- **功能扩展**：通过提交 PR 实现新特性，或通过 `YTDL_OPTIONS` 自定义 yt-dlp 行为。  

**主要特性**  
- 基于 yt-dlp 的强大解析能力，支持主流视频网站。  
- 支持临时文件存储路径（`TEMPDIR`）与下载目录分离。  
- 提供浏览器扩展（如 Raycast）、书签脚本（Bookmarklet）等多端操作方式。  
- 支持通过 `URL_PREFIX` 配置子路径访问，适配反向代理场景。