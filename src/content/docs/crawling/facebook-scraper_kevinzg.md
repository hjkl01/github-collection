
---
title: facebook-scraper
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kevinzg/facebook-scraper?style=social) ](https://github.com/kevinzg/facebook-scraper)
### [kevinzg facebook-scraper](https://github.com/kevinzg/facebook-scraper)

**项目核心内容总结：**

**功能**  
该项目是一个用于抓取Facebook数据的Python库，支持抓取用户动态（如帖子、评论）、用户资料、群组信息等。主要功能包括：  
- 抓取用户主页、群组或页面的帖子及评论；  
- 提取用户资料信息（如教育背景、工作经历）；  
- 获取群组详情（如管理员、成员数）；  
- 支持将抓取数据保存为CSV或JSON文件。  

**使用方法**  
1. **基础抓取**：通过`get_posts()`函数抓取用户或群组的帖子，可设置参数（如分页、时间范围、过滤规则）。  
2. **评论抓取**：在抓取帖子时，使用`options={'comments': True}`获取评论内容。  
3. **用户资料**：调用`get_profile()`提取用户个人信息，需提供账号名或ID。  
4. **群组信息**：使用`get_group_info()`获取群组详情，如管理员列表、成员数。  
5. **写入文件**：通过`write_posts_to_csv()`直接保存数据到本地，并支持断点续传（通过`resume_file`参数）。  

**主要特性**  
- **无需API密钥**：直接通过网页解析实现数据抓取；  
- **支持登录状态**：通过`cookies`参数模拟登录，可获取更多隐私信息（如用户生日）；  
- **大规模数据处理**：分页抓取并保存数据，支持中断后恢复；  
- **灵活过滤**：通过正则表达式（`matching`/`not_matching`）筛选目标内容；  
- **多格式输出**：支持CSV/JSON格式导出，可自定义保存字段。  

**注意事项**  
- 抓取时需遵守Facebook使用条款，避免触发反爬机制；  
- 部分功能（如评论抓取）需设置`allow_extra_requests=True`以获取完整数据；  
- 需自行处理验证码或登录验证问题。