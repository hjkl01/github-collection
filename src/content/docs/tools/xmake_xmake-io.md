
---
title: xmake
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/xmake-io/xmake?style=social) ](https://github.com/xmake-io/xmake)
### [xmake-io xmake](https://github.com/xmake-io/xmake)

**xmake** 是一个跨平台的构建工具，支持多种编程语言（如 C/C++、Zig、Rust 等）和项目类型（库、可执行文件、框架等），提供以下核心功能与特性：  

### **主要功能**  
1. **项目构建与管理**  
   - 支持多种构建模式（调试/发布），自动管理依赖（如 zlib、libogg 等）。  
   - 可生成 IDE 项目文件（Visual Studio、CMake、Ninja、compile_commands 等），适配主流开发环境。  
   - 支持跨平台编译（Windows、Linux、macOS），并可自动获取远程工具链（如 LLVM 10、muslcc 等）。  

2. **依赖与工具链管理**  
   - 自动拉取和集成第三方库及交叉编译工具链，支持自定义配置（如 OpenMP、CUDA 项目）。  
   - 提供 `xrepo` 工具管理依赖包，支持本地或远程仓库。  

3. **插件与扩展**  
   - 内置插件支持生成 IDE 项目、运行 Lua 脚本、集成 Gradle 编译 JNI 库等。  
   - 可通过插件仓库扩展功能（如 xmake-vscode、xmake-idea 等）。  

4. **CI/CD 集成**  
   - 支持 GitHub Actions 等 CI 工具，简化持续集成流程。  

### **使用方法**  
- **项目配置**：通过 `xmake project` 生成 IDE 项目文件。  
- **构建项目**：使用 `xmake build` 编译代码，`xmake install` 安装输出。  
- **运行脚本**：通过 `xmake l` 执行自定义 Lua 脚本（如检测工具链）。  
- **集成开发环境**：支持 VSCode、Sublime Text、IntelliJ 等主流 IDE 的插件集成。  

### **核心特性**  
- 跨平台、多语言支持。  
- 自动获取远程工具链与依赖。  
- 强大的插件系统与 IDE 集成。  
- 支持复杂场景（如 OpenMP、CUDA、JNI）。  
- 社区活跃，提供中文文档与多语言社区支持。