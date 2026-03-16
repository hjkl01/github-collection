### [kevin1024 vcrpy](https://github.com/kevin1024/vcrpy)  ![GitHub Repo stars](https://img.shields.io/github/stars/kevin1024/vcrpy?style=social)

VCR.py 是 Ruby VCR 库的 Python 实现，旨在简化并加速涉及 HTTP 请求的测试。其工作原理是：在首次测试运行时，记录所有通过的 HTTP 交互并序列化保存为文件（称为 cassette）；在后续运行中，读取该文件并拦截匹配的 HTTP 请求，直接返回预设响应，而无需实际发起网络请求。这提供了离线测试能力、确保测试完全确定，并显著提升了测试执行速度。若被测 API 发生变更，只需删除 cassette 文件并重新运行测试即可自动更新记录。