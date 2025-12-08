
---
title: nicegui
---

### [zauberzeug nicegui](https://github.com/zauberzeug/nicegui)

**核心内容总结：**  
NiceGUI 是一个基于 Python 的 Web UI 框架，可在浏览器中显示界面，支持创建按钮、图表、3D 场景、表格等元素，适用于微服务应用、仪表盘、机器人项目等场景。  

**功能与特性：**  
- 自动代码修改后页面重载，无需手动刷新  
- 支持 Web 服务器模式（浏览器访问）或本地窗口模式  
- 提供丰富 UI 组件（标签、按钮、输入框、文件上传等）及高级功能（实时图表、3D 渲染、虚拟摇杆控制等）  
- 支持数据绑定、定时刷新、用户通知、自定义颜色主题等  
- 可集成到 Jupyter Notebook，支持 pytest 测试框架  

**使用方法：**  
1. 安装：`python3 -m pip install nicegui`  
2. 编写代码（如 `main.py`）：  
   ```python  
   from nicegui import ui  
   ui.label('Hello NiceGUI!')  
   ui.run()  
   ```  
3. 运行后通过浏览器访问 `http://localhost:8080`  

**其他：**  
- 官方文档和示例项目提供详细教程与演示  
- 基于 FastAPI、Vue/Quasar 构建，依赖 ASGI 框架（Starlette/Uvicorn）  
- 开源项目，支持社区贡献与赞助