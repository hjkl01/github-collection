
---
title: kaiju
---

### [KaijuEngine kaiju](https://github.com/KaijuEngine/kaiju)

**Kaiju Engine 核心内容总结：**  
Kaiju 是一个基于 Vulkan 的 2D/3D 游戏引擎，使用 Go 语言开发，支持 Windows、Linux、Android（Mac 开发中），具备本地 AI 交互功能。引擎以高性能著称，宣称在相同硬件下性能为 Unity 的 3.4 倍（如 5400 FPS 运行基础场景），内存占用更低，构建速度更快。  

**主要特性：**  
- 采用 Go 语言实现，兼顾系统级性能与开发简洁性，支持 Lua 模组扩展；  
- 通过合理设计减少 GC 压力，实现运行时零堆分配；  
- 强调跨平台兼容性（Android 已支持，Mac 开发中）；  
- 引擎本身已具备生产级稳定性，但编辑器仍在开发中。  

**使用方法：**  
- Windows 用户需安装 64 位 Go 工具链（不支持 32 位）；  
- 参考官方文档（[kaijuengine.org](https://kaijuengine.org)）编译源码；  
- 通过 GitHub、Discord 或 Twitter 获取最新动态及社区支持。