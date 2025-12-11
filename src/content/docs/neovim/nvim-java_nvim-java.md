
---
title: nvim-java
---

### [nvim-java nvim-java](https://github.com/nvim-java/nvim-java)

**项目核心内容总结：**

**功能**  
nvim-java 是一个为 Neovim 提供 Java 开发支持的插件，主要功能包括：  
- Spring Boot 工具集成  
- 代码诊断、自动补全与调试配置  
- 测试运行与调试（支持 Java-Test 和 Java-Debug-Adapter 扩展）  
- 内置应用运行器、日志查看器及配置管理界面  
- 反编译支持与 JDK 自动安装  

**使用方法**  
1. **安装**：通过 `vim.pack` 或 `lazy.nvim` 插件管理器配置依赖。  
2. **配置**：在 `setup()` 中设置 JDK 版本、日志级别、扩展功能（如 Lombok、Spring Boot 工具）等。  
3. **操作**：使用 Neovim 命令（如构建、运行测试、调试）或调用 Lua API（如 `require('java').setup()`）进行开发。  

**主要特性**  
- 支持与 JDTLS（Java 语言服务器）无缝通信，扩展 Java-Test 和 Java-Debug-Adapter 功能。  
- 提供详细的日志记录（支持控制台和文件输出）。  
- 自动安装 JDK 并兼容多版本配置。  
- 通过架构分层设计，实现 Neovim 与 JDTLS、扩展工具的高效协作。