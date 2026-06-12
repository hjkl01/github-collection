### [OpenMontage](https://github.com/calesthio/OpenMontage) ![GitHub Repo stars](https://img.shields.io/github/stars/calesthio/OpenMontage?style=social)

OpenMontage 是一个开源的智能体式视频制作系统，可把 AI 编码助手变成完整的视频生产工作室。用户只需用自然语言描述需求，系统就能完成选题研究、脚本撰写、分镜规划、素材生成或检索、剪辑、字幕、配音、配乐与最终渲染，并在关键创意决策点保留人工确认。

它不仅能生成基于图片动画的视频，还能通过免费或开源素材源构建真正的“动态视频”：自动从 Archive.org、NASA、Wikimedia、Pexels、Unsplash 等来源检索真实运动镜头，整理为可搜索素材库后剪成完整成片。支持从参考视频出发，分析节奏、场景、风格和结构，生成差异化创作方案、成本预估和样片建议。

项目内置 12 条完整生产流水线，覆盖动画解说、动态图形、品牌预告、纪实蒙太奇、播客切片、口播视频、本地化配音、屏幕演示等场景。统一流程为：研究、提案、脚本、分镜、素材、剪辑、合成。系统依靠 YAML 流水线定义和 Markdown 技能文件驱动，AI 助手本身就是调度器，可调用 Python 工具完成执行、审查和状态检查点保存。

OpenMontage 兼容免费本地方案和云端服务。零 API Key 也能使用 Piper TTS、FFmpeg、Remotion、HyperFrames 以及开放素材源生成完整视频；如果配置额外密钥，还可接入 FLUX、Runway、Veo、Kling、OpenAI、Google、ElevenLabs、Suno 等图像、视频、语音和音乐服务。系统会根据任务、质量、控制能力、可靠性、成本、延迟和连续性 7 个维度自动评分选择最合适的提供商。

它强调生产级治理能力，包括成本预估与预算上限、逐步审批、决策审计日志、渲染前校验、渲染后自检、字幕检查、音频分析、黑帧检测和“幻灯片风险”评估，避免输出低质量或与承诺不符的视频。整体目标是用可审计、可扩展、可替换的开源架构，让 AI 助手像真实制作团队一样完成端到端视频生产。