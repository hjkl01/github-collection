
---
title: luci-app-easytier
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/EasyTier/luci-app-easytier?style=social) ](https://github.com/EasyTier/luci-app-easytier)
### [EasyTier luci-app-easytier](https://github.com/EasyTier/luci-app-easytier)

**项目功能**  
luci-app-easytier 是一个 OpenWRT 系统的 LuCI 插件，用于管理 EasyTier 二进制程序。需用户自行上传二进制文件并配置参数。

**使用方法**  
1. **安装依赖**：系统需提前安装 `kmod-tun`。  
2. **编译插件**：  
   - 修改 `.github/workflows/build.yml` 中的 `arch` 和 `sdk` 配置，选择目标架构及 OpenWRT 版本（如 `openwrt-22.03` 生成 ipk 包，`SNAPSHOT` 生成 apk 包）。  
   - 通过 GitHub Actions 触发编译，需填写 release 版本以生成安装包。  
3. **安装插件**：  
   - 使用 `opkg install` 或 `apk add --allow-untrusted` 安装生成的 `.ipk` 或 `.apk` 文件。  
   - 安装后需重启页面或重新登录以显示插件。  
4. **更新插件**：卸载旧版本后安装新版本，修改参数后需重新保存生效。  

**主要特性**  
- 支持 OpenWRT 22.03 及以上版本（需适配 SDK）。  
- 提供编译流程脚本，兼容不同架构（如 aarch64）。  
- 需用户手动上传二进制程序，不包含在插件中。  
- 提供日志错误修复方案（如替换 Lua 文件中的 `util.pcdata` 为 `xml.pcdata`）。