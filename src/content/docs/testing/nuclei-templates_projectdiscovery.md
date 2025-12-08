
---
title: nuclei-templates
---

### [projectdiscovery nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)

**项目功能**  
Nuclei Templates 是 Nuclei 扫描器的模板库，用于发现应用程序中的安全漏洞，包含社区和官方提供的模板，支持多种漏洞类型和扫描场景。

**使用方法**  
通过 Nuclei 命令行工具调用模板，例如使用 `-tags` 参数指定扫描类型（如 `kev` 或 `vkev`）扫描已知被利用漏洞，或根据模板分类（如 HTTP、DNS、文件等）进行针对性扫描。

**主要特性**  
1. **覆盖已知漏洞**：支持 CISA 和 VulnCheck 的 KEV 漏洞目录，包含 1496 个相关模板。  
2. **模板丰富**：超过 11,997 个文件，涵盖 873 个目录，支持信息收集、漏洞利用（如 XSS、CVE）、配置暴露等场景。  
3. **社区驱动**：支持用户通过 GitHub 提交模板、报告问题或提出功能需求，贡献者可直接参与模板开发。  
4. **多类型支持**：包含文件、HTTP、DNS、代码分析等模板类型，支持不同严重程度（如 critical、high、low）。