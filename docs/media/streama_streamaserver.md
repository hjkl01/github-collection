### [streamaserver streama](https://github.com/streamaserver/streama)  ![GitHub Repo stars](https://img.shields.io/github/stars/streamaserver/streama?style=social)

Streama 是一款自托管的流媒体服务器软件，旨在打造个人专属的 Netflix 体验。核心功能如下：

1. **媒体管理**：集成 theMovieDB API 自动填充元数据和海报，支持视频文件拖拽上传或直接映射本地目录批量导入。
2. **播放体验**：基于 HTML5 的播放器，提供 Netflix 风格的剧集/季浏览界面，支持播放控制及观看进度记录（继续观看）。
3. **用户权限**：内置管理面板，支持创建用户并分配权限，区分管理员（可添加内容）与普通用户（仅浏览）。
4. **系统配置**：支持自定义上传目录、API 密钥及文件匹配正则表达式，后端基于 Grails 3 与 SpringSecurity，前端使用 AngularJS。