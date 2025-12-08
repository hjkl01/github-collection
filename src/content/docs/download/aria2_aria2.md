
---
title: aria2
---

### [aria2 aria2](https://github.com/aria2/aria2)

**项目核心内容总结：**  
aria2 是一个支持多协议的下载工具，可下载 HTTP/HTTPS/FTP/SFTP/BitTorrent/Metalink 等资源，具备以下特性：  
1. **功能**：支持 BitTorrent（含 DHT、UDP 跟踪器）、Metalink 校验（MD5/SHA 系列）、WebSocket 服务器，以及通过 libaria2 库提供 C++ 接口。  
2. **使用方法**：通过命令行参数（如 `-o` 指定文件名、`--bt-max-open-files` 控制并发文件数）或配置文件设置，支持从 Metalink 文件自动验证数据块完整性。  
3. **主要特性**：  
   - **BitTorrent 扩展**：兼容 DHT、IPv6 跟踪器、Fast Extension 等协议，支持私有 torrent 和多 tracker 元数据。  
   - **Metalink 支持**：自动验证文件哈希，失败时直接退出；支持多源镜像和协议切换（HTTP/FTP/SFTP）。  
   - **网络优化**：默认使用 6881-6999 端口，支持 IPv4/IPv6，通过 `--dht-listen-port` 调整端口。  
   - **配置灵活性**：支持 `.netrc` 认证、`--metalink-base-uri` 解析相对路径，可禁用 netrc（`-n` 参数）。  
4. **依赖与构建**：需安装 libxml2、libcurl 等库，通过 `--enable-libaria2` 编译动态库，`--enable-static` 生成静态库。  

**注意事项**：需手动配置路由器端口转发，下载速率受限时可通过 `--bt-request-peer-speed-limit` 调整。