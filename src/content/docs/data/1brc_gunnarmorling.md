
---
title: 1brc
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gunnarmorling/1brc?style=social) ](https://github.com/gunnarmorling/1brc)
### [gunnarmorling 1brc](https://github.com/gunnarmorling/1brc)

该项目名为“1BRC”（One Billion Row Challenge），旨在测试Java处理超大规模数据集的性能。其核心功能是处理包含十亿行数据的文件（如CSV格式），并完成统计计算（如计算平均值）。主要特性包括：提供基准测试工具、支持多种Java优化技术（如并行处理、内存优化）、允许使用G1垃圾回收器等。使用方法包括生成测试数据、运行Java程序进行处理，并通过工具记录性能结果。评估环境基于Fedora 39操作系统，使用特定硬件配置（如8核CPU）进行对比。项目目标是探索Java在大数据处理中的极限，并分享优化策略（如减少对象创建、使用原生类型、避免锁竞争）。