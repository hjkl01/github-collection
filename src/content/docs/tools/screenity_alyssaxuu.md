
---
title: screenity
---

### [alyssaxuu screenity](https://github.com/alyssaxuu/screenity)

### **Screenity 核心信息总结**

---

#### **1. 产品概述**
- **Screenity** 是一款 **免费且隐私友好的屏幕录制工具**，支持无限制录制桌面、摄像头、音频等，适用于工作、教育等多种场景。
- **特色功能**：AI驱动的摄像头模糊、多格式导出（mp4/gif/webm）、自定义设置（倒计时、缩放、聚光灯模式）、无需登录即可使用。

---

#### **2. 安装方式**
- **Chrome商店安装**：直接通过 [Chrome Web Store](https://chrome.google.com/webstore/detail/screenity-screen-recorder/kbbdabhdfibnancpjfhlkhafgdilcnji) 下载安装。
- **自托管**：
  1. 从 [GitHub 发布页面](https://github.com/alyssaxuu/screenity/releases) 下载 `Build.zip`。
  2. 在 Chrome 浏览器中打开 `chrome://extensions/`，启用 **开发者模式**。
  3. 解压并加载扩展文件夹。
  4. 按需配置 **Google Drive 保存**（需修改 `manifest.json` 中的 `client_id`，通过 [Google Cloud Console](https://console.cloud.google.com/) 创建 OAuth 客户端 ID）。

---

#### **3. 开发者版本配置**
- **要求**：Node.js 14 及以上。
- **步骤**：
  1. 克隆仓库：`git clone https://github.com/alyssaxuu/screenity.git`。
  2. 安装依赖：`npm install`。
  3. 启动开发服务器：`npm start`。
  4. 在 Chrome 中加载开发版本（`chrome://extensions/`，选择 **加载未打包扩展程序**，指向 `build` 文件夹）。
  5. 修改代码后重新构建：`npm run build`。

---

#### **4. 许可与商业用途**
- **许可证**：从版本 3.0.0 起，采用 **GPLv3** 协议，需阅读 [许可证条款](https://github.com/alyssaxuu/screenity/blob/master/LICENSE)。
- **商业用途**：如需基于 Screenity 开发商业产品，需联系开发者 [Alyssa X](https://alyssax.com)。

---

#### **5. 致谢与推荐**
- **Recall.ai**：提供桌面录制 API 服务，支持 Zoom、Google Meet 等平台。
- **推荐平台**：[Product Hunt](https://www.producthunt.com/posts/screenity)、[Hacker News](https://news.ycombinator.com/item?id=25150804)。

---

#### **6. 其他信息**
- **高级功能**：[Screenity Pro](https://screenity.io/pro) 提供欧盟托管服务，支持链接分享、多场景编辑、字幕等功能。
- **隐私保障**：所有数据本地处理，不收集用户信息，支持离线使用。

---

通过以上信息，用户可根据需求选择安装方式或开发配置，充分利用 Screenity 的功能。