
---
title: VCPToolBox
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/lioensky/VCPToolBox?style=social) ](https://github.com/lioensky/VCPToolBox)
### [lioensky VCPToolBox](https://github.com/lioensky/VCPToolBox)

**VCP项目核心内容总结：**

VCP是一个用于构建和管理AI代理（Agent）的框架，核心功能包括：  
1. **模块化系统提示词工程**：通过`Tar*`变量实现动态提示词组合，支持时间、天气、工具列表等实时信息注入，提升AI对环境和任务的适应性。  
2. **插件集成与工具调用**：内置文生图、计算器、联网搜索、B站视频获取等工具，通过占位符（如`{{VCPFluxGen}}`）实现AI对工具的自动调用。  
3. **Agent协作机制**：支持Agent间自主通信、任务分配与协同，通过标准化通信总线（ACB）实现团队式智能协作。  
4. **动态变量系统**：包含`Tar*`（高优先级模板）、`Var*`（通用变量）、`Sar*`（模型适配变量），支持复杂场景下的灵活配置。  
5. **主动交互能力**：集成`AgentMessage`和WebSocket，允许AI根据条件主动通知用户或执行动作。  

**使用方法**：  
- 在`config.env`中定义`Tar*`模块和变量；  
- 通过组合`Tar*`模块生成系统提示词（如`{{Nova}}{{VCPTavern::dailychat}}`）；  
- 调用插件工具时，使用预定义占位符注入功能。  

**主要特性**：  
- 高度可定制的提示词工程；  
- 实时环境感知与工具调用；  
- 支持Agent自主协作与主动交互；  
- 开放的插件生态与未来扩展方向（如深度记忆回溯、事件总线等）。  

项目采用CC BY-NC-SA 4.0许可证，适用于非商业场景，需注意API成本及安全责任。