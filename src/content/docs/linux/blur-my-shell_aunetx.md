
---
title: blur-my-shell
---

### [aunetx blur-my-shell](https://github.com/aunetx/blur-my-shell)

**核心内容总结：**

**项目功能**  
GNOME Shell扩展“Blur my Shell”为GNOME桌面环境添加模糊效果，支持对顶部面板、启动器、概览界面、窗口选择器、锁屏界面等组件进行静态或动态模糊处理，提升视觉效果与个性化体验。  

**主要特性**  
1. **模糊类型**：  
   - **静态模糊**：基于壁纸静态图像应用多级效果（如高斯模糊、像素化、圆角等），支持自定义效果顺序和参数。  
   - **动态模糊**：直接对组件后方内容进行实时模糊，仅支持高斯模糊，但可能产生黑框伪影，可通过“Hack等级”优化。  

2. **兼容性**：  
   - 支持主流扩展（如Dash to Dock、Dash to Panel、Hide Top Bar等），并提供针对性配置选项。  

3. **高级配置**：  
   - 自定义面板/启动器背景颜色、模糊触发条件（如全屏时关闭面板模糊）、应用窗口模糊模式（白名单/黑名单）。  

**使用方法**  
- 通过[GNOME扩展商店](https://extensions.gnome.org/extension/3193/blur-my-shell/)安装，或从源码安装：  
  ```sh  
  git clone https://github.com/aunetx/blur-my-shell  
  cd blur-my-shell  
  make install  
  ```  
  安装后需重启GNOME Shell（如`Alt+F2`输入`r`）。  

**版本支持**  
- 主分支支持GNOME Shell 46，其他历史版本可通过标签（如`v58`、`v47`等）兼容GNOME 3.38至46。  

**注意事项**  
- 静态模糊性能较高，动态模糊可能影响流畅度；  
- 部分模糊效果（如圆角）仅适用于静态模糊；  
- 需注意模糊与窗口透明度、扩展冲突的兼容性。