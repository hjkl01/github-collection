### [google-maps-scraper](https://github.com/gosom/google-maps-scraper) ![GitHub Repo stars](https://img.shields.io/github/stars/gosom/google-maps-scraper?style=social)

这是一个开源免费的 Google Maps 数据采集工具（MIT 许可），可通过 **CLI、Web UI、REST API** 及可选自托管 SaaS 方式运行，用于批量抓取商家线索与本地商业数据。  
核心能力包括：采集商家名称、分类、地址、电话、网站、评分、评论数、坐标、营业状态、图片、菜单、预订链接等 **33+ 字段**，并可选抓取商家网站邮箱与扩展评论。  
支持 **CSV/JSON/PostgreSQL/S3/LeadsDB/自定义插件** 等多种输出，内置 **代理轮换（SOCKS5/HTTP/HTTPS）**、并发控制、网格区域抓取、快速模式、分布式部署（PostgreSQL + Kubernetes）和实验性 AWS Lambda 支持。  
工具面向线索挖掘、销售拓客、数据补全和自动化场景，性能约 **120 条地点/分钟**（典型配置），并可与 AI 编码代理集成实现“自然语言下发抓取任务”。