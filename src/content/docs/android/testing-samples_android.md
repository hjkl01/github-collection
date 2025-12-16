
---
title: testing-samples
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/android/testing-samples?style=social) ](https://github.com/android/testing-samples)
### [android testing-samples](https://github.com/android/testing-samples)

**项目核心内容总结：**

1. **项目功能**  
   提供多种Android自动化测试框架的示例代码，涵盖Espresso、UiAutomator、AndroidJUnitRunner等，展示测试技巧（如自定义匹配器、RecyclerView操作、多窗口测试等）。

2. **使用方法**  
   - **构建要求**：需Android SDK v28及Build Tools v28.03。  
   - **Gradle构建**：通过`./gradlew assemble`编译项目，使用`connectedAndroidTest`运行设备测试，`test`执行本地单元测试。  
   - **Bazel支持（实验性）**：需安装Bazel 0.12.0+，通过`bazel test`命令运行测试，支持无GUI模式及本地设备测试。

3. **主要特性**  
   - 支持多种测试框架（Espresso、UiAutomator等）及高级功能（如IdlingResource同步、截图保存）。  
   - 提供AndroidX测试库的集成示例。  
   - 包含针对不同场景的示例（如服务测试、多进程测试、参数化测试）。  
   - 支持Bazel构建，适配CI环境及本地设备测试。