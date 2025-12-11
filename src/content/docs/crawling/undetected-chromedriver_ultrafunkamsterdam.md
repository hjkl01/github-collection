
---
title: undetected-chromedriver
---

### [ultrafunkamsterdam undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

**项目核心内容总结：**

**项目功能**  
该项目是一个用于规避网站反爬虫检测的ChromeDriver工具库，通过修改ChromeDriver行为，使自动化脚本更难以被反爬系统（如DistilNetworks、DataDome）识别。

**主要特性**  
1. 支持指定Chrome版本，适配不同浏览器环境  
2. 提供多种使用模式（普通模式、MonkeyPatch模式）  
3. 支持自定义配置（如代理设置、驱动路径）  
4. 无头模式（Headless）兼容性优化  
5. 内置反检测机制，提升自动化脚本隐蔽性  

**使用方法**  
1. 基础用法：直接导入库并初始化Chrome驱动  
2. 版本控制：通过`uc.TARGET_VERSION`指定Chrome版本  
3. 高级配置：可设置驱动路径、添加代理参数等  
4. MonkeyPatch模式：需在导入Selenium前调用`uc.install()`  
5. 示例包含绕过DataDome反爬检测的场景演示