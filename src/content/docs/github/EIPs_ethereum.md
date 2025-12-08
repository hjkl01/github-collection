
---
title: EIPs
---

### [ethereum EIPs](https://github.com/ethereum/EIPs)

**项目核心内容总结：**  
EIPs（以太坊改进提案）项目旨在标准化和规范以太坊协议及其应用层标准，通过EIP文档记录协议改进和相关技术规范。EIPs分为核心协议改进、网络层、接口标准、ERC（应用层标准）、元提案及信息类提案等类别，所有提案需通过社区讨论（如Ethereum Magicians或Ethereum Research）并遵循EIP-1流程提交。  

**使用方法：**  
1. 提交EIP前需在指定社区讨论并达成共识，按EIP-1规则撰写提案；  
2. 通过GitHub提交PR时，需通过自动化验证（如eip-review-bot、eipw工具检查格式与规范）；  
3. 构建本地状态页面需安装Ruby、Bundler及Jekyll，执行`bundle exec jekyll serve`启动本地服务器预览。  

**主要特性：**  
- 严格验证流程：自动检查格式、拼写、链接及EIP-1合规性；  
- 分类管理：按功能划分提案类型（如核心协议、ERC等），明确适用范围；  
- 开放协作：通过GitHub社区参与提案讨论与修改，支持编辑者申请（EIP-5069）。