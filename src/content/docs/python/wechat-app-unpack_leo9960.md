
---
title: wechat-app-unpack
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/leo9960/wechat-app-unpack?style=social) ](https://github.com/leo9960/wechat-app-unpack)
### [leo9960 wechat-app-unpack](https://github.com/leo9960/wechat-app-unpack)

**项目核心内容总结：**  
该项目为微信小程序解包工具集合，提供多种语言版本（Python2/3、PHP、Java、Node.js、Kaitai Struct），可提取小程序中的页面配置（`app-config.json`）、JS源码（`app-service.js`）、WXML文件（`page-frame.html`）等资源。  

**使用方法：**  
1. 下载对应语言的解包工具，通过工具解压`.wxapkg`文件；  
2. 使用`page-frame.html`配合`ana.js`解析WXML文件：  
   - 引入`ana.js`，替换`page-frame.html`中的函数；  
   - 在浏览器控制台运行`$gwx("...wxml地址...")()`解析单个文件，或`$gwx("ana")()`解析所有文件。  

**主要特性：**  
- 支持解析多种微信小程序版本（如`v0.6vv_20170905_fbi_wxs`等）；  
- 可还原WXML结构（支持`{{}}`变量、`wx:for`、`block`等语法），但无法解析`template`模板及`wx:if`组件；  
- 提供在线分析器（需自行提交版本信息以扩展支持）。  

**注意事项：**  
- `app-service.js`中包含第三方JS代码，不同小程序内容可能不同；  
- `page-frame.html`解析存在局限，需手动调整函数以适配特定版本。