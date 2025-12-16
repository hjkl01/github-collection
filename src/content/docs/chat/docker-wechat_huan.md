
---
title: docker-wechat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/huan/docker-wechat?style=social) ](https://github.com/huan/docker-wechat)
### [huan docker-wechat](https://github.com/huan/docker-wechat)

**项目核心内容总结：**  
该项目通过Docker容器在Linux系统上运行微信PC客户端，支持Debian、Ubuntu、openSUSE等发行版。  

**功能：**  
- 在Linux桌面运行微信PC客户端，支持消息、文件传输、小程序等功能。  
- 提供多版本微信客户端选择（如2.8.0.112、3.3.0.115等）。  

**使用方法：**  
1. 安装Docker及依赖（如Wine、X11转发支持）。  
2. 执行Shell脚本启动容器，通过环境变量配置DPI缩放、微信版本等参数。  

**主要特性：**  
- 支持多显示器配置，可通过脚本调整显示器布局避免窗口显示异常。  
- 提供`DOCHAT_DPI`环境变量自定义屏幕分辨率缩放比例。  
- 支持通过`DOCHAT_WECHAT_VERSION`选择不同版本的微信客户端。  
- 修复了声音、升级过程异常退出等问题。  

**注意事项：**  
- 需安装`xhost`并执行`xhost +`允许X服务器连接。  
- GNOME桌面用户需安装“TopIcons Plus Git”扩展显示系统托盘图标。  
- 多显示器启动时需先单显示器运行，再调整布局，避免窗口位置异常。