
---
title: OpCore-Simplify
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/lzhoang2801/OpCore-Simplify?style=social) ](https://github.com/lzhoang2801/OpCore-Simplify)
### [lzhoang2801 OpCore-Simplify](https://github.com/lzhoang2801/OpCore-Simplify)

**项目核心内容总结**  
OpCore Simplify 是一款自动化工具，用于简化 OpenCore EFI 的创建流程，提供标准化配置，减少手动操作。  

**主要功能**  
1. **硬件与系统兼容性支持**：支持 Intel/AMD CPU、多代 GPU（包括 NVIDIA、AMD、Intel iGPU）及 macOS High Sierra 至 Tahoe 版本，提供硬件兼容性检查功能。  
2. **自动化配置**：自动添加 ACPI 补丁（如 FakeEC、FixHPET）和内核扩展（kexts），优化电源管理、GPU 识别、睡眠状态等。  
3. **自动更新**：构建 EFI 前自动更新 OpenCorePkg 和 kexts。  
4. **EFI 自定义配置**：支持 CPU/GPU ID 伪装、SMBIOS 优化、Resizable BAR 设置、WiFi 自动连接等。  
5. **灵活定制**：允许用户手动调整 ACPI 补丁、kexts 和 SMBIOS（需谨慎操作）。  

**使用方法**  
1. 下载并解压工具，通过 `.bat`（Windows）、`.command`（macOS）或 `.py`（Linux）运行。  
2. 生成硬件报告（推荐使用内置导出功能或 Hardware Sniffer 工具）。  
3. 选择 macOS 版本，工具自动匹配补丁和 kexts。  
4. 构建 EFI，工具会自动下载所需文件。  
5. 使用 UnPlugged 工具制作 USB 安装盘并安装 macOS。  

**注意事项**  
- 需结合 Dortania 指南理解基础概念，安装后需自行测试和排错。  
- 工具不保证首次安装成功，部分功能（如 AMD 显卡加速）需后续手动调整参数。  
- 仅 OpenCore-Legacy-Patcher 3.0.0 支持 macOS Tahoe 26，其他版本不兼容。