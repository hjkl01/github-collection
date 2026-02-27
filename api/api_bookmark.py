#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
from datetime import datetime
from pathlib import Path


def find_chrome_bookmarks():
    """查找Chrome书签文件的位置"""
    # macOS Chrome书签文件通常位于以下位置之一
    possible_paths = [
        Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "Default" / "Bookmarks",
        Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "Profile 1" / "Bookmarks",
        Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "Profile 2" / "Bookmarks",
        Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "Profile 3" / "Bookmarks",
        Path.cwd() / "Bookmarks",
    ]

    for path in possible_paths:
        if path.exists():
            print(f"找到Chrome书签文件: {path}")
            return str(path)

    print("未找到Chrome书签文件，请确保Chrome已安装并使用过")
    print("可能的路径:")
    for path in possible_paths:
        print(f"  - {path}")
    return None


def extract_github_bookmarks(bookmarks_file, output_file):
    """提取包含github.com的书签"""
    try:
        with open(bookmarks_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        roots = data.get("roots", {})
        github_bookmarks = []

        def extract_bookmarks(node, results):
            """递归提取书签"""
            if isinstance(node, dict):
                if node.get("type") == "url":
                    url = node.get("url", "")
                    name = node.get("name", "")
                    if "github.com" in url.lower():
                        results.append({"name": name, "url": url, "type": "bookmark"})

                if "children" in node:
                    for child in node["children"]:
                        extract_bookmarks(child, results)

        for root_node in roots.values():
            if isinstance(root_node, dict):
                extract_bookmarks(root_node, github_bookmarks)

        output_data = {
            "total_count": len(github_bookmarks),
            "bookmarks": github_bookmarks,
            "extracted_at": {
                "timestamp": datetime.now().isoformat(),
                "source": bookmarks_file
            },
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"\n提取完成！")
        print(f"找到 {len(github_bookmarks)} 个包含github.com的书签")
        print(f"结果已保存到: {output_file}")

        if github_bookmarks:
            print(f"\n前5个书签预览:")
            for i, bookmark in enumerate(github_bookmarks[:5]):
                print(f"  {i + 1}. {bookmark['name']}")
                print(f"     {bookmark['url']}\n")

        return True

    except FileNotFoundError:
        print(f"错误: 找不到文件 {bookmarks_file}")
        return False
    except json.JSONDecodeError as e:
        print(f"错误: 无法解析JSON文件 {bookmarks_file}")
        print(f"详细信息: {e}")
        return False
    except Exception as e:
        print(f"发生未知错误: {e}")
        return False


def main():
    """主函数"""
    print("=== Chrome GitHub 书签提取工具 ===")
    print("正在查找Chrome书签文件...")

    bookmarks_file = find_chrome_bookmarks()
    if not bookmarks_file:
        sys.exit(1)

    output_file = Path.cwd() / "github_bookmarks.json"

    print(f"输出文件: {output_file}")
    print("-" * 50)

    success = extract_github_bookmarks(bookmarks_file, str(output_file))

    if success:
        print("\n✅ 操作成功完成！")
    else:
        print("\n❌ 操作失败，请检查错误信息。")
        sys.exit(1)


if __name__ == "__main__":
    main()
