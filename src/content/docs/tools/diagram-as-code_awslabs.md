
---
title: diagram-as-code
---

### [awslabs diagram-as-code](https://github.com/awslabs/diagram-as-code)

### 核心内容总结

**项目功能**  
这是一个基于YAML代码的命令行工具（CLI），用于生成AWS基础设施架构图，无需依赖图像库。支持通过YAML文件实现“代码即图表”，可与Git集成，便于版本管理和协作。提供从CloudFormation模板生成图表的Beta功能，但需注意准确性限制。

**使用方法**  
- **安装**：Go用户通过`go install`安装，macOS用户通过`brew install awsdac`安装。  
- **基本用法**：执行`awsdac <输入文件> [参数]`，支持输出文件名、模板处理、CloudFormation模板生成图表等。  
- **Beta功能**：使用`--cfn-template`从CloudFormation模板生成图表，或通过`--dac-file`生成自定义YAML文件后输入`awsdac`生成图表。

**主要特性**  
1. **符合AWS架构规范**：遵循AWS图标指南生成图表。  
2. **灵活布局**：自动调整组的位置和大小。  
3. **轻量高效**：无需依赖浏览器或GUI，适合CI/CD流程。  
4. **与IaC集成**：与基础设施即代码（如CloudFormation）结合，生成图表与代码保持一致。  
5. **可扩展性**：支持自定义定义文件，可生成非AWS图表。  
6. **MCP服务器集成**：通过Model Context Protocol（MCP）与AI工具、开发工具集成，实现程序化图表生成。

**注意事项**  
- CloudFormation模板生成图表功能为Beta，可能存在不准确问题。  
- 使用`--dac-file`可将CloudFormation模板转换为自定义YAML文件，再通过`awsdac`生成图表。  
- 支持通过MCP客户端配置服务器，生成图表并保存到指定路径。  
