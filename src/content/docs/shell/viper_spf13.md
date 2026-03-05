
---
title: viper
---

### [spf13 viper](https://github.com/spf13/viper)  ![GitHub Repo stars](https://img.shields.io/github/stars/spf13/viper?style=social)

Viper 是 Go 语言的配置管理解决方案，遵循 12-Factor 应用规范。它支持从多种来源读取并合并配置，优先级包括显式设置、命令行标志、环境变量、配置文件、远程键值存储及默认值。支持的文件格式包括 JSON、TOML、YAML、INI、envfile 及 Java Properties 等。核心功能涵盖：配置文件及远程配置的动态发现、实时监听与自动更新；绑定环境变量与命令行标志；支持远程存储（Etcd、Consul、Firestore、NATS）及配置加密；配置项别名管理；多实例支持；以及将配置值反序列化为 Go 类型。默认配置键名大小写不敏感。