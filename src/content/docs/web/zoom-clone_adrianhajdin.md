
---
title: zoom-clone
---

### [adrianhajdin zoom-clone](https://github.com/adrianhajdin/zoom-clone)

**项目核心内容总结：**

该项目是一个基于Next.js和TypeScript开发的Zoom克隆应用，支持用户登录、创建/加入会议、实时互动、录制会议、管理参会者等功能。主要技术栈包括Next.js、TypeScript、Clerk（用户认证）、getstream（实时视频交互）、Tailwind CSS（样式设计）。

**主要功能：**
- 用户通过Clerk实现社交账号或邮箱密码认证；
- 支持创建新会议、配置音视频设置后加入；
- 会议中可录制、屏幕共享、静音/取消静音、调整布局、管理参会者（如禁言、移除）；
- 可预约未来会议并查看历史会议记录及回放；
- 提供个人专属会议房间和通过链接加入会议的功能；
- 采用响应式设计适配多设备。

**使用方法：**
1. 克隆仓库并安装依赖：`git clone https://github.com/adrianhajdin/zoom-clone.git` 和 `npm install`；
2. 配置环境变量（如Clerk和getstream的API密钥）；
3. 运行项目：`npm run dev`；
4. 通过浏览器访问本地开发服务器进行测试。