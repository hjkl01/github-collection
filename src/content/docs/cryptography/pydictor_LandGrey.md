
---
title: pydictor
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/LandGrey/pydictor?style=social) ](https://github.com/LandGrey/pydictor)
### [LandGrey pydictor](https://github.com/LandGrey/pydictor)

**pydictor 核心内容总结：**

**项目功能：**  
pydictor 是一款用于生成暴力破解字典的工具，支持多种字典类型（如基础字典、字符组合、扩展规则、社会工程等），提供内置工具处理字典（合并、去重、频率统计等），并支持自定义编码脚本、插件和配置文件，实现高度定制化生成。

**使用方法：**  
1. 克隆仓库：`git clone --depth=1 --branch=master https://www.github.com/landgrey/pydictor.git`  
2. 进入目录并赋予权限：`cd pydictor/ && chmod +x pydictor.py`  
3. 运行脚本：`python pydictor.py`  

**主要特性：**  
- **高度定制化**：通过修改配置文件、添加自定义编码脚本（如 `/lib/encode/`）、插件（`/plugins/`）及工具（`/tools/`）实现复杂字典生成。  
- **多样化生成规则**：支持长度范围、前后缀、正则过滤、leet模式（替代字符）、字符频率/类型/重复次数控制等。  
- **兼容性强**：支持 Python 2.7 及 3.x 版本，跨平台运行（Windows/Linux/Mac）。  
- **内置工具链**：提供合并、对比、去重、编码、混合生成等工具，满足字典预处理需求。  
- **扩展性**：支持插件生成（如生日、身份证尾号、网页关键词等）及多级规则配置（如 `/funcfg/` 中的扩展规则）。