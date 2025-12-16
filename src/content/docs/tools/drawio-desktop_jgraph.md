
---
title: drawio-desktop
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jgraph/drawio-desktop?style=social) ](https://github.com/jgraph/drawio-desktop)
### [jgraph drawio-desktop](https://github.com/jgraph/drawio-desktop)

**核心内容总结：**  
1. **项目功能**：drawio-desktop 是基于 Electron 的桌面图表工具，封装了 draw.io 的核心编辑器，支持下载安装包（通过 GitHub 发布页面获取）。  

2. **使用方法**：  
   - 直接下载 GitHub 发布页面的二进制文件安装使用。  
   - 开发者需递归克隆项目（`git clone --recursive`），执行 `npm install` 和 `npm start` 启动应用。  

3. **主要特性**：  
   - **安全性**：应用与互联网隔离（仅更新时连接 GitHub 和 AWS S3），禁止外部 JavaScript 运行，不传输任何用户数据或使用分析。  
   - **许可**：Apache 2.0 协议，可免费使用（不可修改代码且接受“按原样提供”）。  
   - **本地存储**：数据保存在系统 AppData 目录（macOS：`~/Library/Application Support/draw.io`；Windows：`C:\Users\<用户>\AppData\Roaming\draw.io\`）。  

4. **开发与发布**：  
   - 依赖 draw.io 子模块，需更新版本并打标签。  
   - 构建完成后需手动签名 Windows 安装包并上传至 GitHub 发布页面。  

5. **贡献政策**：项目不接受外部贡献（除非维护者特许），因代码复杂度高，需严格测试，仅接受 bug 报告和功能建议。