from typing import Union
import json
import re
import time
import base64
import asyncio
from functools import lru_cache

import requests
from tenacity import retry, stop_after_attempt, wait_fixed

from .config import logger, GITHUB_TOKEN, OPENAI_API, OPENAI_API_KEY, OPENAI_MODEL
from .prompts import CATEGORY_PROMPT


# 复用 session 提高性能
@lru_cache(maxsize=1)
def get_github_session():
    """创建 GitHub API session"""
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    })
    return session


@lru_cache(maxsize=1)
def get_openai_session():
    """创建 OpenAI API session"""
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    })
    return session


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def api_github_readme(owner, repo):
    """获取 GitHub 仓库的 README"""
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    session = get_github_session()

    resp = session.get(url)
    if resp.status_code != 200:
        print("❌ 无法获取 README:", resp.text)
        return None

    data = resp.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def api_openai_generate(
    prompt: str,
    model: str = OPENAI_MODEL,
    host: str = OPENAI_API,
    stream: bool = False,
    timeout: float = 300.0,
    **extra_options,
) -> Union[str, dict]:
    """
    调用 OpenAI Chat Completions API

    参数:
      model: 模型名，如 "gpt-4o-mini"
      prompt: 提示词
      host: OpenAI API 地址
      stream: 是否流式返回
      timeout: 请求超时（秒）
      **extra_options: 其他可选项，例如：
         temperature=0.7,
         max_tokens=1000,
         system="你是...",
         messages=[{"role": "user", "content": "..."}],

    返回:
      非流式: {"text": 模型输出文本, "raw": 完整 JSON 对象}
      流式: {"text": 累积的输出文本, "raw": 最后一条 JSON 对象}
    """
    if not OPENAI_API:
        raise RuntimeError("请配置 OPENAI_API 环境变量")

    url = f"{host.rstrip('/')}/v1/chat/completions"
    session = get_openai_session()

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

    resp = session.post(url, json=payload, timeout=timeout)
    if resp.status_code != 200:
        raise RuntimeError(f"OpenAI generate 请求失败: HTTP {resp.status_code} - {resp.text}")

    if not stream:
        obj = resp.json()
        text = obj.get("choices", [{}])[0].get("message", {}).get("content", "")
        logger.debug(text[:300])
        return text.strip()

    text_parts = []
    last_obj = None
    start_ts = time.time()
    for line in resp.iter_lines():
        if time.time() - start_ts > timeout:
            raise TimeoutError("OpenAI 流式生成超时")
        if not line:
            continue
        if line.startswith(b"data: "):
            data = line[6:]
            if data == b"[DONE]":
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


async def auto_category(content, category_dirs):
    """异步分类 - 在线程池中运行同步的 API 调用"""
    content = f"""我收集了GitHub上的项目,以下是对项目的描述: {content}.
    现在我想对其进行分类，已有的分类有 {category_dirs} ，分析该项目应在哪个分类下，如不存在已有的分类，返回 github。 直接返回分类名称， 不需要其他的废话."""
    prompt = CATEGORY_PROMPT.replace("content", content).replace("category_dirs", ",".join(category_dirs))

    # 在线程池中运行同步的 API 调用
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, api_openai_generate, prompt)
    logger.info(response)
    return response


if __name__ == "__main__":
    pass
