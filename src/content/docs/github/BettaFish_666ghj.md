
---
title: BettaFish
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/666ghj/BettaFish?style=social) ](https://github.com/666ghj/BettaFish)
### [666ghj BettaFish](https://github.com/666ghj/BettaFish)

**项目核心内容总结**：

BettaFish 是一个舆情分析系统，支持数据爬取、多语言情感分析、自定义报告生成及多数据库接入。主要功能包括：  
1. **数据爬取与分析**：通过爬虫收集网络数据，结合多种情感分析模型（如多语言模型、BERT微调、Qwen3、传统机器学习）进行情绪判断。  
2. **报告生成**：支持自定义Markdown/文本模板，生成结构化分析报告，可通过Web界面或API调用。  
3. **多数据库支持**：兼容MySQL、MongoDB等数据库，允许接入自定义业务数据，扩展数据查询功能。  
4. **灵活配置**：提供命令行与Web界面操作，支持自定义数据库连接、模板上传及模型切换。  

**使用方法**：  
- 安装Python环境，配置数据库连接参数。  
- 运行爬虫采集数据，通过InsightEngine执行分析。  
- 使用ReportEngine生成报告，支持自定义模板与导出。  

**主要特性**：  
- 多语言情感分析（中/英文等）、多种模型可选（BERT、Qwen微调、传统机器学习）。  
- 支持自定义业务数据库接入与数据查询工具开发。  
- 提供API接口与Web界面，便于集成与操作。  
- 开源项目，遵循GPL-2.0许可证，适用于学术研究与教育场景。