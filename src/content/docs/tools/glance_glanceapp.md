
---
title: glance
---

### [glanceapp glance](https://github.com/glanceapp/glance)

**项目核心内容总结：**

Glance 是一个轻量级、高度可定制的仪表盘工具，支持通过多种小部件（如 RSS 订阅、Reddit 动态、天气、市场行情等）集中展示用户关注的信息，界面简洁且支持多设备访问。

**主要功能：**
- 支持多种信息源小部件（RSS、Subreddit、Hacker News、天气、YouTube、市场数据等）
- 低资源占用，页面加载速度快（通常小于1秒）
- 支持多页面/标签、自定义布局和样式
- 移动端优化，适配手机等移动设备
- 可通过 YAML 配置文件自定义主题、小部件标题和缓存策略

**使用方法：**
1. **Docker 安装**：通过 `docker-compose` 或 Podman 部署
2. **手动安装**：支持 Go 编译构建二进制文件，或使用 Docker 构建镜像
3. **配置**：通过 YAML 文件定义页面结构、小部件类型及参数

**关键特性：**
- 数据仅在页面加载时获取，支持缓存机制
- 支持自定义开发小部件（iframe、HTML、API 接口等）
- 可通过 Dark Reader 等浏览器扩展调整主题
- 提供常见问题解决方案（如 DNS 限速、布局异常等）