### [lego](https://github.com/go-acme/lego) ![GitHub Repo stars](https://img.shields.io/github/stars/go-acme/lego?style=social)

<think>**总结主要功能**

这个项目是一个使用Go语言编写的ACME客户端和库，支持自动管理证书。它涵盖了注册、获取、续订和吊销证书，支持多种DNS提供商的挑战验证，提供命令行工具和库两种使用方式。</think>

Lego 是用 Go 编写的 ACME 客户端和库，可用于 Let's Encrypt 等 CA 自动签发 HTTPS 证书。支持 ACME v2 及多项扩展（ALPN、IP 证书、续期信息、配置文件），可注册 CA、申请/续期/吊销证书、支持 SAN、证书打包与 OCSP，提供 HTTP-01、DNS-01、TLS-ALPN-01 挑战及自定义挑战解算器，并内置约 180 个 DNS 服务商集成；可作为命令行工具或库使用。