
---
title: viper
---

### [spf13 viper](https://github.com/spf13/viper)  ![GitHub Repo stars](https://img.shields.io/github/stars/spf13/viper?style=social)

Viper 是一款为 Go 应用程序设计的完整配置解决方案。核心功能包括：
1. **多源配置读取**：支持配置文件（JSON、TOML、YAML、INI 等）、环境变量、命令行标志、默认值、显式设置及远程键值存储（Etcd、Consul、Firestore 等）。
2. **配置优先级**：遵循显式设置优先于标志、环境变量、配置文件、外部存储及默认值的合并顺序。
3. **动态特性**：支持配置文件动态发现、实时监听文件变化并自动更新配置。
4. **数据处理**：支持配置键别名、子集提取、反序列化为结构体，以及远程配置的加密与解密。
5. **集成支持**：支持 Go Modules，键名默认不区分大小写，可与 Cobra/pflag 库无缝集成。