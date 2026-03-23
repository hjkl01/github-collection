from typing import Union
import json
import time
import base64

import httpx
from tenacity import retry, stop_after_attempt, wait_fixed

from .config import logger, GITHUB_TOKEN, OPENAI_API, OPENAI_API_KEY, OPENAI_MODEL
from .prompts import CATEGORY_PROMPT


# 预编译正则表达式
GITHUB_URL_PATTERN = r"https?://github\.com/([^/]+)/([^/?#]+)(?:[/?#].*)?"


def extract_github_info(github_url: str) -> tuple[str | None, str | None]:
    """解析 GitHub URL，提取用户名和仓库名"""
    import re

    match = re.match(GITHUB_URL_PATTERN, github_url.strip())
    if match:
        return match.group(1), match.group(2)
    return None, None


class httpxClient:
    """异步 HTTP 客户端单例"""

    _instance: httpx.AsyncClient | None = None
    _github_client: httpx.AsyncClient | None = None

    @classmethod
    async def get_github_client(cls) -> httpx.AsyncClient:
        if cls._github_client is None:
            cls._github_client = httpx.AsyncClient(
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}",
                    "Accept": "application/vnd.github.v3+json",
                },
                timeout=30.0,
            )
        return cls._github_client

    @classmethod
    async def get_openai_client(cls) -> httpx.AsyncClient:
        if cls._instance is None:
            cls._instance = httpx.AsyncClient(
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json",
                },
                timeout=300.0,
            )
        return cls._instance

    @classmethod
    async def close(cls):
        if cls._instance:
            await cls._instance.aclose()
            cls._instance = None
        if cls._github_client:
            await cls._github_client.aclose()
            cls._github_client = None


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def api_github_readme(owner: str, repo: str) -> str | None:
    """异步获取 GitHub 仓库的 README 内容"""
    logger.debug(f"{owner=} {repo=}")
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    client = await httpxClient.get_github_client()

    resp = await client.get(url)
    if resp.status_code != 200:
        logger.error(f"无法获取 README: HTTP {resp.status_code}")
        return None

    data = resp.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def api_openai_generate(
    prompt: str,
    model: str = OPENAI_MODEL,
    host: str = OPENAI_API,
    stream: bool = False,
    timeout: float = 300.0,
    **extra_options,
) -> Union[str, dict]:
    """异步调用 OpenAI API 生成内容"""
    if not OPENAI_API:
        raise RuntimeError("请配置 OPENAI_API 环境变量")

    url = f"{host.rstrip('/')}/v1/chat/completions"
    client = await httpxClient.get_openai_client()

    if "messages" not in extra_options:
        messages = [{"role": "user", "content": prompt}]
        if "system" in extra_options:
            messages.insert(0, {"role": "system", "content": extra_options.pop("system")})
    else:
        messages = extra_options.pop("messages")

    payload = {
        "model": model,
        "messages": messages,
        "stream": stream,
        **extra_options,
    }
    logger.debug(url)
    logger.debug(str(payload)[:200])

    resp = await client.post(url, json=payload, timeout=timeout)
    if resp.status_code != 200:
        raise RuntimeError(f"OpenAI generate 请求失败: HTTP {resp.status_code} - {resp.text}")

    if not stream:
        obj = resp.json()
        text = obj.get("choices", [{}])[0].get("message", {}).get("content", "")
        logger.debug(text[:300])
        return text.strip()

    # 流式响应处理
    text_parts = []
    last_obj = None
    start_ts = time.time()
    async for line in resp.aiter_lines():
        if time.time() - start_ts > timeout:
            raise TimeoutError("OpenAI 流式生成超时")
        if not line:
            continue
        if line.startswith("data: "):
            data = line[6:]
            if data == "[DONE]":
                break
            try:
                obj = json.loads(data)
            except json.JSONDecodeError:
                continue
            if "choices" in obj:
                choice = obj["choices"][0]
                if "delta" in choice and "content" in choice["delta"]:
                    text_parts.append(choice["delta"]["content"])
            last_obj = obj

    return {"text": "".join(text_parts), "raw": last_obj or {}}


async def auto_category(content: str, category_dirs: list[str]) -> str:
    """自动为项目分类"""
    prompt = CATEGORY_PROMPT.replace("content", content).replace("category_dirs", ",".join(category_dirs))

    response = await api_openai_generate(prompt)
    logger.info(response)
    return response


# 导出共享的函数
__all__ = ["api_github_readme", "api_openai_generate", "auto_category", "extract_github_info"]
