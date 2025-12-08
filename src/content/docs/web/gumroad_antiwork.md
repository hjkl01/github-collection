
---
title: gumroad
---

### [antiwork gumroad](https://github.com/antiwork/gumroad)

**核心内容总结：**  
**项目功能**：Gumroad 是一个电商平台，允许创作者直接向消费者销售产品，该 README 提供了其 Web 应用的源码开发指南。  

**使用方法**：  
1. **环境准备**：需安装 Ruby、Node.js、Docker、MySQL 8.0、ImageMagick、libvips、FFmpeg、PDFtk、wkhtmltopdf 等依赖。  
2. **安装配置**：通过 Bundler 安装 Ruby 依赖，npm 安装 Node.js 依赖，配置 `.env` 文件并创建指定 S3 存储桶（`gumroad_dev` 和 `gumroad-dev-public-storage`）。  
3. **运行本地服务**：使用 `make local` 启动 Docker 服务，执行 `bin/rails db:prepare` 初始化数据库，通过 `bin/dev` 启动应用（访问地址 `https://gumroad.dev`）。  

**主要特性**：  
- 支持 Docker 容器化开发环境；  
- 提供本地 SSL 证书生成工具（mkcert）；  
- 集成 Elasticsearch 索引管理（需手动重置）；  
- 支持推送通知（RPush）；  
- 包含开发常用任务（如 Rails 控制台、Rake 任务、代码规范检查）。  

**注意事项**：  
- macOS 用户需禁用 Spring 框架以避免测试时的 `fork()` 错误。