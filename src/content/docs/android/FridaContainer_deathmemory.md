
---
title: FridaContainer
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/deathmemory/FridaContainer?style=social) ](https://github.com/deathmemory/FridaContainer)
### [deathmemory FridaContainer](https://github.com/deathmemory/FridaContainer)

**FridaContainer 核心内容总结：**

**项目功能**  
整合多款常用 Frida 脚本，提供 Android/iOS 逆向辅助功能，包括：  
- **Android**：反调试绕过、堆栈打印、Dex 文件提取、SSL Pinning 绕过（支持 Cronet）、JNI Hook、Java 方法追踪、多 Dex 模块 Hook 等。  
- **iOS**：函数地址获取与模糊查找、堆栈打印、UI 结构 Dump、数据类型转换等。  
- **跨平台通用工具**：模块信息查询、堆栈与寄存器值打印、模块转储等功能。

**使用方法**  
1. **源码方式（推荐）**：  
   - 克隆仓库后，修改 `index.ts` 编写逻辑，执行 `npm install` 安装依赖。  
   - 通过 `npm run build` 编译，使用 `frida -U -f <包名> -l _fcagent.js` 注入脚本。  
   - 开发时运行 `npm run watch` 实时编译，配合 PyCharm 等 IDE 编辑脚本。  
   - Android 环境初始化可执行 `setupAndroid.py`。  

2. **npm 模块方式（不推荐）**：当前版本可能存在兼容性问题，建议使用源码方式。

**主要特性**  
- 支持 Frida 17.0+（需使用 `for17` 分支适配 API 变动）。  
- 提供结构化脚本开发流程（如 `agent` 目录管理业务逻辑）。  
- 集成多平台逆向常用功能，提升调试与分析效率。