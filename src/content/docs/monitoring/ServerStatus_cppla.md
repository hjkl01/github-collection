
---
title: ServerStatus
---

### [cppla ServerStatus](https://github.com/cppla/ServerStatus)

**核心内容总结：**

**项目功能**  
ServerStatus中文版是一款支持多服务器监控的云探针工具，提供服务器负载、网络、磁盘等状态监测，并支持通过Telegram、Server酱等渠道发送告警通知。  

**使用方法**  
- **服务端部署**：支持Docker或Docker-compose一键启动，或手动编译安装（需安装依赖如gcc、libcurl）。需配置JSON文件定义服务器信息、监控规则及告警回调地址。  
- **客户端配置**：下载对应平台的Python脚本（如`client-linux.py`），设置服务器地址、用户名及密码后后台运行，支持开机自启。  

**主要特性**  
- **Watchdog触发式告警**：根据自定义规则（如CPU>90%、内存使用率>90%）触发告警，支持排除特定条件（如排除某机器）。  
- **多平台兼容**：支持Linux、Windows等系统，客户端跨平台运行。  
- **灵活监控规则**：可组合字段表达式（如`(network_out-last_network_out)/1024/1024/1024>999`）监测流量、丢包率等。  
- **告警渠道多样**：支持Telegram、Server酱、PushDeer等回调通知。  

**注意事项**  
- 监控规则表达式需使用英文字符（Exprtk库不支持中文）。  
- `watchdog interval`为告警最小通知间隔，非探测频率。