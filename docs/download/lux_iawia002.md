### [lux](https://github.com/iawia002/lux) ![GitHub Repo stars](https://img.shields.io/github/stars/iawia002/lux?style=social)

Lux 是一个使用 Go 开发的高速、简洁命令行下载工具，主要用于下载多平台视频，也支持部分图片和音频资源。  
核心功能包括：按 URL 下载、查看可选清晰度并指定码流下载、批量 URL 下载、播放列表下载（可指定范围）、断点续传、失败自动重试、多线程下载、代理支持、Cookie/Referrer 设置、输出路径与文件名自定义、调试模式、JSON 数据导出、字幕下载与嵌入（部分站点）。  
工具支持通过 go install、Homebrew、AUR、Scoop、Chocolatey 等方式安装，依赖 FFmpeg 进行最终文件合并。  
已适配大量国内外网站（如抖音、B站、优酷、YouTube、微博、腾讯视频、TikTok、Instagram、Twitter 等），并对部分站点提供 VIP/登录 Cookie 场景支持。  
已知问题主要在优酷（ccode 常变）与西瓜/头条（通常需携带有效 Cookie）下载场景。