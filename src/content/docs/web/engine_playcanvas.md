
---
title: engine
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/playcanvas/engine?style=social) ](https://github.com/playcanvas/engine)
### [playcanvas engine](https://github.com/playcanvas/engine)

**PlayCanvas 引擎核心内容总结：**

**项目功能**  
PlayCanvas 是一个开源的 HTML5 游戏引擎，基于 WebGL2 和 WebGPU 实现，支持在浏览器中运行 2D/3D 交互内容，适用于开发游戏、广告及可视化应用。

**主要特性**  
- **图形渲染**：支持高级 2D/3D 图形，兼容 WebGPU。  
- **动画系统**：基于状态的动画控制，支持角色及场景属性动画。  
- **物理引擎**：集成 ammo.js 实现 3D 刚体物理模拟。  
- **输入支持**：兼容鼠标、键盘、触摸屏、手柄及 VR 控制器。  
- **音频处理**：基于 Web Audio API 的 3D 空间音效。  
- **资源管理**：支持 glTF 2.0、Draco 和 Basis 压缩格式的异步加载。  
- **脚本开发**：使用 TypeScript 或 JavaScript 编写游戏逻辑。

**使用方法**  
通过 JavaScript 初始化引擎，创建场景实体（如立方体、相机、光源），并绑定更新逻辑。示例包含创建旋转立方体的代码，支持通过 CodePen 线上调试。本地开发需安装 Node.js 18+，执行 `npm install` 后通过 `npm run build` 构建项目。

**其他**  
提供官方编辑器（独立项目），支持跨平台开发，被多家知名公司用于游戏与可视化项目。