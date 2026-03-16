### [microsoft windows-rs](https://github.com/microsoft/windows-rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/windows-rs?style=social)

本项目旨在为 Rust 语言提供全面的 Windows API 支持。它基于 Windows API 元数据自动生成代码，使 Rust 开发者能像调用普通模块一样，以自然、惯用的方式调用 C 风格、COM 及 WinRT 接口。核心包含 windows-sys（原始绑定）和 windows（安全绑定），并配套提供代码生成、核心类型支持、异步处理、注册表、服务、线程及字符串管理等功能的一系列辅助库，同时集成 C++/WinRT 编译器绑定。