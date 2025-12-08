
---
title: pdf2htmlEX
---

### [pdf2htmlEX pdf2htmlEX](https://github.com/pdf2htmlEX/pdf2htmlEX)

**项目核心内容总结：**  
pdf2htmlEX 是一个将 PDF 文件转换为 HTML 的工具，利用现代 Web 技术实现高精度渲染，支持学术论文、杂志等复杂布局文档。  

**功能与特性：**  
- 支持原生 HTML 文本，保留精确字体和位置信息；  
- 灵活输出模式：可生成单个 HTML 文件或按需加载页面（需 JavaScript）；  
- 优化文件大小，通常小于 PDF，支持链接、书签、打印、SVG 背景、Type 3 字体等；  
- 改进处理遮挡文本（如 `--correct-text-visibility` 参数控制可见性）；  
- 支持 CJK 字符（如中文），适用于多语言文档。  

**使用方法：**  
- 推荐参数：`--font-size-multiplier 1 --zoom 25` 以避免浏览器舍入误差；  
- 可通过 `--covered-text-dpi` 调整遮挡文本的渲染精度；  
- 建议修改 FontForge 防止生成时间戳，并通过去重减少 HTML 文件体积。  

**许可证：**  
项目整体采用 GPLv3+ 许可证，部分资源文件使用更宽松的许可证。