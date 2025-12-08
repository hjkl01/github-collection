
---
title: selenium-wire
---

### [wkeeling selenium-wire](https://github.com/wkeeling/selenium-wire)

**项目核心内容总结：**  
**功能：**  
Selenium Wire 是一个用于浏览器自动化测试的工具，可拦截和处理 HTTP/HTTPS 请求与响应，支持 HTTPS 解密、请求/响应修改、HAR 数据捕获，并提供代理配置、证书管理等功能。  

**使用方法：**  
1. 安装：`pip install selenium-wire`  
2. 在代码中通过 `seleniumwire_options` 配置参数（如代理、存储路径、证书路径等），结合 Selenium WebDriver 使用。  
3. 使用 `driver.requests` 拦截请求，或通过 `driver.har` 获取 HAR 归档数据。  
4. 支持与 `undetected-chromedriver` 集成，规避反爬虫检测。  

**主要特性：**  
- 自动解密 HTTPS 流量（需浏览器信任证书）；  
- 支持内存或磁盘存储捕获数据；  
- 可自定义代理服务器及证书；  
- 提供 HAR 归档功能，便于调试与分析；  
- 可绕过反爬虫机制（通过 `undetected-chromedriver`）；  
- 支持忽略特定 HTTP 方法（如 OPTIONS）或禁用请求压缩。