
---
title: Mindustry
---

### [Anuken Mindustry](https://github.com/Anuken/Mindustry)

**项目核心内容总结：**  
Mindustry 是一款用 Java 编写的自动化塔防策略游戏（RTS），支持多平台运行（桌面、服务器、Android）。  

**主要功能与特性：**  
- 提供自动化战斗与资源管理机制，结合塔防与即时战略玩法。  
- 支持跨平台开发与运行，包括桌面（Windows/Linux/Mac）、服务器及 Android。  
- 项目代码包含动态生成的类（如 `mindustry.gen` 包），这些类由构建过程自动生成，不可手动编辑。  

**使用方法：**  
1. **构建依赖**：需安装 JDK 17，通过 Gradle 命令构建（如 `gradlew desktop:run` 运行桌面版）。  
2. **平台适配**：  
   - 桌面：使用 `gradlew desktop:dist` 生成可执行文件。  
   - 服务器：替换命令中的 `desktop` 为 `server`。  
   - Android：需配置 Android SDK，运行 `gradlew android:assembleDebug` 生成 APK。  
3. **调试**：连接设备后，可通过 `gradlew android:installDebug android:run` 进行调试。  

**其他信息：**  
- 项目提供 Wiki、Trello 任务看板及 Discord 社区支持。  
- 功能扩展建议通过 [Mindustry-Suggestions](https://github.com/Anuken/Mindustry-Suggestions) 仓库提交。  
- 可通过 Itch.io、Google Play 等平台下载已发布版本。