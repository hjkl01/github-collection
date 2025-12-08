
---
title: lighthouse
---

### [GoogleChrome lighthouse](https://github.com/GoogleChrome/lighthouse)

Lighthouse是一款用于审计网页性能和质量的工具，支持运行性能、可访问性、SEO等多维度检查，并生成详细报告。核心功能包括：  
1. **性能评估**：模拟移动设备4G网络环境，分析页面加载速度、资源优化等指标；  
2. **报告生成**：提供HTML、JSON格式报告，支持集成到CI/CD流程（如GitHub Actions、CircleCI）；  
3. **扩展性**：允许自定义审计规则，通过插件或脚本扩展功能；  
4. **本地运行**：所有数据处理在本地完成，不上传至远程服务器；  
5. **多语言支持**：通过Intl API适配不同语言环境。  

**使用方法**：  
- 命令行工具直接运行审计；  
- 集成到Webpack、Gradle等构建工具；  
- 与Chrome DevTools、WebPageTest等工具联动。  

**主要特性**：  
- 支持网络限速模拟（4G/3G/2G）；  
- 提供性能评分、优化建议及改进方案；  
- 可通过配置调整审计规则和阈值；  
- 支持自动化测试与持续集成。