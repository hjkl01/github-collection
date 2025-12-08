
---
title: Beyond-All-Reason
---

### [beyond-all-reason Beyond-All-Reason](https://github.com/beyond-all-reason/Beyond-All-Reason)

**核心内容总结：**

Beyond-All-Reason（BAR）是一款基于Recoil RTS引擎开发的开源即时战略游戏。项目包含两个主要部分：游戏代码（当前仓库）和大厅/启动器（Chobby）。  

**使用方法：**  
1. **玩家**：通过官网下载安装包（https://www.beyondallreason.info/download）即可游玩，操作指南见https://www.beyondallreason.info/guides。  
2. **开发者**：  
   - 安装BAR大厅（可通过官网下载或开发Chobby）。  
   - 在BAR安装目录中创建`devmode.txt`文件，并将游戏代码克隆至`data/games/`目录下的以`.sdd`结尾的文件夹（如`BAR.sdd`）。  
   - 启动游戏后，在设置中选择“Beyond All Reason Dev”模式，即可使用本地开发代码进行测试。  

**主要特性：**  
- 开源，基于Recoil引擎（https://github.com/beyond-all-reason/spring）。  
- 支持自定义开发，通过`.sdd`目录结构兼容Spring引擎的LUA脚本规范。  
- 开发流程需依赖Chobby大厅（https://github.com/beyond-all-reason/BYAR-Chobby），可同时开发游戏和大厅客户端。