
---
title: ddddocr
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sml2h3/ddddocr?style=social) ](https://github.com/sml2h3/ddddocr)
### [sml2h3 ddddocr](https://github.com/sml2h3/ddddocr)

**项目总结：**

该项目是一个基于Python的OCR（光学字符识别）工具，名为`ddddocr`，主要用于识别验证码图片中的文字内容。其核心功能包括：

- **验证码识别**：支持多种验证码类型（如字母、数字、彩色验证码等），并提供颜色过滤功能，提升识别准确率。
- **目标检测**：可检测图像中的目标区域（如验证码位置）。
- **滑块匹配与比较**：支持滑块验证码的识别与处理。
- **API服务支持**：提供RESTful API接口，方便集成到其他系统中使用。
- **MCP协议支持**：支持AI Agent通过MCP协议调用服务。
- **多平台兼容**：可在Windows、Linux、macOS等系统上运行，支持GPU加速。

**使用方法：**

1. **安装**：通过pip安装`ddddocr`。
2. **初始化**：使用`DdddOcr`类初始化OCR实例。
3. **调用功能**：
   - `ocr`：识别验证码图片中的文字。
   - `detect`：检测图像中的目标区域。
   - `slide_match` 和 `slide_comparison`：处理滑块验证码。
4. **API服务**：通过启动API服务，使用HTTP接口进行远程调用。
5. **颜色过滤**：支持预设颜色（如红色、蓝色）或自定义HSV颜色范围进行图像过滤。

**主要特性：**

- 支持多种模型（old、beta等）以适应不同类型的验证码。
- 提供字符集限制功能（`set_ranges`），缩小识别范围，提高准确率。
- 支持GPU加速，提升处理速度。
- 提供命令行工具，如`python -m ddddocr colors`用于查看颜色预设。
- 可训练自定义模型，适用于特定场景。

**适用场景：**

适用于需要自动识别验证码的场景，如自动化注册、登录、爬虫等。