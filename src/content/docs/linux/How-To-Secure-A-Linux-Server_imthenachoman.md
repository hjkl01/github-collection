
---
title: How-To-Secure-A-Linux-Server
---

### [imthenachoman How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server)  ![GitHub Repo stars](https://img.shields.io/github/stars/imthenachoman/How-To-Secure-A-Linux-Server?style=social)

这是一个提供 Linux 服务器安全加固全面指南的项目。主要内容包括：

1. **SSH 安全配置**：支持密钥认证、双因素认证、配置优化及组权限控制。
2. **系统基础防护**：涵盖 sudo/su 权限限制、强密码策略、自动安全更新、NTP 同步及应用沙盒化。
3. **网络与入侵防御**：集成 UFW 防火墙、PSAD、Fail2Ban 和 CrowdSec 进行入侵检测与阻断。
4. **安全审计与监控**：包含文件完整性监测 (AIDE)、反病毒扫描 (ClamAV)、Rootkit 检测及系统审计工具 (Lynis, OSSEC)。
5. **高级硬ening**：涉及内核参数调整、GRUB 密码保护、Root 登录禁用及无用软件清理。
6. **自动化与支持**：提供 Ansible Playbooks 自动化脚本、邮件告警系统及日志管理配置。

项目目标是通过分步指导和代码片段，帮助用户理解并实施有效的服务器安全措施，主要基于 Debian 测试但适用于大多数 Linux 发行版。