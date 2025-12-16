
---
title: waifu2x
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nagadomi/waifu2x?style=social) ](https://github.com/nagadomi/waifu2x)
### [nagadomi waifu2x](https://github.com/nagadomi/waifu2x)

**项目核心内容总结：**

waifu2x 是一个基于深度卷积神经网络的图像超分辨率工具，支持动漫风格艺术和照片的高清修复与放大。主要功能包括：  
- **图像处理**：提供降噪（支持4个噪声等级）、2x放大、降噪+放大融合模式，支持PNG/JPG格式。  
- **批量处理**：通过文件列表实现多图批量处理，支持自定义输出命名规则。  
- **视频处理**：支持从视频中提取帧、处理后重新生成视频。  
- **自定义训练**：可使用用户自定义数据集训练降噪、放大或融合模型，提供训练脚本和示例。  

**使用方式**：  
- **命令行工具**：通过Lua脚本调用（如 `th waifu2x.lua`），支持GPU加速（需CUDA/cuDNN）。  
- **Web应用**：运行 `th web.lua` 启动本地服务（端口8812）。  
- **Docker部署**：提供镜像，支持GPU加速和挂载目录处理文件。  

**主要特性**：  
- 支持多种模型模式（降噪、放大、融合），可切换照片/动漫模型。  
- 优化性能（cuDNN加速、内存管理参数）。  
- 跨平台兼容（Linux + Docker），提供第三方工具替代方案（如waifu2x-ncnn-vulkan）。