
---
title: cs2-dumper
---

### [a2x cs2-dumper](https://github.com/a2x/cs2-dumper)

**核心内容总结：**  
该项目是一个用于《反恐精英2》（Counter-Strike 2）的内存偏移和接口信息提取工具（dumper），支持Windows和Linux系统，基于Memflow库实现。  

**功能与特性：**  
1. **支持平台**：兼容Windows和Linux（Linux版本需使用特定分支，但当前可能过时）。  
2. **使用方式**：运行游戏后执行`cs2-dumper`程序，可自动通过默认连接器（memflow-native）读取内存；也可通过参数指定其他连接器（如pcileech、kvm）。  
3. **参数配置**：支持自定义输出文件类型（如`cs`、`hpp`、`json`等）、输出目录、缩进格式、进程名称等。  
4. **权限要求**：部分连接器（如kvm、pcileech）需管理员权限（Linux用`sudo`，Windows以管理员身份运行）。  
5. **编译要求**：自行编译需Rust 1.74.0及以上版本。  

**使用方法：**  
- 下载预编译版本或通过`cargo`编译。  
- 启动游戏后运行`cs2-dumper`，根据需要配置连接器和输出选项。