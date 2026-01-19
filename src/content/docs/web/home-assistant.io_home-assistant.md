
---
title: home-assistant.io
---

### [home-assistant home-assistant.io](https://github.com/home-assistant/home-assistant.io)  ![GitHub Repo stars](https://img.shields.io/github/stars/home-assistant/home-assistant.io?style=social)

**项目核心内容总结：**  
该项目是Home Assistant官网的源代码，用于构建和维护[Home-Assistant.io](https://home-assistant.io)网站。  

**主要功能与特性：**  
1. **多环境部署**：通过不同分支（`current`、`rc`、`next`）分别对应生产环境、测试版和开发版网站，地址分别为：  
   - 生产环境：https://www.home-assistant.io  
   - 测试版：https://rc.home-assistant.io  
   - 开发版：https://next.home-assistant.io  
2. **本地预览**：使用`bundle exec rake preview`命令可在本地启动网站预览（默认地址`http://127.0.0.1:4000`），并支持自定义IP地址。  
3. **加速生成**：通过`rake isolate[文件名]`临时隔离未修改的博客文章以提升生成速度，完成后用`rake integrate`恢复所有内容。  

**使用方法：**  
- 贡献者需参考[开发者文档](https://developers.home-assistant.io/docs/documenting/)设置环境并提交PR。  
- 每个PR的Netlify预览链接会通过评论提供。