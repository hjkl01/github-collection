
---
title: TabPy
---

### [tableau TabPy](https://github.com/tableau/TabPy)

**TabPy核心内容总结：**  
TabPy是Tableau的Python服务器，作为分析扩展实现，允许用户通过Tableau的表计算执行Python脚本和预存函数，扩展Tableau的数据分析能力。  

**功能与使用方法：**  
- 提供安装、配置、虚拟环境部署及Heroku部署指南；  
- 支持在Tableau中编写Python计算逻辑；  
- 包含工具文档和REST API接口；  
- 提供安全配置选项（如启用认证以防止远程代码执行风险）。  

**主要特性：**  
- 兼容多版本Python（通过PyPI支持）；  
- 开源MIT许可证；  
- 自动化测试与代码覆盖率检查；  
- 提供中文文档和社区支持资源（如教程、论坛）。  

**安全注意事项：**  
默认未启用认证，需在配置中强制开启认证，避免潜在的远程代码执行漏洞。