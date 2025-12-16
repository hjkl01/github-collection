
---
title: faker
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/joke2k/faker?style=social) ](https://github.com/joke2k/faker)
### [joke2k faker](https://github.com/joke2k/faker)

**项目核心内容总结：**  
Faker 是一个 Python 库，用于生成模拟数据，支持数据库填充、测试数据生成、压力测试等场景。  

**主要功能与特性：**  
1. **多语言支持**：可生成多种语言的假数据（如英文、法文等），并支持自定义语言内容（如替换 Lorem 文本）。  
2. **灵活使用**：通过 `Faker()` 实例调用方法生成数据（如 `fake.name()`），支持动态提供者（从外部读取数据）、唯一值生成（避免重复）、种子设置（保证数据可复现）。  
3. **性能优化**：提供 `use_weighting` 参数控制数据生成的随机性权重。  
4. **集成能力**：支持与 `Factory Boy` 测试框架集成，通过 `factory.Faker` 生成数据；提供 `pytest` 插件支持。  
5. **高级功能**：支持多实例独立随机数生成、多语言唯一值生成（指定语言上下文）、异常处理（如唯一值生成冲突时抛出 `UniquenessException`）。  

**使用方法：**  
- 安装：`pip install Faker`  
- 基础用法：  
  ```python  
  from faker import Faker  
  fake = Faker()  
  print(fake.name())  # 生成随机姓名  
  ```  
- 命令行生成文档：`python -m faker > docs.txt`  
- 自定义提供者：通过继承 `BaseProvider` 或使用 `DynamicProvider` 动态读取外部数据。  

**注意事项：**  
- 种子设置（`seed()`）生成的随机数据依赖 Faker 版本，版本更新可能导致结果变化。  
- 唯一值生成可能因数据范围有限（如姓名）触发异常，需合理控制生成数量。