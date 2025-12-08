
---
title: IronCalc
---

### [ironcalc IronCalc](https://github.com/ironcalc/IronCalc)

**IronCalc 核心内容总结：**

1. **项目功能**  
   - 一个用 Rust 编写的现代电子表格引擎，支持多种编程语言（如 Python、JavaScript、Node.js 等）集成。  
   - 提供 XLSX 文件读写功能，支持创建、编辑和计算电子表格。  
   - 支持多种界面形式（终端、桌面应用、Web 应用）。  

2. **使用方法**  
   - **Docker 部署**：通过 `docker compose up --build` 启动，访问 http://localhost:2080 测试。  
   - **本地构建**：使用 `cargo build --release` 编译。  
   - **测试与覆盖率**：运行 `make tests` 执行所有测试，`make coverage` 生成覆盖率报告。  
   - **文档查看**：通过 `make docs` 生成本地 API 文档，或访问 https://docs.rs/ironcalc。  

3. **主要特性**  
   - 支持公式计算、多工作表管理及复杂数据操作（如示例中的公式 `=SUM(Sheet1!A1:CV100)`）。  
   - 提供完善的测试套件和代码覆盖率跟踪（通过 Codecov）。  
   - 双许可证（MIT/Apache 2.0），支持开源和商业应用。  
   - 项目处于开发阶段，提供早期浏览器预览（https://app.ironcalc.com）。  

4. **社区与协作**  
   - 鼓励开发者、设计师、Excel 用户等参与，可通过 Discord 或邮件（hello@ironcalc.com）联系。