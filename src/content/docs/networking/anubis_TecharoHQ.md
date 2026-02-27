
---
title: anubis
---

### [TecharoHQ anubis](https://github.com/TecharoHQ/anubis)  ![GitHub Repo stars](https://img.shields.io/github/stars/TecharoHQ/anubis?style=social)

**项目名称：Anubis（阿努比斯）**

**项目功能：**  
Anubis 是一个用于网络的 AI 防火墙工具，用于保护上游资源免受爬虫机器人的攻击。它通过设置一个或多个“挑战”来验证连接请求，类似于“称量灵魂”的过程，从而过滤掉恶意请求。

**使用方法：**  
用户可将 Anubis 部署在自己的服务器前，作为反爬虫的第一道防线。项目提供了详细的[文档](https://anubis.techaro.lol)，用户可参考进行部署和配置。

**主要特性：**  
1. 轻量级设计，适合中小型网站使用；
2. 支持自定义“机器人策略”，可白名单允许“好机器人”（如互联网档案馆）访问；
3. 提供“已知良好机器人”列表，帮助在可发现性和服务器可用性之间取得平衡；
4. 不依赖 Cloudflare，适合无法或不愿使用 Cloudflare 的情况；
5. 开源项目，支持 GitHub 赞助和社区贡献。

**适用场景：**  
适合希望防止 AI 公司爬虫大规模请求、保护网站资源的个人或组织，尤其适用于没有使用 Cloudflare 的用户。