
---
title: otclient
---

### [mehah otclient](https://github.com/mehah/otclient)

**核心内容总结：**  
该项目是一个支持多种游戏协议的跨平台客户端（OTClient），主要用于连接TFS（The Forgotten Server）及Canary等游戏服务器。核心功能包括：支持TFS 7.72、TFS 1.5、TFS 1.6及Canary 13.x等协议版本；提供模块化功能如照明系统、路径寻找、商店模块等；适配移动设备（当前支持Android，计划扩展iOS）；支持Docker构建与部署。  

**使用方法：**  
1. **编译**：通过Wiki提供的教程编译Android版本，或使用Docker命令构建镜像并运行容器。  
2. **配置**：根据目标协议版本调整`data/setup.otml`文件中的参数（如`force-new-walking-formula`、`item-ticks-per-frame`）。  
3. **连接**：支持TFS、Nostalrius、OpenTibiaBr等服务器，部分协议需启用特定功能（如`g_game.enableFeature`）。  

**主要特性：**  
- 支持主流游戏协议（TFS 7.72至TFS 1.6、Canary 13.x等），兼容性高。  
- 模块化设计，包含商店、装备、路径寻找等扩展功能。  
- 提供Docker部署方案，简化生产环境构建流程。  
- 移动端适配（Android已实现，iOS待开发），支持LUA代码复用。  
- 开源MIT许可证，允许商业及非商业使用，社区活跃（提供Discord支持及Bug跟踪）。