
---
title: RustPython
---

### [RustPython RustPython](https://github.com/RustPython/RustPython)

**项目核心内容总结：**  
RustPython 是一个用 Rust 编写的 Python 3 解释器，支持 CPython 3.13.0 及以上版本，目标是提供一个完全用 Rust 实现的 Python 环境，无需依赖 CPython 绑定或兼容性补丁。  

**功能与特性：**  
- **跨平台支持**：可在本地运行（包括 Windows）、WebAssembly（WASI）及嵌入到 Rust 应用中。  
- **JIT 编译器**：实验性功能，可将 Python 函数编译为本地代码以提升性能。  
- **WebAssembly 支持**：可构建为独立的 WASI 模块，通过 `wasmer` 或 `wapm` 运行。  
- **嵌入能力**：提供示例代码展示如何将 RustPython 集成到 Rust 应用中，用于脚本扩展。  
- **SSL 配置**：默认使用 `rustls`，也可切换为 `openssl`（需依赖或编译）。  

**使用方法：**  
1. 安装 Rust（通过 [rustup.rs](https://rustup.rs/)）。  
2. 克隆仓库并构建：  
   ```bash  
   git clone https://github.com/RustPython/RustPython  
   cd RustPython  
   cargo run --release demo_closures.py  
   ```  
3. 交互式 shell：`cargo run --release`。  
4. 安装 pip：`cargo install --git ... rustpython && rustpython --install-pip`。  
5. WASI 构建：  
   ```bash  
   cargo build --target wasm32-wasip1 --features freeze-stdlib  
   ```  

**注意事项：**  
- 项目尚在开发中，非完全生产就绪，但已支持部分实际应用（如数据库、游戏引擎等）。  
- Windows 用户需设置 `RUSTPYTHONPATH` 环境变量指向 `Lib/` 目录。  
- JIT 和 WASI 需额外依赖或编译工具（如 `clang`、`make`）。  

**许可证：**  
采用 MIT 许可证，项目 Logo 使用 CC-BY-4.0 许可证。