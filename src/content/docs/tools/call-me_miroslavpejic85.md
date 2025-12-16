
---
title: call-me
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/miroslavpejic85/call-me?style=social) ](https://github.com/miroslavpejic85/call-me)
### [miroslavpejic85 call-me](https://github.com/miroslavpejic85/call-me)

**项目核心内容总结：**

**功能**  
基于WebRTC实现浏览器端点对点视频通话，支持登录、发起通话、实时聊天、摄像头/麦克风/屏幕切换、音频视频控制、挂断通话，提供REST API获取在线用户列表或发起通话。

**使用方法**  
1. **Node.js部署**：克隆代码→配置`config.js`和`.env`→安装依赖→运行`npm start`，访问`http://localhost:8000`。  
2. **Docker部署**：克隆代码→配置`.env`和`docker-compose.yml`→执行`docker-compose up`启动容器。  
3. **快速体验**：通过URL参数直接加入通话（如`http://localhost:8000/join?user=user1`）。  
4. **网页集成**：使用iframe嵌入代码（提供示例链接）。

**主要特性**  
- 支持实时音视频通话、屏幕共享、设备切换。  
- 提供REST API接口（如获取在线用户、生成通话链接）。  
- 支持自托管部署（附文档链接）。  
- 可通过iframe快速集成到第三方网站。