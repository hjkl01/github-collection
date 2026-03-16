### [stretchr testify](https://github.com/stretchr/testify)  ![GitHub Repo stars](https://img.shields.io/github/stars/stretchr/testify?style=social)

Testify 是一套 Go 语言测试工具包，用于验证代码行为是否符合预期。核心功能包括：

1. **assert**：提供易读友好的断言方法和失败描述，支持返回布尔值以进行条件判断。
2. **require**：功能同 assert，但断言失败时立即终止当前测试。
3. **mock**：提供模拟对象机制，用于替代真实对象并设置和验证调用期望。
4. **suite**：支持以结构体构建测试套件，包含 Setup/Teardown 方法，但不支持并行测试。