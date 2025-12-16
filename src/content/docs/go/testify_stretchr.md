
---
title: testify
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/stretchr/testify?style=social) ](https://github.com/stretchr/testify)
### [stretchr testify](https://github.com/stretchr/testify)

Testify 是一个 Go 语言测试工具包，提供断言、模拟对象和测试套件等功能，帮助开发者更高效地编写测试代码。  

**核心功能**：  
1. **断言工具（assert）**：支持断言相等、不等、nil 检查等，提供清晰的失败信息，支持条件判断继续测试。  
2. **终止测试工具（require）**：与 assert 类似，但断言失败时直接终止当前测试。  
3. **模拟对象（mock）**：通过定义接口模拟对象，设置预期调用和返回值，验证测试中方法是否按预期执行。  
4. **测试套件（suite）**：支持构建测试套件，提供 Setup/Teardown 方法，集中管理测试逻辑。  

**使用方法**：  
- 安装：`go get github.com/stretchr/testify`  
- 导入包（如 assert）并编写测试函数，例如：  
  ```go  
  assert.Equal(t, 123, 123, "值应相等")  
  ```  
- 模拟对象示例：定义接口实现，设置预期调用 `On()`，验证 `AssertExpectations()`。  

**主要特性**：  
- 支持 Go 1.19 及以上版本。  
- `suite` 包不支持并行测试。  
- 提供 API 文档、测试规范建议（如使用 testifylint）及社区支持。  

**注意事项**：  
- `mock` 包需手动编写模拟逻辑或使用 `mockery` 工具生成。  
- `suite` 包需通过 `suite.Run()` 启动测试套件。