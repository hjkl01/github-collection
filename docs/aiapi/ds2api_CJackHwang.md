### [ds2api](https://github.com/CJackHwang/ds2api) ![GitHub Repo stars](https://img.shields.io/github/stars/CJackHwang/ds2api?style=social)

DS2API 是一个将 DeepSeek Web 对话能力转换为 **OpenAI、Claude、Gemini 兼容 API** 的网关服务。项目后端使用 Go 全量实现，提供 React WebUI 管理台（`/admin`）。

核心功能包括：  
- 提供 OpenAI/Claude/Gemini 多协议兼容接口与统一转译能力  
- 支持多账号托管与轮询（邮箱/手机号登录、token 自动刷新）  
- 提供并发槽位与等待队列控制，超载时返回 429  
- 内置高性能 DeepSeek PoW（纯 Go）  
- 支持 Tool Calling 适配与防泄漏处理，兼容流式输出  
- 提供 Admin API：配置管理、热更新、代理管理、账号测试、会话清理、导入导出、Vercel 同步、版本检查等  
- 提供健康检查与就绪探针（`/healthz`、`/readyz`）  
- 支持模型别名映射（如 GPT/Claude/Gemini 常见模型名映射到 DeepSeek 模型）  
- 支持两种鉴权：托管 key 模式与直通 token 模式  

部署方式覆盖：Release 二进制、Docker/Zeabur、Vercel、本地源码运行；以 `config.json` 作为统一配置源，并支持环境变量注入（含 Base64 配置）。项目兼容主流 SDK 与框架（OpenAI SDK、Anthropic SDK、Gemini SDK、Vercel AI SDK、LangChain/LlamaIndex/OpenWebUI）。