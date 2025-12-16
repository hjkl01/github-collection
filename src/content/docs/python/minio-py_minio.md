
---
title: minio-py
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/minio/minio-py?style=social) ](https://github.com/minio/minio-py)
### [minio minio-py](https://github.com/minio/minio-py)

**核心内容总结：**  
MinIO Python SDK 是用于访问 MinIO 对象存储或其他 Amazon S3 兼容云存储服务的高级 API 工具。  

**功能与使用方法：**  
1. **安装方式**：支持通过 `pip3 install minio` 安装，或从 GitHub 源码编译安装。  
2. **连接配置**：通过 `Minio()` 方法创建客户端，需提供服务地址（`endpoint`）、访问密钥（`access_key`）和密钥（`secret_key`）。  
3. **示例功能**：提供文件上传示例，包括创建存储桶、上传文件（支持重命名）及验证上传结果。  

**主要特性：**  
- 兼容 Amazon S3 API，支持 MinIO 及其他 S3 兼容服务；  
- 提供详细的 API 文档和示例代码；  
- 支持 Python 3.9 及以上版本；  
- 可通过 `mc` 命令行工具验证操作结果。  

**注意事项**：  
- 示例中使用的 `play.min.io` 测试服务器为公开服务，上传数据默认公开可读；  
- 需自行创建本地文件（如 `/tmp/test-file.txt`）以运行示例。