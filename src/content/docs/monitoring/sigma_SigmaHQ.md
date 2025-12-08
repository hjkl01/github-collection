
---
title: sigma
---

### [SigmaHQ sigma](https://github.com/SigmaHQ/sigma)

**项目核心内容总结：**  
Sigma 是一种用于 SIEM 系统的通用日志事件签名格式，旨在以结构化方式描述检测规则，便于共享和复用。其功能包括：  
- **规则类型**：提供通用检测、威胁狩猎、新兴威胁、合规性及占位符规则，覆盖 3000+ 规则。  
- **使用方法**：通过 [Sigma CLI](https://github.com/SigmaHQ/sigma-cli) 或 [sigconverter.io](https://sigconverter.io) 转换规则；从 [发布页面](https://github.com/SigmaHQ/sigma/releases) 下载规则包；使用 [pySigma](https://github.com/SigmaHQ/pySigma) 集成到工具链。  
- **核心特性**：  
  - 社区协作维护，规则由专业检测工程师同行评审；  
  - 厂商中立，适用于任意日志源；  
  - 支持多 SIEM 平台（如 IBM QRadar、SOC Prime 等）；  
  - 提供 MITRE ATT&CK 对接、合规框架（如 NIST）检测等能力。  

**贡献方式**：通过 GitHub 提交 PR，或使用 [CONTRIBUTING](./CONTRIBUTING.md) 指南提交新规则或反馈问题。