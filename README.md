# Zensical Project

GitHub Trending 爬虫与静态站点生成器。

## 功能特性

- **爬取 GitHub Trending**：自动抓取 GitHub 热门仓库
- **AI 文章生成**：使用 OpenAI API 将 README 转换为中文 Markdown 格式
- **自动分类**：根据项目类型自动归类到不同分类目录
- **静态站点生成**：使用 zensical 构建静态站点
- **一键部署**：支持部署到 GitHub Pages

## 快速开始

### 环境要求

- Python 3.12+
- uv 包管理器

### 安装

```bash
make install
```

### 配置

复制 `.env.example` 为 `.env`，填入以下环境变量：

```bash
# OpenAI API (可选，使用 dashscope 时留空)
OPENAI_API_KEY=your_openai_api_key
OPENAI_API=https://api.openai.com
OPENAI_MODEL=gpt-4o-mini

# DashScope API (可选，使用 openai 时留空)
DASHSCOPE_API_KEY=your_dashscope_api_key

# GitHub Token (可选，用于提升 API 限流)
GITHUB_TOKEN=your_github_token
```

### 使用

```bash
# 抓取 GitHub Trending
make crawl

# 解析生成 Markdown 文章
make gene

# 执行完整流程 (crawl + gene)
make run

# 构建静态站点
make build

# 部署到 GitHub Pages
make deploy

# 从 md 文件导出 URL
make export

# 清理缓存
make clean-cache
```

## 项目结构

```
├── api/                    # API 模块
│   ├── api_ai.py          # AI 接口封装
│   ├── config.py          # 配置管理
│   ├── github_trending_scraper.py  # GitHub Trending 爬虫
│   └── prompts.py         # AI 提示词
├── docs/                   # 生成的 Markdown 文章
├── src/                    # zensical 源码
├── site/                   # 构建输出的静态站点
├── main.py                 # 主程序入口
├── Makefile               # 命令行工具
└── pyproject.toml         # 项目配置
```

## 命令行用法

```bash
# 抓取 Trending
python main.py crawl

# 生成文章
python main.py

# 导出 URL
python main.py export

# 分类现有文件
python main.py cate
```

## 部署到 GitHub Pages

```bash
make deploy
```

这会：
1. 构建静态站点 (`make build`)
2. 将 `site` 目录推送到 `gh-pages` 分支
3. 自动启用 GitHub Pages（需在 GitHub 仓库设置中选择 gh-pages 分支）