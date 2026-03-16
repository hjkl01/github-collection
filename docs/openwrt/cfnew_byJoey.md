### [byJoey cfnew](https://github.com/byJoey/cfnew)  ![GitHub Repo stars](https://img.shields.io/github/stars/byJoey/cfnew?style=social)

CFnew 是一款基于 Cloudflare Workers 的代理订阅管理工具，核心功能总结如下：

1. **多协议支持**：支持 VLESS、Trojan、xhttp 协议混合部署，可多协议同时启用。
2. **图形化管理**：利用 Cloudflare KV 存储配置，修改后即时生效，无需重新部署。
3. **智能优选与测速**：内置延迟测试工具，支持优选 IP/域名、按地区筛选、延迟排序及自动获取机场码。
4. **多客户端兼容**：支持 CLASH、SURGE、SING-BOX 等十余种客户端，根据 User-Agent 自动识别并适配配置格式。
5. **API 管理**：支持通过 RESTful API 动态添加、删除或清空优选 IP 列表。
6. **高级定制**：支持 ECH 加密握手、自定义路径、节点级 path 参数覆盖（ProxyIP、地区、SOCKS5 等）及订阅转换服务。
7. **自动化服务**：支持每 15 分钟自动优选更新，根据浏览器语言自动切换中文或波斯语界面。