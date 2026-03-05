
---
title: syft
---

### [anchore syft](https://github.com/anchore/syft)  ![GitHub Repo stars](https://img.shields.io/github/stars/anchore/syft?style=social)

Syft 是一个用于生成软件物料清单（SBOM）的命令行工具和 Go 库。它支持从容器镜像、文件系统及归档文件中提取软件包信息，兼容 OCI、Docker 等多种镜像格式及数十种包生态（如 Go、Python、Java、RPM 等）。项目支持 CycloneDX、SPDX 等多种 SBOM 输出格式，可与 Grype 集成进行漏洞扫描，并支持基于 in-toto 规范创建签名 SBOM 证明。