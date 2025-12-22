
---
title: CloudflareSpeedTest
---

### [XIU2 CloudflareSpeedTest](https://github.com/XIU2/CloudflareSpeedTest)  ![GitHub Repo stars](https://img.shields.io/github/stars/XIU2/CloudflareSpeedTest?style=social)

**项目核心内容总结：**  
CloudflareSpeedTest（CFST）是一款用于测试并选择最优Cloudflare CDN节点的工具，可加速访问使用Cloudflare服务的网站。  

**主要功能：**  
1. **性能测试**：支持测试Cloudflare IP的延迟、带宽，自动筛选最优节点。  
2. **Hosts管理**：自动更新Hosts文件，将域名解析指向最优CDN节点，无需手动修改。  
3. **多平台支持**：提供Windows/Linux版本，支持安卓、OpenWrt路由器等衍生项目。  
4. **自定义配置**：允许用户自定义下载测速地址、IP范围及测试参数。  

**使用方法：**  
- 命令行运行工具，通过参数（如`-t`测试模式、`-u`更新Hosts）控制功能。  
- 支持手动输入IP或自动从Cloudflare官方列表获取节点。  

**主要特性：**  
- 识别并排除无效IP（如回源IP）。  
- 提供多种下载测速地址选择，提升稳定性。  
- 支持交叉网络环境测试（如切换手机流量排查问题）。  
- 开源，基于GPL-3.0许可证，提供手动编译方式。  

**注意事项：**  
- 部分IP可能因网络策略无法建立HTTP连接，需多尝试不同节点。  
- 自动更新Hosts功能需用户授权，确保安全。