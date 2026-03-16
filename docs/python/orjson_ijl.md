### [ijl orjson](https://github.com/ijl/orjson)  ![GitHub Repo stars](https://img.shields.io/github/stars/ijl/orjson?style=social)

orjson 是 Python 中性能最快的 JSON 库，序列化速度约为标准 json 的 10 倍，反序列化约为 2 倍，且严格遵循 UTF-8 和 RFC 8259 标准，正确性更高。它原生支持 dataclass、datetime、numpy、uuid 等复杂类型，输出为 bytes 对象。支持多种选项控制格式（如缩进、排序、严格整数），并提供 default 参数处理任意类型。仅支持 CPython 3.10 至 3.15，不支持 PyPy。