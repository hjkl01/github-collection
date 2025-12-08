
---
title: nettu-meet
---

### [fmeringdal nettu-meet](https://github.com/fmeringdal/nettu-meet)

**项目核心内容总结：**  

**功能**：  
- 支持实时音视频通信、共享白板、屏幕共享、聊天、文件上传、数学图表绘制及自定义品牌标识（如上传Logo）。  

**使用方法**：  
1. **本地运行**：  
   - 启动服务器：进入`server`目录，配置环境变量，使用`npm run infra`启动依赖服务（Redis、MongoDB），安装依赖后运行`npm start`。  
   - 启动前端：进入`frontend`目录，执行`npm i`和`npm start`。  
2. **创建会议**：通过`curl`命令向本地服务器发送POST请求生成会议链接。  

**文档与资源**：  
- 提供Swagger API文档（本地地址：`http://localhost:5000/api/v1/docs/`，或在线访问）。  
- 开源许可证为AGPL3。  

**主要特性**：  
专为在线教学设计，支持互动协作与个性化配置。