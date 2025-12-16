
---
title: orjson
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ijl/orjson?style=social) ](https://github.com/ijl/orjson)
### [ijl orjson](https://github.com/ijl/orjson)

**项目核心内容总结：**  
orjson 是一个高性能的 Python JSON 库，支持 JSON 序列化与反序列化，严格遵循 RFC 8259 标准。其主要特性包括：  
1. **性能优势**：比 Python 标准库 `json` 快 10-100 倍，适用于大规模数据处理。  
2. **类型支持**：原生支持 UUID、datetime、bytes 等类型，可扩展自定义类型。  
3. **严格验证**：拒绝非法 JSON 格式，确保数据安全性。  
4. **测试全面**：通过 JSONTestSuite 等测试集验证，兼容多平台（Linux、macOS、Windows）。  
5. **易用性**：提供 `dumps` 和 `loads` 接口，支持 `default` 和 `object_hook` 自定义处理。  

**使用方法**：  
通过 `pip install orjson` 安装，使用 `orjson.dumps()` 和 `orjson.loads()` 替代标准库函数。  

**注意事项**：  
- 不支持数据类、Decimal 等复杂对象的自动反序列化，需手动处理。  
- 仅提供 `bytes` 类型的序列化结果，不直接生成 `str`。  
- 不支持 JSON5、NDJSON 等扩展格式。  

**许可证**：Apache 2.0 或 MIT 双许可。