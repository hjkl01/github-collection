
---
title: mimesis
---

### [lk-geimfari mimesis](https://github.com/lk-geimfari/mimesis)

**项目核心内容总结：**  
Mimesis 是一个 Python 假数据生成器，支持 46 种语言环境，可生成包括个人信息、邮箱、电话等多类数据。主要特性包括：多语言支持、可扩展性（支持自定义数据提供者）、高性能、基于模式的数据生成、类型提示（支持编辑器自动补全）。  

**使用方法：**  
通过 `pip install mimesis` 安装后，导入对应的数据提供者（如 `Person`），调用其方法生成数据。例如：  
```python  
from mimesis import Person  
person = Person("en")  
print(person.full_name())  # 输出随机英文全名  
```  

**注意事项：**  
- Python 3.8/3.9 用户需安装 11.1.0 版本，19.0.0 及以上版本移除了内置数据提供者。  
- 完整文档见 [https://mimesis.name/](https://mimesis.name/)，采用 MIT 开源协议。