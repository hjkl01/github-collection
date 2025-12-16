
---
title: grm
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gphper/grm?style=social) ](https://github.com/gphper/grm)
### [gphper grm](https://github.com/gphper/grm)

**项目核心内容总结：**

本项目是一个基于Go语言和Vue3的Web版Redis管理工具，支持多种数据类型操作、用户鉴权、服务监控等功能。主要功能包括：  
- 管理Redis连接（支持直连和SSH）、切换DB；  
- 支持String/List/Set/ZSet/Hash/Stream类型的数据增删查改；  
- 提供用户鉴权、操作日志、LUA脚本执行及Redis性能监控；  
- 支持编译为独立二进制文件，可打包为Windows服务或通过Docker部署；  
- 提供命令行工具管理用户及服务运行。  

**使用方法：**  
1. **编译**：前端通过`npm run build`构建，后端使用`go build`生成二进制文件，推荐用UPX压缩；  
2. **运行**：支持三种方式：  
   - 命令行运行`grm srv run`；  
   - Docker构建镜像并运行容器；  
   - 安装为Windows服务（支持安装/卸载/启动/停止）；  
3. **Nginx反向代理配置**：提供标准及域名路径映射示例，访问地址格式为`http://域名/grm/static/#/`。  

**主要特性：**  
- 支持跨平台编译及服务化部署；  
- 提供可视化界面与命令行双重操作方式；  
- 集成用户权限管理、操作日志记录；  
- 支持通过Nginx反向代理部署至域名；  
- 提供Redis实时监控与性能分析功能。