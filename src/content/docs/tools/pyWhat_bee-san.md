
---
title: pyWhat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/bee-san/pyWhat?style=social) ](https://github.com/bee-san/pyWhat)
### [bee-san pyWhat](https://github.com/bee-san/pyWhat)

**项目核心内容总结：**

**功能**  
`pywhat` 是一个用于识别文本或文件中隐藏信息的工具，可快速识别域名、URL、邮箱、API密钥、加密货币地址、漏洞信息（如SSN、信用卡号）等结构化数据，支持递归扫描文件/目录。

**使用方法**  
- 安装：`pip3 install pywhat` 或 `brew install pywhat`  
- 基础用法：`what "文本内容"` 或 `what 文件路径`  
- 高级功能：  
  - 过滤识别结果（如 `--include "Bug Bounty"`）  
  - 排序输出（如 `--sort rarity`）  
  - 导出为JSON（`--json > 文件.json`）  
  - 支持正则表达式自定义规则  

**主要特性**  
1. **多场景支持**：分析恶意软件（如Wannacry）、抓取网络流量（pcap文件）、挖掘漏洞赏金（API密钥泄露）。  
2. **智能识别**：自动识别文件内容中的结构化数据，支持字符串内信息匹配（边界模式）。  
3. **灵活过滤**：通过标签（如 `--tags`）组合过滤条件（如 `--exclude "Ripple Wallet"`）。  
4. **扩展性**：支持开发者添加自定义正则表达式规则。  
5. **API接口**：提供API供集成调用。  

**适用场景**  
安全研究人员、渗透测试人员、开发人员用于快速定位敏感信息、分析恶意文件或挖掘漏洞赏金。