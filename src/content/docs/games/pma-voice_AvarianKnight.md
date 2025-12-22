
---
title: pma-voice
---

### [AvarianKnight pma-voice](https://github.com/AvarianKnight/pma-voice)  ![GitHub Repo stars](https://img.shields.io/github/stars/AvarianKnight/pma-voice?style=social)

### 项目核心内容总结

**项目功能：**  
pma-voice 是一个基于 FiveM/RedM 内部 Mumble 服务器的语音系统，支持语音聊天、电台和通话模块，提供 2D/3D 音频、子混音（submix）等特性，适用于多人游戏语音交互。

**使用方法：**  
1. **配置**：通过 ConVars 设置音频模式（如 `voice_useNativeAudio`）、默认音量（如 `voice_defaultCallVolume`）、按键绑定（如 `voice_defaultRadio`）等参数。  
2. **API 调用**：客户端和服务器端提供丰富的 API（如 `setRadioChannel`、`getPlayersInRadioChannel`），用于控制语音属性、频道和权限。  
3. **权限管理**：通过 Ace 权限（如 `add_ace group.superadmin command.muteply allow`）控制管理员命令（如 `/muteply`）。  

**主要特性：**  
- 支持 2D/3D 音频与子混音，增强语音沉浸感。  
- 内置 UI 与 proximity（距离）模式切换功能，支持自定义按键。  
- 提供客户端/服务器端事件（如 `pma-voice:radioActive`）和状态管理（如 `Player(source).state.call`），便于第三方集成。  
- 安全性配置：通过 `voice_useSendingRangeOnly` 限制连接范围，防止外挂。  
- 兼容性要求：需禁用其他语音系统（如 vMenu 语音），避免冲突。  

**注意事项：**  
- 不可同时启用 `voice_useNativeAudio`、`voice_use2dAudio`、`voice_use3dAudio`。  
- 禁止覆盖 `NetworkSetTalkerProximity` 等原生函数，否则可能导致功能失效。  
- 配置变更仅对新玩家生效，老玩家需重新加入服务器。