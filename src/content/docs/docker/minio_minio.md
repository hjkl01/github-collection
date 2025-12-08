
---
title: minio
---

### [minio minio](https://github.com/minio/minio)

**核心内容总结：**  
MinIO 是一个高性能、S3 兼容的对象存储解决方案，适用于 AI/ML、分析和大数据工作负载，采用 GNU AGPLv3 许可证。其主要特性包括：S3 API 兼容性、高吞吐量设计、支持大规模数据管道。  

**使用方法：**  
1. **从源码安装**：需 Go 1.24+ 环境，执行 `go install github.com/minio/minio@latest`，通过 `minio server PATH` 启动服务。  
2. **构建 Docker 镜像**：需先构建源码，使用 `docker build` 命令生成镜像，再通过 `docker run` 启动容器。  
3. **Helm Chart 安装**：支持通过 Kubernetes Helm Chart 或 MinIO Operator 部署。  

**注意事项：**  
- 社区版仅提供源码，不再提供预编译二进制文件，历史版本不再维护。  
- 项目处于维护模式，不接受新功能或 PR，仅处理关键安全修复。  
- 生产环境使用源码构建的二进制文件需自行承担风险，AGPLv3 许可证无任何 warranties。  
- 企业用户可联系获取 MinIO AIStor 的商业支持版本。  

**其他信息：**  
- 提供 MinIO Console（Web 界面）和 `mc` 命令行工具进行测试和管理。  
- 文档、SDK 和社区支持可通过官网和 Slack 获取。