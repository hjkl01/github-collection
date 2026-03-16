### [sml2h3 ddddocr](https://github.com/sml2h3/ddddocr)  ![GitHub Repo stars](https://img.shields.io/github/stars/sml2h3/ddddocr?style=social)

DdddOcr 是一个通用验证码离线本地识别 Python 库，核心功能包括：

1.  **文字识别 (OCR)**：支持数字、字母、中文及特殊字符，提供概率输出、自定义字符范围、颜色过滤及透明 PNG 修复功能。
2.  **目标检测**：用于检测图片中目标的位置坐标。
3.  **滑块验证码处理**：提供边缘匹配和图像差异比较算法，用于识别滑块缺口位置。
4.  **自定义模型**：支持导入 ONNX 格式的自定义训练模型。

技术特性方面，项目支持 CPU/GPU 加速、多线程优化与批量处理，提供 RESTful API 服务及 Docker 部署方案，兼容 Windows、Linux 和 macOS 系统。