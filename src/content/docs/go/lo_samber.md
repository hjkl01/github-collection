
---
title: lo
---

### [samber lo](https://github.com/samber/lo)

**项目核心内容总结：**  

**功能**：  
`lo` 是一个 Go 语言实用函数库，提供函数式编程工具，简化集合操作（如 `Map`、`Filter`、`Reduce`）和常见编程任务（如错误处理、断言、类型检查等）。  

**主要特性**：  
- **高性能**：通过减少内存分配和避免反射，`lo.Map` 比 `go-funk` 等库快 7 倍，且内存效率接近原生 `for` 循环。  
- **类型安全**：函数支持泛型，确保编译时类型检查。  
- **丰富的辅助工具**：包括错误处理（`Try`、`Catch`、`TryOr`）、断言（`Assert`）、类型检查（`ErrorsAs`）等功能。  
- **易用性**：提供简洁的 API，如 `lo.Map`、`lo.Filter` 等，直接操作切片、映射等数据结构。  

**使用方法**：  
示例：  
```go  
_ = lo.Map[int64](arr, func(x int64, i int) string {  
    return strconv.FormatInt(x, 10)  
})  
```  

**性能优势**：  
基准测试显示，`lo.Map` 在 CPU 和内存使用上优于其他库（如 `lop.Map`、`go-funk`），仅比原生 `for` 循环慢 4%。  

**其他**：  
- 支持通过 `Try`、`Catch` 处理 panic 和错误，`TryOr` 提供默认值。  
- 提供 `Assert` 和 `Assertf` 进行条件检查（虽不推荐频繁使用）。  
- 项目使用 MIT 许可证，可通过 GitHub 贡献代码或提出功能需求。