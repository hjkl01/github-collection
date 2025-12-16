
---
title: FerretDB
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/FerretDB/FerretDB?style=social) ](https://github.com/FerretDB/FerretDB)
### [FerretDB FerretDB](https://github.com/FerretDB/FerretDB)

**FerretDB 核心内容总结：**

**项目功能**  
FerretDB 是一个开源的 MongoDB 替代品，作为代理将 MongoDB 5.0+ 协议转换为 SQL，并使用 PostgreSQL（集成 DocumentDB 扩展）作为数据库引擎，实现 MongoDB 与 PostgreSQL 的兼容性转换。

**使用方法**  
1. **Docker 快速启动**：通过指定 PostgreSQL 用户和密码运行 Docker 镜像，即可启动 FerretDB 服务。  
   示例命令：  
   ```sh
   docker run -d --rm --name ferretdb -p 27017:27017 \
     -e POSTGRES_USER=<username> \
     -e POSTGRES_PASSWORD=<password> \
     ghcr.io/ferretdb/ferretdb-eval:2
   ```  
2. **连接方式**：  
   - 使用 MongoDB 客户端连接（URI：`mongodb://<username>:<password>@127.0.0.1:27017/`）。  
   - 通过 MongoDB Shell 或 PostgreSQL 客户端访问容器内的数据库。  
3. **其他方式**：提供 Linux 二进制文件、包管理安装及 Go 库集成选项。

**主要特性**  
- **兼容性**：支持 MongoDB 驱动和工具，可作为 MongoDB 5.0+ 的替代方案。  
- **开源免费**：避免 MongoDB 的 SSPL 许可限制，适用于开源和商业项目。  
- **性能扩展**：持续增加功能以提升兼容性与性能。  
- **云服务支持**：提供 FerretDB Cloud、Civo、Tembo 等云平台托管方案。  

**注意事项**：Docker 示例仅用于测试，生产环境需使用官方安装指南部署。