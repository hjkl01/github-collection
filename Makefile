# 可配置变量
PYTHON := python3.12
PIP := pip3

# 虚拟环境
VENV := .venv
ACTIVATE := . $(VENV)/bin/activate

.PHONY: install run build deploy help export

help:
	@echo "📋 可用命令:"
	@echo ""
	@echo "  make install      安装开发依赖并激活虚拟环境"
	@echo "  make crawl        抓取 GitHub Trending"
	@echo "  make gene         启动文章解析"
	@echo "  make run          执行 crawl + gene"
	@echo "  make build        构建静态站点 (zensical build)"
	@echo "  make deploy       构建并部署到 GitHub Pages"
	@echo "  make export       从 md 文件导出 URL 到 urls.txt"
	@echo "  make clean-cache  清理缓存"
	@echo ""

install:
	@echo "📦 安装开发依赖..."
	uv sync
	@echo "✅ 依赖安装完成，激活环境：source $(VENV)/bin/activate"

crawl:
	@echo "🚀 抓取trending..."
	$(ACTIVATE) && uv run python main.py crawl

gene:
	@echo "🚀 启动解析..."
	$(ACTIVATE) && uv run python main.py

run: crawl gene build
	@echo "🚀 启动服务run\crawl..."

build:
	@echo "🏗️ 构建静态站点..."
	$(ACTIVATE) && uv run zensical build

deploy: build
	@echo "🚀 部署到 GitHub Pages..."
	@cd site && rm -rf .git && git init && git add -A && git commit -m "Deploy to GitHub Pages" && git remote add origin ssh://git@ssh.github.com:443/hjkl01/github-collection.git && git push -f origin HEAD:gh-pages

export:
	@echo "📤 导出 URL..."
	$(ACTIVATE) && uv run python main.py export

clean-cache:
	@echo "🚀 清理缓存..."
	rm -rf src/content/docs/00
