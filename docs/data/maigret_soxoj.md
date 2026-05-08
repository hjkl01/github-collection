### [maigret](https://github.com/soxoj/maigret) ![GitHub Repo stars](https://img.shields.io/github/stars/soxoj/maigret?style=social)

Maigret 是一款基于用户名的人物信息收集（OSINT）工具，无需 API Key，可在 3000+ 网站中检索账号并从页面/API提取公开信息。默认扫描流量最高的 500 个站点，也可全量扫描或按标签（类别、国家）筛选。

核心功能包括：账号信息提取与关联账号发现、基于新发现用户名/ID的递归搜索、用户名变体生成搜索、页面解析触发扩展搜索、对封锁/审查/CAPTCHA 的部分绕过、支持代理/Tor/I2P 与域名检查。内置站点数据库可自动从 GitHub 更新（离线时回退本地库）。

支持命令行与 Web 界面两种使用方式；可输出 HTML、PDF、XMind、JSON/NDJSON、CSV、TXT、交互式图谱等报告；也可作为 Python 异步库嵌入到自定义项目和工作流中。支持 pip、源码、Docker、Windows 可执行文件及云端环境运行。项目采用 MIT 许可证。