
---
title: dive
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/wagoodman/dive?style=social) ](https://github.com/wagoodman/dive)
### [wagoodman dive](https://github.com/wagoodman/dive)

**项目核心内容总结：**

dive 是一款用于分析 Docker/OCI 镜像的工具，可查看镜像层内容、识别冗余空间并优化镜像大小。主要功能包括：  
1. **分层分析**：显示镜像各层内容及文件变化（新增、修改、删除）。  
2. **效率评估**：估算镜像冗余空间占比及大小，提供优化建议。  
3. **快速分析**：支持一键构建镜像并立即分析（`dive build`）。  
4. **CI 集成**：通过设置 `CI=true` 实现自动化检测镜像效率，符合规则时返回成功状态。  
5. **多源支持**：可从 Docker、Podman 或本地镜像文件分析（`--source` 参数）。  

**使用方法**：  
- 直接运行 `dive <镜像名>` 或通过 Docker 命令别名分析。  
- 构建并分析镜像：`dive build -t <标签> .`。  
- 支持多平台安装（Linux、macOS、Windows、Docker 容器等）。  

**主要特性**：  
- 可视化交互式界面（支持键盘操作切换视图、过滤文件等）。  
- 支持自定义配置文件（如键绑定、UI 布局、分析规则）。  
- 提供 `.dive-ci` 文件定义 CI 检测阈值（如效率最低值、冗余空间上限）。