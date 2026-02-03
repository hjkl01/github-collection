
---
title: zerobrew
---

### [lucasgelfond zerobrew](https://github.com/lucasgelfond/zerobrew)  ![GitHub Repo stars](https://img.shields.io/github/stars/lucasgelfond/zerobrew?style=social)

**项目名称**：zerobrew  
**项目简介**：zerobrew 是一个快速、现代的 macOS 包管理器，基于 Homebrew 的 CDN，但性能显著提升。它通过内容地址存储（Content-Addressable Store）和并行处理实现快速安装与卸载，可作为 `brew` 的替代品，使用方式兼容 Homebrew。

---

### **核心功能**

- **快速安装**：通过 SHA256 哈希存储包，重复安装几乎无耗时。
- **支持命令**：支持安装、卸载、批量安装、从 Brewfile 安装、清理等。
- **兼容性**：可直接使用 `brew` 的命令替换为 `zb`，如 `zb install jq`。

---

### **使用方法**

- 安装 zerobrew：
  ```bash
  curl -sSL https://raw.githubusercontent.com/lucasgelfond/zerobrew/main/install.sh | bash
  ```

- 常用命令：
  ```bash
  zb install jq                  # 安装单个包
  zb install wget git            # 安装多个包
  zb install --file Brewfile     # 从 Brewfile 安装
  zb bundle                      # 当前目录下读取 Brewfile
  zb uninstall jq                # 卸载包
  zb reset                       # 卸载所有包
  zb gc                          # 清理未使用的存储项
  zbx jq --version               # 不链接直接运行
  ```

- Brewfile 示例（兼容 Homebrew）：
  ```
  # Brewfile
  jq
  wget
  git
  ```

---

### **主要特性**

- **内容地址存储**：包按 SHA256 哈希存储，避免重复下载。
- **APFS 克隆文件**：使用写时复制技术，节省磁盘空间。
- **并行下载**：多个连接并行下载，提高效率。
- **流式执行**：下载、解压、链接同步进行，提高速度。

---

### **性能优势**

- 性能提升显著，冷安装平均快 2x，热安装快 7.6x。
- 举例：
  - `ffmpeg` 冷安装 3.0s，热安装 0.7s。
  - `tesseract` 热安装快 29.5x。

---

### **项目状态**

- 实验性，支持大多数核心 Homebrew 包。
- 欢迎提交 issue 或 PR。

---

### **构建与测试**

- 源码构建：
  ```bash
  cargo build --release
  cargo install --path zb_cli
  ```

- 基准测试：
  ```bash
  ./benchmark.sh
  ```

---

### **许可证**

- 采用 Apache 或 MIT 双许可证，任选其一。