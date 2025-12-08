
---
title: pocketbase
---

### [pocketbase pocketbase](https://github.com/pocketbase/pocketbase)

**项目核心内容总结：**

**功能**  
PocketBase 是一个开源的 Go 语言后端框架，集成嵌入式 SQLite 数据库（支持实时订阅）、文件与用户管理、可视化 Admin 仪表盘，以及简洁的 REST-ish API 接口。

**使用方法**  
1. **作为独立应用**：  
   - 从 [Releases 页面](https://github.com/pocketbase/pocketbase/releases) 下载预构建的可执行文件，解压后运行 `./pocketbase serve` 启动。  
   - 默认启用 JS VM 插件，支持通过 JavaScript 扩展功能。  

2. **作为 Go 框架**：  
   - 通过 Go 模块集成，自定义业务逻辑。  
   - 示例代码：通过 `main.go` 定义路由（如 `/hello`），使用 `go run main.go serve` 启动，或通过 `CGO_ENABLED=0 go build` 构建静态可执行文件。  

**主要特性**  
- 支持跨平台构建（涵盖主流操作系统和架构，如 Linux/Windows/macOS）。  
- 提供官方 SDK（JavaScript/Dart），简化 Web/移动端开发。  
- 支持通过 Go 或 JavaScript 扩展功能（如自定义路由、业务逻辑）。  
- 内置测试工具，支持 `go test ./...` 运行单元/集成测试。  

**注意事项**  
项目仍在活跃开发中，v1.0.0 前不保证完全向后兼容。