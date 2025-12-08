
---
title: openevolve
---

### [codelion openevolve](https://github.com/codelion/openevolve)

**核心内容总结：**

**项目功能**  
OpenEvolve 是一个开源的进化编程工具，基于大语言模型（LLM）实现自动代码优化，支持函数优化、GPU内核发现、提示（Prompt）优化等场景。通过多岛进化、MAP-Elites多样性维护等机制，探索代码改进方案，提供实时可视化界面跟踪演化过程。

**使用方法**  
1. 安装依赖（如Python、LLM API兼容环境）；  
2. 配置`config`文件，指定LLM接口（如OpenAI、本地Ollama等）；  
3. 运行示例任务（如函数最小化、GPU内核优化），通过命令启动可视化工具（`python visualizer.py`）；  
4. 自定义评估器，返回性能指标及错误信息（如`EvaluationResult`类）。

**主要特性**  
- **多目标优化**：支持性能、正确性、多样性等多维度评估；  
- **防止停滞**：通过岛屿迁移、温度控制、多样性维护（MAP-Elites）避免收敛；  
- **实时反馈**：错误日志、LLM反馈自动注入到下一代提示中；  
- **跨语言支持**：可优化Python、Rust等代码，适配不同LLM；  
- **可视化分析**：交互式界面展示演化树、性能曲线、代码差异等；  
- **自研提示优化**：通过元进化（Meta-Evolution）自动改进系统提示，提升LLM输出质量。