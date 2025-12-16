
---
title: blizzless-diiis
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/blizzless/blizzless-diiis?style=social) ](https://github.com/blizzless/blizzless-diiis)
### [blizzless blizzless-diiis](https://github.com/blizzless/blizzless-diiis)

**项目核心内容总结：**  

**功能**：DiIiS 是《暗黑破坏神3：复仇者之魂》的开源本地服务器，支持账户创建、角色大厅、聊天系统、公会系统、DRLG地牢生成、物品生成、全职业技能机制、套装系统、剧情任务脚本、冒险模式和挑战模式等，但移除了Donate Store功能。  

**使用方法**：  
1. **数据库准备**：安装 PostgreSQL 9.5.25，创建 `diiis` 和 `worlds` 数据库，通过配置文件设置账号密码并导入备份数据，或使用 Docker 部署。  
2. **编译运行**：安装 .NET 7 SDK，执行 `dotnet publish` 命令生成发布文件，修改配置文件中的 IP 地址后运行服务器。  
3. **客户端设置**：使用支持的客户端版本（2.7.4.84161），安装证书并修改 hosts 文件或游戏文件，将连接指向本地服务器。  

**主要特性**：  
- 实现 Necromancer 类机制、80% 小怪 AI、50% 怪物 AI 和部分 Boss AI。  
- 支持 LAN 玩法，可创建公共游戏房间。  
- 包含基础的剧情任务脚本和冒险模式生成器。  
- 限制：未实现 Donate Store 功能。  

**系统要求**：最低需 4GB 内存、500MB 硬盘空间，推荐 16GB 内存及更高配置。