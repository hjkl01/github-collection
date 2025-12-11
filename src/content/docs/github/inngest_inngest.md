
---
title: inngest
---

### [inngest inngest](https://github.com/inngest/inngest)

**项目核心内容总结：**  
Inngest 是一个用于构建和管理后台任务与工作流的工具，提供多语言 SDK（支持 JavaScript/TypeScript、Python、Go、Kotlin/Java 等），帮助开发者无需依赖基础设施即可编写可靠的任务函数。  

**主要功能与特性：**  
1. **持久函数**：替代传统队列和调度系统，支持任务自动重试、复杂流程控制（如并发、限流、去抖等）。  
2. **本地开发与部署**：通过 `Inngest Dev Server` 实现本地开发环境，支持部署到自托管服务器或与 Inngest 平台同步。  
3. **灵活架构**：包含事件处理、任务执行、状态存储、分布式协调等模块，支持高可用和扩展。  
4. **自托管支持**：提供完整的自托管方案，适用于企业私有化部署需求。  

**使用方法：**  
- 使用 SDK 编写函数逻辑，定义触发条件和流程控制规则。  
- 通过 CLI 工具启动本地开发服务器，测试并调试任务流程。  
- 部署到自托管环境或 Inngest 平台，通过 HTTPS 接收事件并执行任务。  

**许可证**：  
- 服务器和 CLI 采用 Server Side Public License（SSPL）和 Apache 2.0 混合许可。  
- 所有 SDK 仅采用 Apache 2.0 许可证。