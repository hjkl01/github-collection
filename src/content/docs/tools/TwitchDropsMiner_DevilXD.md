
---
title: TwitchDropsMiner
---

### [DevilXD TwitchDropsMiner](https://github.com/DevilXD/TwitchDropsMiner)  ![GitHub Repo stars](https://img.shields.io/github/stars/DevilXD/TwitchDropsMiner?style=social)

**项目核心内容总结：**

**功能**  
Twitch Drops Miner 是一款用于自动挖掘 Twitch Drops 奖励的工具，无需手动切换频道或观看直播内容，通过获取直播元数据模拟观看行为，节省带宽。支持自动发现活动、管理游戏优先级列表、保存登录信息等功能。

**使用方法**  
1. 下载并解压最新版本，运行程序后通过内置登录表单绑定 Twitch 账号。  
2. 登录后选择目标游戏加入优先级列表，点击“Reload”开始挖掘。  
3. 程序会自动切换频道（如当前频道下线或更高优先级游戏上线）。  

**主要特性**  
- 无需实际观看直播，仅通过元数据模拟观看，节省流量；  
- 支持游戏优先级排序、黑名单过滤；  
- 最多可同时跟踪 199 个频道；  
- 自动发现绑定账号的活动，验证直播标签与奖励资格；  
- 登录信息保存在 `cookies.jar` 文件中；  
- 自动启动新活动、停止无奖励挖掘；  
- 支持 Windows 和 Linux 系统（Linux 版本包含 AppImage 和 PyInstaller 两种格式）。  

**注意事项**  
- 同一账号勿在浏览器或其他工具中观看直播，可能干扰进度；  
- `cookies.jar` 文件需妥善保管，防止账号泄露；  
- Linux 版本依赖 `glibc>=2.35` 和显示服务器；  
- Windows 可能被误报为病毒，可忽略或自行编译源码运行。