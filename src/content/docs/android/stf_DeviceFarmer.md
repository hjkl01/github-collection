
---
title: stf
---

### [DeviceFarmer stf](https://github.com/DeviceFarmer/stf)

**项目核心内容总结：**

**功能**  
STF（Smartphone Test Farm）是一个用于连接和管理移动设备的平台，支持通过USB将设备接入测试环境，提供Web界面进行设备控制、监控和测试。  

**使用方法**  
1. 通过Docker部署STF服务（提供Docker镜像）。  
2. 使用兼容的USB Hub和控制器（如Plugable或System TALKS）连接设备。  
3. 通过Web界面管理设备，支持多语言（中、日等）。  

**主要特性**  
- 支持多种设备连接（兼容不同USB Hub和控制器）。  
- 提供高功率输出的USB Hub推荐（如Plugable 7口Hub）。  
- 多语言支持（可通过Transifex翻译扩展）。  
- 社区驱动，支持开源贡献和测试。  
- 部署灵活，依赖Docker容器化技术。  

**注意事项**  
- 部分硬件（如玄人志向USB3.0卡）存在兼容性问题。  
- 需注意Hub的供电设计（部分Hub仅部分端口供电）。