
---
title: jam
---

### [jam-systems jam](https://github.com/jam-systems/jam)

**Jam 项目核心内容总结：**

**项目功能**  
Jam 是一个开源的音频聊天平台，提供类似 Clubhouse 和 Twitter Spaces 的功能，支持创建音频房间用于讨论、音乐演出、戏剧等场景。用户可通过网页、iOS、Android 等多平台使用。

**主要特性**  
- **品牌自定义**：支持设置房间 Logo、颜色等品牌信息。  
- **嵌入能力**：可通过 iframe、WebView 或 JS SDK 集成到第三方应用或网站。  
- **互动功能**：支持动画反应（如 ❤️、😂）、描述与链接（支持 Markdown）、用户通过房间赚取收入（支持 PayPal、比特币等）。  
- **数据主权**：服务器部署于欧盟（德国），支持开源自托管。  
- **扩展性**：单房间最多支持数百人，无平台限制（取决于服务器性能）。  

**使用方法**  
1. **房间配置**：通过 URL 参数（如 `room.name`、`room.color`）或 Base64 编码的哈希值配置房间属性。  
2. **自建服务器**：需 Docker 和 docker-compose，最低配置为 1GB RAM 和 1GHz CPU，支持 Raspberry Pi、Digital Ocean 等平台部署。  
3. **开发集成**：提供 `jam-core`（JavaScript 库）和 `jam-core-react`（React 组件库）供开发者构建自定义 UI 或机器人。  

**已知问题与解决方案**  
- **音频输出问题**：iPhone 用户建议使用蓝牙耳机避免扬声器切换问题。  
- **后台静音问题**：Android/iOS 用户需在独立浏览器中使用 Jam，而非 WebView。  
- **听音权限**：主持人需手动将参与者从观众区移至舞台区以实现双向语音。  

**其他**  
支持通过 Slack、Wordpress、Webflow、Shopify 等平台集成 Jam，提供早期访问计划（Jam Shelf）用于自建服务器。