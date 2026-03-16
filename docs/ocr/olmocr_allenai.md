### [allenai olmocr](https://github.com/allenai/olmocr)  ![GitHub Repo stars](https://img.shields.io/github/stars/allenai/olmocr?style=social)

olmOCR 是一款将 PDF 及图像格式文档转换为清洁、可读 Markdown 文本的工具包。该工具基于 7B 参数视觉语言模型（VLM），需 GPU 支持运行。核心功能包括支持公式、表格、手写体及复杂排版，自动去除页眉页脚，并正确处理多栏布局与图文混排的自然阅读顺序。项目提供本地部署、Docker 容器化、外部 API 调用及多节点集群（S3/Beaker）处理方案，并附带完整的基准测试套件（olmOCR-Bench）和模型微调训练代码。