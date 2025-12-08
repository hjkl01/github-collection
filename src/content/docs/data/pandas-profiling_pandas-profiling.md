
---
title: pandas-profiling
---

### [pandas-profiling pandas-profiling](https://github.com/pandas-profiling/pandas-profiling)

**项目核心内容总结：**

ydata-profiling 是一个用于数据分析的 Python 库，能够自动生成详细的 HTML 格式数据探查报告，帮助用户快速了解数据集的结构、统计信息、缺失值、重复值、分布情况等。它支持多种数据格式，包括 pandas DataFrame、Spark DataFrame 等，并具备以下主要功能和特性：

- **数据探查功能**：自动分析数据类型、统计描述、缺失值、唯一值、相关性等。
- **可视化支持**：提供丰富的图表，如直方图、箱线图、热力图等，用于展示数据分布和关系。
- **支持多种数据源**：除 pandas 外，还支持 Spark、Dask 等大数据框架。
- **集成与扩展**：可与 Great Expectations、Streamlit、Dash 等工具集成，支持在数据管道中使用。
- **使用方法**：通过 pip 安装后，导入库并调用 `ProfileReport` 类即可生成报告，支持 Jupyter Notebook 中的交互式显示。
- **安装方式**：支持 pip、conda 安装，也可从源码安装，支持多种额外依赖安装（如 notebook、unicode、pyspark）。

**使用方法简述**：

1. 安装：`pip install ydata-profiling`。
2. 导入库并生成报告：
   ```python
   from ydata_profiling import ProfileReport
   profile = ProfileReport(df)
   profile.to_file("output.html")
   ```
3. 报告可在浏览器中打开查看，支持多种主题和自定义设置。

**主要特性**：

- 自动分析数据质量。
- 支持大规模数据处理（通过 pyspark）。
- 提供详细的可交互式 HTML 报告。
- 支持中文、Unicode 文本分析（需安装 unicode 依赖）。
- 可扩展性强，适用于数据科学工作流、数据清洗、数据预处理等场景。