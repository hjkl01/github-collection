
---
title: SheerID-Verification-Tool
---

### [ThanhNguyxn SheerID-Verification-Tool](https://github.com/ThanhNguyxn/SheerID-Verification-Tool)  ![GitHub Repo stars](https://img.shields.io/github/stars/ThanhNguyxn/SheerID-Verification-Tool?style=social)

### 项目核心内容总结

#### **功能**
- 提供自动化验证工具，支持 Spotify、YouTube、Google One、Bolt.new、Canva 教育版等平台的学生、教师、退伍军人身份验证。
- 包含多个子工具，针对不同用户群体（如大学生、K12教师、退伍军人）设计验证策略。
- 支持生成虚拟身份信息（姓名、出生日期、邮箱）、上传伪造证明文件（学生证、教师证书等）。

#### **使用方法**
1. 克隆仓库并安装依赖：  
   ```bash
   git clone https://github.com/ThanhNguyxn/SheerID-Verification-Tool.git
   pip install httpx Pillow
   ```
2. 可选安装反检测模块：  
   ```bash
   pip install curl_cffi cloudscraper
   ```
3. 运行具体工具（以 Spotify 为例）：  
   ```bash
   cd spotify-verify-tool
   python main.py "YOUR_SHEERID_URL"
   ```

#### **主要特性**
1. **验证流程**  
   - 五步标准化流程：生成身份数据 → 提交信息 → 跳过 SSO 登录 → 上传证明文件 → 完成验证。
2. **智能策略**  
   - 根据目标平台（如 Spotify、YouTube）选择高校名单（含 45+ 国家/地区高校）。
   - 教师验证生成“就业证明”，K12 教师可自动通过验证。
   - 退伍军人验证严格匹配国防部数据库。
3. **反检测模块**  
   - 随机 User-Agent、TLS 指纹伪装（使用 `curl_cffi`）、请求延迟随机化。
   - 自动选择最佳 HTTP 库（优先 `curl_cffi`）。

#### **注意事项**
- 项目仅用于教育目的，禁止用于非法用途。
- 推荐搭配住宅代理和 `curl_cffi` 提高验证成功率。