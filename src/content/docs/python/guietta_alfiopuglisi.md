
---
title: guietta
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/alfiopuglisi/guietta?style=social) ](https://github.com/alfiopuglisi/guietta)
### [alfiopuglisi guietta](https://github.com/alfiopuglisi/guietta)

Guietta 是一个简化 Python 图形界面开发的工具，通过直观的布局定义和事件绑定实现快速开发。核心功能包括：通过类似表格的结构定义界面布局（如输入框、按钮等），使用 `with gui.按钮` 语法绑定事件处理逻辑，支持动态更新界面元素（如 `gui.result = ...`）。主要特性涵盖与 matplotlib/pyqtgraph 的图表集成、多窗口支持、异常处理自定义、队列模式（类似 PySimpleGUI）、兼容任意 QT 小部件（包括自定义控件）、后台处理长任务、支持传统 QT 信号槽机制等。安装方式为 `pip install guietta`，部分平台需手动指定 PyQt5 替代 PySide2。