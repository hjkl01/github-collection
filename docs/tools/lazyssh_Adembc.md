### [Adembc lazyssh](https://github.com/Adembc/lazyssh)  ![GitHub Repo stars](https://img.shields.io/github/stars/Adembc/lazyssh?style=social)

Lazyssh 是一款基于终端的交互式 SSH 管理器，通过键盘驱动的 UI 帮助用户直接从终端管理服务器，替代传统命令行操作。

主要功能：
1. 服务器管理：自动读取 ~/.ssh/config，支持在界面中添加、编辑、删除、置顶服务器及 Ping 测试。
2. 快速导航：支持别名、IP 或标签的模糊搜索，提供标签筛选及排序功能。
3. 高级配置：支持端口转发、连接复用、认证选项、安全设置及代理配置。
4. 密钥管理：支持 SSH 密钥自动补全与智能选择。
5. 安全机制：作为 OpenSSH 的 UI 包装器，不存储私钥，配置修改前自动备份并采用原子写入。
6. 计划功能：包含本地与服务器间的文件传输及 SSH 密钥部署。

支持通过 Homebrew、二进制下载或源码构建进行安装。