
---
title: taichi
---

### [taichi-dev taichi](https://github.com/taichi-dev/taichi)

Taichi Lang 是一个嵌入 Python 的高性能数值计算语言，通过 JIT 编译技术将 Python 代码转换为 GPU/CPU 指令，适用于物理模拟、AI、图形渲染等场景。核心功能包括：  
1. **Python 集成**：语法与 Python 高度兼容，支持 NumPy/PyTorch 生态；  
2. **高性能计算**：通过 `@ti.kernel` 装饰器实现并行化，支持 CUDA/Vulkan 等多平台；  
3. **灵活性**：提供 SNode 数据结构，支持稀疏计算、多维场构建；  
4. **可扩展性**：包含可微编程、量化计算（实验性）等特性。  

**使用方法**：  
- 安装：`pip install taichi` 或夜间版 `pip install taichi-nightly`；  
- 示例：运行 `ti gallery` 启动演示，通过 `@ti.kernel` 编写并行代码（如分形生成、流体模拟）。  

项目支持跨平台部署，适用于实时模拟、视觉特效、科学计算等领域。