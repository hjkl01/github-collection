### [anchore syft](https://github.com/anchore/syft)  ![GitHub Repo stars](https://img.shields.io/github/stars/anchore/syft?style=social)

Syft 是一个用于从容器镜像、文件系统和归档文件中生成软件物料清单（SBOM）的命令行工具和 Go 库。它支持数十种软件包生态系统（如 Alpine、Debian、RPM、Go、Python、Java 等），提供 CycloneDX、SPDX、Syft JSON 等多种 SBOM 输出格式。该工具可与 Grype 配合进行漏洞扫描，并支持使用 in-toto 规范创建签名的 SBOM 声明。