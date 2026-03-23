### [SYSTRAN faster-whisper](https://github.com/SYSTRAN/faster-whisper)  ![GitHub Repo stars](https://img.shields.io/github/stars/SYSTRAN/faster-whisper?style=social)

faster-whisper 是基于 CTranslate2 实现的高性能 Whisper 模型重新封装。相比原版，它在相同精度下快 4 倍且内存占用更低，支持 GPU 和 CPU 加速及 8-bit 量化。项目提供 Python 库，支持批量转录、单词级时间戳、VAD 语音过滤等功能，无需安装 FFmpeg。支持从 Hugging Face Hub 加载模型或自定义转换模型。