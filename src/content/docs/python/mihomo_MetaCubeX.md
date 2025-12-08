
---
title: mihomo
---

### [MetaCubeX mihomo](https://github.com/MetaCubeX/mihomo)

**核心内容总结：**  
该项目是一个用于解析《崩坏：星穹铁道》玩家数据的Python库，基于Mihomo API提供类型提示和自动补全支持。  

**功能：**  
- 通过Mihomo API获取并解析玩家数据（包括角色、成就等信息）。  
- 支持两种数据格式（V1和V2），对应不同版本的模型结构。  
- 提供工具函数，如去除重复角色、合并角色数据等。  
- 支持数据持久化（如使用pickle或JSON保存/加载数据）。  

**使用方法：**  
1. 安装：`pip install -U git+https://github.com/KT-Yeh/mihomo.git`  
2. 初始化API客户端并指定语言。  
3. 调用`fetch_user`或`fetch_user_v1`获取数据，使用对应模型（如`StarrailInfoParsed`或`StarrailInfoParsedV1`）。  
4. 工具函数可直接操作数据（如`tools.remove_duplicate_character`）。  
5. 数据可通过序列化方式保存，支持压缩和解析。  

**主要特性：**  
- 自动补全与类型安全（基于pydantic模型）。  
- 支持两种版本的数据模型（V1/V2）。  
- 提供便捷的工具函数处理数据。  
- 灵活的数据持久化方案（JSON、pickle等）。