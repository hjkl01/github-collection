
---
title: restic
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/restic/restic?style=social) ](https://github.com/restic/restic)
### [restic restic](https://github.com/restic/restic)

**项目核心内容总结：**

**功能**  
restic 是一款支持 Linux、macOS、Windows 等多平台的高效备份工具，支持通过本地目录、SFTP、HTTP、S3、Google Cloud Storage 等多种后端存储备份数据，提供加密、去重、增量备份及快速恢复能力。

**使用方法**  
1. 初始化备份仓库：`restic init --repo <路径>`（需设置密码）  
2. 执行备份：`restic --repo <路径> backup <目录>`  
3. 恢复数据：`restic restore` 或通过 `restic mount` 挂载仓库浏览历史快照。

**主要特性**  
- **安全性**：数据加密存储，保障隐私与完整性。  
- **高效性**：增量备份与去重技术减少存储空间占用。  
- **快速性**：备份/恢复速度受限于硬件带宽，支持快速恢复所需数据。  
- **可验证性**：提供数据可恢复性验证功能。  
- **兼容性**：支持多种云存储及本地后端，可通过 rclone 扩展更多服务。  
- **可重现构建**：0.6.1 及以上版本支持从源码完全复现二进制文件。