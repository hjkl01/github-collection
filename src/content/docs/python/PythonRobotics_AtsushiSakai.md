
---
title: PythonRobotics
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/AtsushiSakai/PythonRobotics?style=social) ](https://github.com/AtsushiSakai/PythonRobotics)
### [AtsushiSakai PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)

**核心内容总结：**  
该项目是一个基于Python的机器人算法实现库，涵盖路径规划、路径跟踪、SLAM、避障、机械臂控制、空中导航等多个领域。主要功能包括：  
1. **路径规划**：支持多种算法（如A*、RRT*、Frenet最优轨迹生成）及复杂场景（动态障碍物、多关节机械臂避障）。  
2. **路径跟踪**：提供Stanley控制、LQR、MPC等控制方法，适用于车辆、无人机等系统的轨迹跟踪。  
3. **交互模拟**：支持点击设置目标点、实时调整参数，包含2D/3D可视化（如机械臂、无人机轨迹）。  
4. **模块化设计**：代码按功能（如导航、控制、臂部操作）分类，便于扩展和复用。  
5. **多场景应用**：覆盖地面车辆、无人机、火箭着陆、双足机器人等典型应用场景。  

**使用方法**：  
- 直接运行示例代码，通过修改参数调整算法行为。  
- 支持交互式操作（如点击设置目标点）。  
- 可集成至自研机器人项目，引用时需注明学术出处。  

**主要特性**：  
- 提供完整算法实现（含PID、模型预测控制、非线性优化等）。  
- 开源且免费（MIT许可证），支持社区贡献。  
- 文档详细，包含技术文档、使用案例及引用方式。