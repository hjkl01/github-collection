### [kulala.nvim](https://github.com/mistweaverco/kulala.nvim) ![GitHub Repo stars](https://img.shields.io/github/stars/mistweaverco/kulala.nvim?style=social)

`kulala.nvim` 是一个运行在 Neovim 中的全功能请求客户端，支持 HTTP、GraphQL、gRPC、WebSocket 和流式请求，并兼容 JetBrains `.http` 规范与 IntelliJ HTTP Client。

它的核心功能包括：在编辑器内直接发送和管理请求；支持环境变量、文档变量、请求变量、动态变量、提示输入及 `http-client.env` 文件；可导入、运行和保存外部 `*.http` 请求及请求/响应数据；支持 JavaScript 和 Lua 脚本，用于请求前、请求后、条件判断、内联和外部脚本场景；提供多种认证方式，如 Basic、Bearer、Digest、NTLM、OAuth2、AWS 和 SSL。

此外，它还支持响应格式化与实时过滤、断言与自动化测试及报告、内置 LSP 补全和格式化、与 Postman、OpenAPI、Bruno 的导入导出、CLI 工具和 CI 集成，以及用于快速发起请求的 scratchpad。项目目标是结合独立的语言服务器和格式化工具，为 Neovim 提供完整、高兼容性的 REST/接口调试体验。