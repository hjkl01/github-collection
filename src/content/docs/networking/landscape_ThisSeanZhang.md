
---
title: landscape
---

### [ThisSeanZhang landscape](https://github.com/ThisSeanZhang/landscape)

**项目核心内容总结：**  
Landscape 是一个基于 Web 的 Linux 路由器配置工具，使用 Rust、eBPF 和 AF_PACKET 开发，支持流量控制、eBPF 路由、独立 DNS 配置、Docker 流量导入及 Geo 管理。  

**主要功能：**  
- **流量控制**：支持流量分类、优先级设置及基于规则的路由。  
- **eBPF 路由**：利用 eBPF 技术实现高性能网络数据包处理。  
- **DNS 配置**：为不同流量设置独立 DNS，提升网络灵活性。  
- **Docker 集成**：可将容器流量导入路由器进行统一管理。  
- **Geo 管理**：支持基于地理位置的流量路由策略。  

**使用方法：**  
1. **系统要求**：需 Linux 6.9 或更高版本，部分功能依赖 Docker。  
2. **部署步骤**：  
   - 下载二进制文件，以 root 身份运行 `./landscape-webserver`，默认端口 6300，账号密码均为 `root`。  
   - 配置 `landscape_init.toml` 文件，定义初始参数。  
   - 可通过 systemd 设置为系统服务。  
3. **构建说明**：参考项目提供的编译文档或交叉编译指南。  

**许可证**：  
- `landscape-ebpf` 模块使用 GNU GPL v2.0，其他部分使用 GNU GPL v3.0。  

**适用场景**：适用于需要精细化网络管理的场景，如家庭路由器、企业网络优化及开发测试环境。