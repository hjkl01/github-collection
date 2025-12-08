
---
title: Magisk
---

### [topjohnwu Magisk](https://github.com/topjohnwu/Magisk)

**项目核心内容总结：**  
Magisk 是一款用于自定义 Android 系统的开源工具套件，支持 Android 6.0 及以上设备。其主要功能包括：  
- **MagiskSU**：为应用提供 root 权限；  
- **Magisk 模块**：通过模块安装修改只读分区；  
- **MagiskBoot**：解包和重新打包 Android 启动镜像；  
- **Zygisk**：在所有 Android 应用进程中运行代码。  

**使用方法**：  
通过 [GitHub 发布页面](https://github.com/topjohnwu/Magisk/releases) 下载官方版本，安装说明详见 [官方文档](https://topjohnwu.github.io/Magisk/install.html)。  

**注意事项**：  
- Bug 报告需使用调试版本，并上传对应日志（如 boot image、logcat 或 dmesg）；  
- 翻译需修改 `app/core/src/main/res/values/strings.xml` 等文件中的字符串资源；  
- 项目遵循 GNU GPL v3 协议。