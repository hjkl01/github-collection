
---
title: immich-go
---

### [simulot immich-go](https://github.com/simulot/immich-go)  ![GitHub Repo stars](https://img.shields.io/github/stars/simulot/immich-go?style=social)

**项目核心内容总结：**

**功能**  
Immich-Go 是一款开源工具，用于将照片和视频上传至自托管的 Immich 服务器，支持从本地文件夹、Google Photos 导出文件、iCloud、ZIP 归档及其他 Immich 服务器迁移数据。具备智能管理功能，如重复检测、RAW+JPEG 合并、批量照片堆叠等。

**使用方法**  
1. 从 GitHub 发布页下载对应系统的二进制文件  
2. 命令行操作示例：  
   - 本地文件夹上传：`immich-go upload from-folder --server=服务器地址 --api-key=密钥 /照片路径`  
   - Google Photos 迁移：`immich-go upload from-google-photos --server=服务器地址 --api-key=密钥 /Takeout.zip路径`  
   - 从 Immich 服务器归档：`immich-go archive from-immich --server=服务器地址 --api-key=密钥 --write-to-folder=输出路径`

**主要特性**  
- 跨平台支持（Windows/macOS/Linux/FreeBSD）  
- 支持 10 万+级照片处理  
- 自动创建相册/标签，保留元数据和组织结构  
- 智能过滤系统文件（如 `.DS_Store`、`@eaDir/` 等）  
- 需 Immich 服务器配合，API 密钥需包含 `asset.copy` 和 `asset.delete` 权限  

**注意事项**  
- 当前为早期版本，建议备份文件  
- 迁移 Google Photos 需注意 JSON 元数据匹配  
- 服务器端需开启 API 访问权限