
---
title: luci-app-easytier
---

### [EasyTier luci-app-easytier](https://github.com/EasyTier/luci-app-easytier)  ![GitHub Repo stars](https://img.shields.io/github/stars/EasyTier/luci-app-easytier?style=social)

`luci-app-easytier` 是 OpenWrt 的 LuCI 插件，用于通过 Web 界面配置和管理 EasyTier 虚拟组网服务。该插件依赖 `kmod-tun` 模块，不包含 EasyTier 二进制程序，需用户手动上传。支持通过 GitHub Actions 自动编译或本地 SDK 构建，可使用 `opkg` 或 `apk` 进行安装部署，并提供了解决 uhttpd 日志报错的修复命令。