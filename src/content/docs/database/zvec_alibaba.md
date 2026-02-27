
---
title: zvec
---

### [alibaba zvec](https://github.com/alibaba/zvec)  ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/zvec?style=social)

Zvec 是一个开源的进程内向量数据库，轻量、快速，可直接嵌入应用程序中。它基于阿里巴巴经过实战验证的 Proxima 向量搜索引擎构建，提供生产级别的低延迟、可扩展的相似性搜索功能，且几乎无需配置。

### ✅ 核心功能：
- **极速搜索**：可在毫秒内完成数十亿向量的搜索。
- **即装即用**：安装后即可快速使用，无需服务器、无需配置。
- **支持密集和稀疏向量**：支持混合查询密集和稀疏嵌入。
- **混合搜索**：结合语义相似性和结构化过滤，提升搜索精度。
- **跨平台运行**：作为进程内库，可在各种环境中运行，包括笔记本、服务器、命令行工具或边缘设备。

### 📦 安装方式：
- **Python**：
  ```bash
  pip install zvec
  ```
- **Node.js**：
  ```bash
  npm install @zvec/zvec
  ```

### 🚀 快速示例（Python）：
```python
import zvec

# 定义集合结构
schema = zvec.CollectionSchema(
    name="example",
    vectors=zvec.VectorSchema("embedding", zvec.DataType.VECTOR_FP32, 4),
)

# 创建并打开集合
collection = zvec.create_and_open(path="./zvec_example", schema=schema)

# 插入文档
collection.insert([
    zvec.Doc(id="doc_1", vectors={"embedding": [0.1, 0.2, 0.3, 0.4]}),
    zvec.Doc(id="doc_2", vectors={"embedding": [0.2, 0.3, 0.4, 0.1]}),
])

# 向量相似性查询
results = collection.query(
    zvec.VectorQuery("embedding", vector=[0.4, 0.3, 0.3, 0.1]),
    topk=10
)

# 输出结果
print(results)
```

### 📈 性能表现：
Zvec 在大规模数据处理中表现出色，适合高要求的生产环境。具体性能数据可参考其性能基准文档。

### 🤝 社区参与：
- 提供 DingTalk、WeChat、Discord 和 X（Twitter）等渠道，方便用户交流和获取支持。
- 鼓励社区贡献，欢迎提交 bug 修复、功能增强或文档改进。