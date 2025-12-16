
---
title: hooker
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/CreditTone/hooker?style=social) ](https://github.com/CreditTone/hooker)
### [CreditTone hooker](https://github.com/CreditTone/hooker)

### 项目核心内容总结

#### **功能概述**
1. **逆向分析工具集**  
   - 提供多种Frida脚本，用于绕过反调试（如检测Frida Server、Root、VPN）、SSL Pinning、动态脱壳、加密算法分析（AES/RSA/HMAC）、WebView调试等。
   - 支持识别Android应用加固壳（如爱加密、梆梆等）及动态脱壳。
   - 可劫持Native层函数（如`dlsym`、`pthread_create`），对抗反调试机制。

2. **设备与应用分析**  
   - 获取设备指纹信息（Android ID、IMEI、传感器数据、系统状态等）。
   - 列出已安装应用及系统状态。

3. **网络与数据抓包**  
   - 绕过SSL证书验证（支持BoringSSL自定义验证函数劫持）。
   - 记录SSL握手过程（`CLIENT_RANDOM`），配合抓包工具还原明文数据。

4. **调试与监控**  
   - 跟踪Activity生命周期、TextView/TextView内容、Native方法调用栈。
   - 监控WebView初始化及JavaScript执行。

---

#### **使用方法**
1. **环境准备**  
   - 安装WSL（推荐Ubuntu 24.04），配置代理（如需）。
   - 安装Python 3.8及依赖（`build-essential`、`libssl-dev`等）。

2. **工具部署**  
   - 将自定义`frida-server`文件放入`mobile-deploy`目录，并修改`hooker.py`中默认文件名。
   - 使用`hooker.py`脚本执行目标功能（如`spawn/attach`指定脚本）。

3. **典型命令**  
   - `spawn dump_dex.js`：脱壳。
   - `attach get_device_info.js`：获取设备信息。
   - `spawn find_boringssl_custom_verify_func.js`：绕过SSL Pinning。

---

#### **主要特性**
- **多场景覆盖**：支持Android逆向、网络抓包、反调试绕过、加密分析等。
- **动态劫持能力**：可修改Native函数行为（如劫持`dlsym`、修改SSL验证逻辑）。
- **兼容性强**：适配多种加固壳、加密算法及Android版本。
- **设备信息全面**：提供设备指纹、传感器、系统状态等详细数据。