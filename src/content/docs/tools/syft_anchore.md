
---
title: syft
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/anchore/syft?style=social) ](https://github.com/anchore/syft)
### [anchore syft](https://github.com/anchore/syft)

**Syft 核心内容总结：**  

**项目功能**  
Syft 是一个开源工具，用于生成容器镜像和文件系统的软件物料清单（SBOM），帮助识别软件包和依赖项，支持漏洞检测（配合 Grype 使用）。  

**主要特性**  
- 支持 OCI、Docker、Singularity 等镜像格式，及文件系统、归档文件；  
- 支持多种 SBOM 输出格式（如 CycloneDX、SPDX、Syft 自有格式）；  
- 可创建符合 in-toto 规范的签名 SBOM；  
- 与 Grype 集成，提升漏洞扫描效率；  
- 支持 Linux 发行版识别及多语言生态（如 Go、Python、Java 等）。  

**使用方法**  
- **安装**：通过 `curl`、Homebrew、Scoop 等方式安装；  
- **生成 SBOM**：`syft <image>`（默认仅显示镜像最终层内容，加 `--scope all-layers` 可包含所有层）；  
- **输出格式**：使用 `-o` 参数指定格式（如 `-o cyclonedx-json`）。  

**支持的生态系统**  
涵盖 Alpine、Debian、Go、Python、Java、JavaScript、Ruby 等主流开发环境及包管理工具。  

**许可证**  
采用 Apache-2.0 开源协议，由 Anchore 赞助维护。