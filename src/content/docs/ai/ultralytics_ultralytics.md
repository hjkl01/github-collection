
---
title: ultralytics
---

### [ultralytics ultralytics](https://github.com/ultralytics/ultralytics)  ![GitHub Repo stars](https://img.shields.io/github/stars/ultralytics/ultralytics?style=social)

**项目核心内容总结：**

1. **功能与性能**  
   Ultralytics YOLOv8 是一个高效的目标检测框架，提供多种模型版本（n/s/m/l/x），在 COCO 数据集上实现高精度（如 mAP 53.3%）与低参数量（如 3.2M）。支持实时推理（如 160 FPS）和多任务（检测/分割/姿态估计）。

2. **使用方法**  
   - 安装：`pip install ultralytics`  
   - 训练：`yolo train data=coco.yaml model=yolov8n.pt`  
   - 验证：`yolo val`  
   - 预测：`yolo predict model=yolov8n.pt`  
   - 导出模型：支持 ONNX/TensorRT/PyTorch/TF 等格式。

3. **主要特性**  
   - 模块化架构，支持自定义配置。  
   - 自动混合精度训练与分布式训练加速。  
   - 集成可视化工具（如 TensorBoard）。  
   - 与主流平台（Weights & Biases、Comet ML）兼容，支持模型跟踪与优化。  
   - 开源 AGPL-3.0 许可证，企业可申请商业授权。  

**注意事项**  
- 本文档为英文 README 的中文翻译与核心提炼，未包含图片及非核心内容。