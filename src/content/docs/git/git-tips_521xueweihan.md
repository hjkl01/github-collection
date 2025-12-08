
---
title: git-tips
---

### [521xueweihan git-tips](https://github.com/521xueweihan/git-tips)

该文档是Git操作指南，涵盖常用命令及工作流规范，核心内容包括：

**功能**  
提供Git全流程操作方案，包含分支管理（rebase/stash/clone）、提交规范（Angular提交标准）、文件追踪控制（忽略文件/权限变更）、代理配置（HTTP/SOCKS）、提交信息工具（cz-cli）等。

**使用方法**  
1. 通过`git config`设置代理或忽略规则  
2. 使用`git stash`暂存修改，`git rebase --autostash`自动暂存  
3. 通过`git clone`指定分支或浅层克隆  
4. 使用`git log --grep`搜索提交记录  
5. 采用`cz-cli`工具生成符合Angular规范的提交信息（feat/refactor/fix等类型）

**主要特性**  
- 提交信息标准化（标题/正文/页脚注释结构）  
- 支持分支对比（`git log Branch1 ^Branch2`）  
- 提供文件状态管理（tracked/untracked/ignored文件识别）  
- 包含深度操作（bundle打包/分支导出）  
- 支持代理配置（HTTP/SOCKS协议）