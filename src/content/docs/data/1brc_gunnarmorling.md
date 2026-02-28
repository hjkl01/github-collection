
---
title: 1brc
---

### [gunnarmorling 1brc](https://github.com/gunnarmorling/1brc)  ![GitHub Repo stars](https://img.shields.io/github/stars/gunnarmorling/1brc?style=social)

**项目名称：十亿行挑战 (The One Billion Row Challenge, 1BRC)**

**项目核心功能**
这是一个旨在探索现代 Java 处理大数据聚合计算极限性能的编程挑战。目标要求编写一个 Java 程序，高效读取包含 10 亿行气象站温度测量值的文本文件（约 12GB），计算每个站点的温度最小值、平均值和最大值，并按站名字母顺序输出统计结果。

**主要特性与规则**
1. **语言限制**：仅使用 Java 21，禁止使用外部库依赖，所有逻辑必须在单一源文件中实现。
2. **计算约束**：必须在应用运行时进行数据计算，禁止在构建时（如 GraalVM 编译期）预计算结果。
3. **优化技术**：鼓励使用虚拟线程、SIMD 指令集、垃圾回收调优、内存映射、GraalVM 原生镜像（Native Image）及 Unsafe 等高级优化手段。
4. **数据规范**：输入为 UTF-8 编码文本，格式为 `<站名>;<温度>`（一位小数），支持任意合法数据分布；输出一位小数精度的 `<min>/<mean>/<max>` 结果。

**使用方法**
1. **环境构建**：安装 Java 21，使用 Apache Maven 执行 `./mvnw clean verify` 构建项目。
2. **数据生成**：运行脚本 `./create_measurements.sh 1000000000` 生成包含 10 亿行数据的测试文件。
3. **基线测试**：运行 `./calculate_average_baseline.sh` 作为性能对比基准（约 2 分钟）。
4. **优化提交**：修改 `CalculateAverage` 程序以提升速度，确保通过测试套件 `./test.sh` 后提交至仓库。
5. **官方评测**：代码将在指定硬件（Hetzner AX161 服务器，8 核）的内存盘上运行 5 次取平均值进行排名。

**项目现状与结果**
挑战已于 2024 年 1 月 31 日截止。在 8 核 AMD EPYC 服务器环境下，官方评测结果显示：
- **基线实现**：耗时约 2 分钟。
- **最优实现**（使用 GraalVM 原生二进制及 Unsafe）：耗时约 1.5 秒。
最终排行榜及相关参与者的实现细节已公开，获奖者将获赠定制 T 恤。