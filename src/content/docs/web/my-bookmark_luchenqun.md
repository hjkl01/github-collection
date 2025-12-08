
---
title: my-bookmark
---

### [luchenqun my-bookmark](https://github.com/luchenqun/my-bookmark)

**项目核心内容总结：**  
1. **功能**：提供在线书签管理，支持跨设备/浏览器同步、分类管理、关键词搜索、时间段筛选、公有/私有书签设置、导入导出Chrome书签、备忘录记录、快捷键操作、Chrome插件添加、移动端适配（手机端地址：mb.lucq.fun）。  
2. **使用方法**：  
   - 在线体验：访问 [http://b.lucq.fun/](http://b.lucq.fun/)（账号：test，密码：123456）。  
   - 部署方式：  
     - **Docker**：执行 `docker run -d -p 2000:2000 -p 3306:3306 luchenqun/mybookmark`。  
     - **手动部署**：安装MySQL（UTF-8编码）、Node.js（v12+），执行SQL脚本，配置pm2及数据库连接。  
3. **特性**：  
   - 支持分类排序、书签自动获取标题、快捷键操作（如Insert添加书签、A新增备忘录）。  
   - 技术栈：Node.js（v12.13.0）、MySQL（v5.7.23）、AngularJS（v1.5.8）、Semantic UI（v2.4.0）。  
4. **其他**：开源MIT许可证（手机版未开源），兼容Chrome浏览器，提供Chrome插件（需手动安装）。