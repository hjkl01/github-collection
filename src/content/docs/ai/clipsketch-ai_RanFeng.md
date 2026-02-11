
---
title: clipsketch-ai
---

### [RanFeng clipsketch-ai](https://github.com/RanFeng/clipsketch-ai)  ![GitHub Repo stars](https://img.shields.io/github/stars/RanFeng/clipsketch-ai?style=social)

**ClipSketch AI（剪辑·素描）核心内容总结：**

ClipSketch AI 是一款面向视频创作者、社交媒体运营者和二次创作者的**AI 驱动内容创作工具**，支持将视频中的精彩瞬间转化为手绘风格的故事板，并自动生成适配社交媒体的文案。

### 项目功能：

- **视频采集**：支持 Bilibili 和小红书视频链接导入，可逐帧播放、标记精彩瞬间。
- **AI 创作**：
  - 通过 Google Gemini 模型生成手绘风格故事板。
  - 根据视频内容生成三种风格的社交媒体文案（情感型、教程型、短小精悍型）。
  - 支持上传自定义角色图像并自动融合进故事板。
  - 生成高质量竖屏视频封面。
  - 批量精修分镜画面。
- **素材导出**：支持导出标记帧为 ZIP 图片包，或导出故事板、封面和文案。

### 使用方法：

1. 粘贴 Bilibili 或小红书视频链接导入。
2. 使用空格播放、左右键控制进度，按 `T` 键标记精彩帧。
3. 点击“下一步：AI 绘图”进入 AI 工作室。
4. 输入 Gemini API Key（或提前配置在 `.env` 中）。
5. 生成故事板、文案与封面，最后导出或分享。

### 主要特性：

- **帧级精准标记**：支持毫秒级时间戳记录。
- **多平台适配**：支持 PC、平板、手机。
- **快捷键操作**：空格播放、←/→ 控制、T 键标记。
- **AI 驱动创作**：Gemini 模型实现智能绘图与文案生成。
- **响应式设计**：界面自适应不同屏幕尺寸。

### 技术栈：

- React 19 / TypeScript / Tailwind CSS
- Google Gemini API / IndexedDB / Canvas API / JSZip

### 部署方式：

- 本地开发：Node.js 18+ + Gemini API Key
- Docker 部署：提供镜像一键运行

### 注意事项：

- 需要有效的 Gemini API Key 并开通 `gemini-3-pro-image-preview` 模型权限。
- 视频播放和截图涉及代理策略和无 referrer 设置。

**许可证**：MIT 协议，2024年发布。