
---
title: roubao
---

### [Turbo1123 roubao](https://github.com/Turbo1123/roubao)  ![GitHub Repo stars](https://img.shields.io/github/stars/Turbo1123/roubao?style=social)

**项目核心内容总结：**

**1. 项目概述**  
"肉包自动导航"是一款安卓自动化工具，通过自然语言指令控制手机操作，结合AI代理（VLM视觉语言模型）与GUI自动化技术，支持打开应用、执行任务等场景。

**2. 核心功能**  
- **智能应用搜索**：支持拼音、语义、分类多维度匹配应用。  
- **双模式操作**：  
  - **Delegation模式**：高置信度指令直接DeepLink跳转（如"打开微信"）。  
  - **GUI自动化模式**：通过截图+AI分析，模拟点击、滑动、输入等操作。  
- **安全限制**：设置操作超时、失败次数限制，防止异常行为。  

**3. 使用方法**  
- 安装Shizuku框架（设备控制依赖）。  
- 配置VLM API密钥（如通义千问等视觉语言模型）。  
- 输入自然语言指令（如"在淘宝搜索手机"），系统自动匹配Skill并执行。  

**4. 主要特性**  
- **原子能力工具层**：封装搜索应用、剪贴板操作、Shell命令等基础功能。  
- **Skill技能层**：预置"打开应用""执行任务"等Skill，支持用户自定义扩展。  
- **日志与调试**：导出操作日志、崩溃信息，便于问题反馈。  
- **无障碍服务混合模式（v2.0开发中）**：结合AccessibilityService实现更精准的UI操作。  

**5. 技术架构**  
- 基于Kotlin开发，模块化设计（Agent、Tools、Skills、UI等）。  
- 依赖Shizuku框架实现设备控制，通过VLMClient调用视觉语言模型。  
- 支持离线使用（v2.0计划加入本地模型）。  

**6. 开发与贡献**  
- 需Android Studio JDK17环境，支持Gradle构建。  
- 开源MIT协议，欢迎提交Issue和Pull Request。