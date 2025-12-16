
---
title: openwrt-passwall
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/xiaorouji/openwrt-passwall?style=social) ](https://github.com/xiaorouji/openwrt-passwall)
### [xiaorouji openwrt-passwall](https://github.com/xiaorouji/openwrt-passwall)

**项目功能**：Passwall 是 OpenWrt 系统中用于实现网络分流的工具，兼容 Xray 和 Sing-box 的分流方式。  

**使用方法**：  
1. **方法1**：在 `feeds.conf.default` 文件顶部添加两个 Git 源（passwall_packages 和 passwall_luci），然后执行 `./scripts/feeds update -a`。  
2. **方法2**：先执行 `./scripts/feeds install -a`，再删除 OpenWrt 自带的旧版本包，克隆指定仓库至 `package/passwall-packages` 和 `package/passwall-luci`。  

**主要特性**：  
- 从 25.3.9 版本起，Sing-box 分流依赖 Geoview 生成规则集，未安装 Geoview 将无法使用该功能。  
- 提供两种编译最新代码的途径，确保与 Sing-box 1.12.0 及以上版本兼容。