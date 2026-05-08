### [RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) ![GitHub Repo stars](https://img.shields.io/github/stars/elebumm/RedditVideoMakerBot?style=social)

该项目是一个自动化生成 Reddit 题材短视频的机器人：可从 Reddit 获取帖子内容并自动完成视频制作流程（无需手动剪辑或素材整合），最终输出可上传的视频文件。  
目前不支持自动发布到 TikTok/YouTube/Instagram，只提供本地生成结果并需手动上传。  

核心可配置功能包括：  
- 选择指定 subreddit 与指定帖子（非随机）；  
- 选择背景画面与背景音乐；  
- 选择语音；  
- 明暗主题模式；  
- NSFW 内容过滤；  
- 检查视频是否已生成，避免重复制作。  

项目基于 Python 3.10 与 Playwright，首次运行通过 Reddit API 配置后即可使用，后续可通过 `config.toml` 重新配置。