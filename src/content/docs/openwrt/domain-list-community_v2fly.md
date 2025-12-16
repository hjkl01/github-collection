
---
title: domain-list-community
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/v2fly/domain-list-community?style=social) ](https://github.com/v2fly/domain-list-community)
### [v2fly domain-list-community](https://github.com/v2fly/domain-list-community)

**核心内容总结：**  
该项目用于管理域名列表，生成路由规则供Project V使用，不涉及对域名的立场判断。用户可通过下载预生成的`dlc.dat`文件或手动编译生成，按需配置路由策略。  

**使用方法：**  
1. **下载文件**：直接获取`dlc.dat`及校验文件。  
2. **手动生成**：安装Go语言环境，克隆项目后运行`go run ./`生成`dlc.dat`。  
3. **配置示例**：在路由规则中引用`geosite:filename`格式的域名分类（如`geosite:category-ads-all`）。  

**主要特性：**  
- **数据结构**：域名分类存储于`data`目录，支持`include`（文件包含）、`domain`（子域名）、`keyword`（关键词）、`regexp`（正则表达式）、`full`（完整域名）等语法。  
- **规则生成**：自动将文件内容转换为V2Ray路由规则（如子域名匹配、正则匹配等）。  
- **文件命名与属性**：文件名建议明确分类（如`google`），域名可附加属性（如`@ads`）以细分用途，支持`geosite:filename@属性`调用。