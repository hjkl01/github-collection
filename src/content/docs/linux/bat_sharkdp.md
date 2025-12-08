
---
title: bat
---

### [sharkdp bat](https://github.com/sharkdp/bat)

**bat工具核心内容总结：**  
bat是一款用于替代POSIX `cat`命令的工具，提供以下功能：  
1. **高级语法高亮**：支持多种编程语言的语法突出显示，可自定义主题（如TwoDark、GitHub等）和样式（如显示行号、Git修改标记等）。  
2. **Git集成**：可显示文件的Git修改状态（新增、删除、修改）。  
3. **跨平台支持**：兼容Windows、Linux、macOS，支持通过配置文件自定义设置（如主题、样式、语法映射）。  
4. **用户友好**：提供命令行选项（如`--theme`、`--style`）和配置文件（`bat.conf`）灵活调整行为。  
5. **特殊处理**：支持处理ANSI转义序列（如`--strip-ansi`）、UTF-8/UTF-16编码文件，Windows下需安装`less`分页器或配置路径兼容性。  

**使用方法**：  
- 基础命令：`bat [文件]`，默认显示语法高亮和Git信息。  
- 自定义：通过`--theme`设定主题，`--style`设定显示样式（如`numbers,changes,header`），`--map-syntax`映射文件扩展名到特定语法（如`--map-syntax "*.ino:C++"`）。  
- 配置文件：创建`bat.conf`定义默认参数，支持注释和多行配置。  

**主要特性**：  
- 支持24位真彩色终端，兼容8位色主题。  
- 可禁用分页（`--paging=never`）或自定义分页器（如`less`）。  
- 提供Windows下Cygwin路径转换的脚本解决方案。  
- 开源，采用MIT或Apache 2.0许可证，支持通过Cargo构建和安装。