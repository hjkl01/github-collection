
---
title: gh-space-shooter
---

### [czl9707 gh-space-shooter](https://github.com/czl9707/gh-space-shooter)  ![GitHub Repo stars](https://img.shields.io/github/stars/czl9707/gh-space-shooter?style=social)

**项目核心内容总结**

**项目名称**：gh-space-shooter

**核心功能**：将 GitHub 用户贡献图转换为太空射击游戏风格的动画（GIF/WebP）。

**主要特性**：
1.  **游戏化呈现**：贡献量转化为敌人强度，支持粒子效果与 Galaga 风格。
2.  **高度可配置**：支持攻击策略（列/行/随机）、帧率、输出路径及最大帧数设置。
3.  **嵌入与缓存**：可生成 HTML Data URL 嵌入文档，支持 JSON 数据缓存以节省 API 配额。

**使用方法**：
1.  **前置准备**：申请 GitHub Personal Access Token 并配置 `GH_TOKEN` 环境变量。
2.  **Web 端**：使用在线界面无需安装直接生成。
3.  **GitHub Action**：配置工作流自动每日更新游戏 GIF。
4.  **命令行工具**：
    - 安装：`pip install gh-space-shooter` 或源码安装。
    - 生成：`gh-space-shooter <用户名> [选项]`。
    - 常用选项：`-o` 输出名，`-s` 策略，`--fps` 帧率，`-wdt` 生成 Data URL。

**许可证**：MIT