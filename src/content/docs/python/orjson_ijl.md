
---
title: orjson
---

### [ijl orjson](https://github.com/ijl/orjson)  ![GitHub Repo stars](https://img.shields.io/github/stars/ijl/orjson?style=social)

orjson 是 Python 中高性能且正确的 JSON 库，序列化速度约为标准库的 10 倍，反序列化速度约为 2 倍。

它原生支持 dataclass、datetime、numpy 数组、UUID 等类型的序列化，输出为 UTF-8 编码的 bytes。库严格遵循 RFC 8259 标准，拒绝 NaN、Infinity 及非法 UTF-8 字符。支持通过 option 参数控制输出格式（如缩进、排序），并通过 default 参数处理自定义类型。反序列化时通过缓存字典键优化内存，支持 CPython 3.10+ 及多平台预编译包。

项目不支持 PyPy、嵌入式 Python 环境，也不直接提供文件读写功能。