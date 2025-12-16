
---
title: brave-browser
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/brave/brave-browser?style=social) ](https://github.com/brave/brave-browser)
### [brave brave-browser](https://github.com/brave/brave-browser)

**项目核心内容总结：**  
该项目为构建Brave桌面浏览器的工具链，支持macOS、Windows和Linux平台，集成Chromium源码、Brave核心组件（如广告拦截引擎adblock-rust）及依赖管理。  

**主要功能：**  
- 通过`npm install`和`npm run init`初始化构建环境，自动同步Chromium源码和Brave核心代码。  
- 支持多种构建模式（Component/Release/Static/Debug），适配不同开发和发布需求。  
- 提供`npm run sync`更新依赖库，支持强制同步、分支切换及依赖清理。  

**使用方法：**  
1. 克隆仓库并初始化：`git clone`后执行`npm install`和`npm run init`。  
2. 构建浏览器：`npm run build`（默认Component模式）或指定Release/Static/Debug模式。  
3. 运行：`npm start`启动构建后的浏览器。  
4. 更新：通过`npm run sync`同步代码库，支持参数控制同步范围和深度。  

**主要特性：**  
- 多平台构建支持，适配Android/iOS开发环境。  
- 模块化依赖管理，集成第三方组件（如Rust实现的广告拦截）。  
- 灵活的构建配置（如静态链接优化启动速度）。  
- 提供安全开发规范及社区协作渠道。