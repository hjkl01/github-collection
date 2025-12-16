
---
title: ultrajson
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ultrajson/ultrajson?style=social) ](https://github.com/ultrajson/ultrajson)
### [ultrajson ultrajson](https://github.com/ultrajson/ultrajson)

**UltraJSON 核心内容总结：**

UltraJSON 是一个用纯 C 编写的超快速 JSON 编码器和解码器，提供 Python 绑定。其主要功能包括：

- **性能优势**：在多种 JSON 编解码场景中速度显著优于 `json`、`simplejson` 等库（如编码/解码数组、对象等场景下性能提升数倍）。
- **使用方法**：可通过 `pip install ujson` 安装，支持 `dumps`/`loads` 方法作为 Python 标准库的替代，例如：
  ```python
  import ujson
  ujson.dumps([{"key": "value"}, 81, True])
  ```
- **特性**：
  - 支持 `encode_html_chars`、`ensure_ascii`、`escape_forward_slashes` 等选项，控制输出格式（如 HTML 转义、ASCII 限制、斜杠转义等）。
  - 支持缩进输出（`indent` 参数）。
- **注意事项**：
  - 项目已进入**维护模式**，不推荐新增功能，建议迁移到更高效的 [orjson](https://pypi.org/project/orjson/)。
  - 构建时可配置调试符号或使用外部 `double-conversion` 库。