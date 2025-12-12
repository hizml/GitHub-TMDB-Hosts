#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   2020-05-19 15:27
#   Desc    :   获取最新的 GitHub 相关域名对应 IP
import os
from typing import Any, Dict, List, Optional
from datetime import datetime
import sys
import asyncio

from pythonping import ping
from requests_html import HTMLSession

from common import GITHUB_URLS, write_hosts_content


PING_TIMEOUT_SEC: int = 1
DISCARD_LIST: List[str] = ["1.0.1.1", "1.2.1.1", "127.0.0.1"]


PING_LIST: Dict[str, int] = dict()


def ping_cached(ip: str) -> int:
    global PING_LIST
    if ip in PING_LIST:
        return PING_LIST[ip]
    
    try:
        ping_times = [ping(ip, timeout=PING_TIMEOUT_SEC).rtt_avg_ms for _ in range(3)]
        ping_times.sort()
        print(f'Ping {ip}: {ping_times} ms')
        PING_LIST[ip] = ping_times[1] # 取中位数
        return PING_LIST[ip]
    except PermissionError:
        # macOS/Linux 需要 sudo 权限执行 ping
        print(f'⚠️  Ping {ip}: 权限不足，使用默认优先级')
        print(f'提示: 使用 "sudo python3 fetch_ips.py" 来启用 ping 测试')
        # 返回一个默认值，表示未测试
        PING_LIST[ip] = 999
        return PING_LIST[ip]
    except Exception as e:
        print(f'❌ Ping {ip}: 失败 - {e}')
        PING_LIST[ip] = 999
        return PING_LIST[ip]


def select_ip_from_list(ip_list: List[str]) -> Optional[str]:
    if len(ip_list) == 0:
        return None
    ping_results = [(ip, ping_cached(ip)) for ip in ip_list]
    ping_results.sort(key=lambda x: x[1])
    best_ip = ping_results[0][0]
    print(f"{ping_results}, selected {best_ip}")
    return best_ip


# Web 查询已被 ipaddress.com 封禁 (HTTP 403)，已移除相关代码


# 添加备用 DNS 查询方法 - 使用 DNS over HTTPS
def get_ip_from_doh(domain: str) -> Optional[List[str]]:
    """使用 Cloudflare DoH 查询域名 IP"""
    try:
        import requests
        url = f"https://cloudflare-dns.com/dns-query?name={domain}&type=A"
        headers = {"Accept": "application/dns-json"}
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if "Answer" in data:
                ips = [answer["data"] for answer in data["Answer"] if answer["type"] == 1]
                if ips:
                    return ips
            # 没有 Answer 字段或 A 记录为空
            print(f"{domain}: DoH 响应无有效 A 记录")
        else:
            print(f"{domain}: DoH 查询 HTTP {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"{domain}: DoH 查询超时")
    except requests.exceptions.RequestException as e:
        print(f"{domain}: DoH 网络请求失败 - {type(e).__name__}")
    except Exception as e:
        print(f"{domain}: DoH 查询异常 - {type(e).__name__}: {e}")
    return []


# DNS 查询在某些环境中存在兼容性问题，已移除


async def get_ip(session: Any, github_url: str) -> Optional[str]:
    """
    获取域名的最优 IP 地址
    使用 Cloudflare DoH 查询，失败时回退到系统 DNS
    """
    # DoH 查询 - 最可靠的方式
    ip_list_doh = []
    try:
        ip_list_doh = get_ip_from_doh(github_url) or []
        if ip_list_doh:
            print(f"{github_url}: DoH 查询成功 {ip_list_doh}")
    except Exception as ex:
        print(f"{github_url}: DoH 查询失败 - {ex}")

    # 过滤无效 IP
    ip_list_set = set(ip_list_doh)
    for discard_ip in DISCARD_LIST:
        ip_list_set.discard(discard_ip)
    ip_list = list(ip_list_set)
    ip_list.sort()

    # 如果 DoH 失败，尝试系统 DNS
    if len(ip_list) == 0:
        print(f"{github_url}: DoH 失败，尝试系统 DNS")
        try:
            import socket
            system_ip = socket.gethostbyname(github_url)
            if system_ip and system_ip not in DISCARD_LIST:
                ip_list = [system_ip]
                print(f"{github_url}: 系统 DNS 查询成功 {system_ip}")
        except Exception as e:
            print(f"{github_url}: 系统 DNS 也失败 - {e}")
            return None

    if len(ip_list) == 0:
        return None

    print(f"{github_url}: 最终 IP 列表 {ip_list}")
    best_ip = select_ip_from_list(ip_list)
    return best_ip


async def main() -> None:
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{current_time} - Start script.')

    # 从环境变量读取 force_update 参数
    force_update = os.getenv('FORCE_UPDATE', 'false').lower() == 'true'
    if force_update:
        print('Force update mode enabled - will update even if content unchanged')

    session = HTMLSession()
    content = ""
    content_list = []
    for index, github_url in enumerate(GITHUB_URLS):
        print(f'Start Processing url: {index + 1}/{len(GITHUB_URLS)}, {github_url}')
        try:
            ip = await get_ip(session, github_url)
            if ip is None:
                print(f"{github_url}: IP Not Found")
                ip = "# IP Address Not Found"
            content += ip.ljust(30) + github_url
            global PING_LIST
            if PING_LIST.get(ip) is not None and PING_LIST.get(ip) == PING_TIMEOUT_SEC * 1000:
                content += "  # Timeout"
            content += "\n"
            content_list.append((ip, github_url,))
        except Exception:
            continue

    write_hosts_content(content, content_list, force_update=force_update)
    # print(hosts_content)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{current_time} - End script.')


if __name__ == "__main__":
    if sys.platform == "win32":
        # Windows 事件循环策略配置
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
