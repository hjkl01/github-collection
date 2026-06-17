### [career-ops](https://github.com/santifer/career-ops) ![GitHub Repo stars](https://img.shields.io/github/stars/santifer/career-ops?style=social)

Career-Ops是一个AI驱动的求职命令行工具，将任何AI编码CLI转换为完整的求职指挥中心。

核心功能：

- **职位评估**：10个维度A-F评分系统（角色匹配度、薪资研究、个人化策略、面试准备等），评分低于4.0建议跳过
- **ATS简历生成**：关键词注入的PDF简历，自动针对每个职位描述定制
- **求职信生成**：研究驱动的求职信，含关键词镜像和四种互动角度提示
- **招聘平台扫描**：预配置45+公司（Anthropic、OpenAI、Mistral等），支持Ashby、Greenhouse、Lever等
- **批量处理**：并行评估10+个职位
- **追踪系统**：单一真相来源，自动合并、去重、状态规范化
- **面试准备**：STAR故事库（5-10个核心故事应对所有行为面试问题）
- **谈判脚本**：薪资谈判框架、地区薪资差异反驳、竞品offer杠杆
- **仪表盘TUI**：终端界面浏览、筛选、排序申请状态

工作流程：粘贴职位URL或描述 → 自动角色分类 → AI评估简历匹配度 → 生成报告、PDF、更新追踪器。

支持Claude Code、Gemini CLI、OpenCode等AI CLI。完全本地运行，不自动提交申请，始终由用户决定。