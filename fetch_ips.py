#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   2020-05-19 15:27
#   Desc    :   获取最新的 GitHub 相关域名对应 IP
import os
import re
from typing import Any, Dict, List, Optional
from datetime import datetime
import sys
import asyncio
import aiodns

from pythonping import ping
from requests_html import HTMLSession
from retry import retry

from common import GITHUB_URLS, write_hosts_content


PING_TIMEOUT_SEC: int = 1
DISCARD_LIST: List[str] = ["1.0.1.1", "1.2.1.1", "127.0.0.1"]


PING_LIST: Dict[str, int] = dict()


def ping_cached(ip: str) -> int:
    global PING_LIST
    if ip in PING_LIST:
        return PING_LIST[ip]
    ping_times = [ping(ip, timeout=PING_TIMEOUT_SEC).rtt_avg_ms for _ in range(3)]
    ping_times.sort()
    print(f'Ping {ip}: {ping_times} ms')
    PING_LIST[ip] = ping_times[1] # 取中位数
    return PING_LIST[ip]


def select_ip_from_list(ip_list: List[str]) -> Optional[str]:
    if len(ip_list) == 0:
        return None
    ping_results = [(ip, ping_cached(ip)) for ip in ip_list]
    ping_results.sort(key=lambda x: x[1])
    best_ip = ping_results[0][0]
    print(f"{ping_results}, selected {best_ip}")
    return best_ip


@retry(tries=2)
def get_ip_list_from_ipaddress_com(session: Any, github_url: str) -> Optional[List[str]]:
    url = f'https://sites.ipaddress.com/{github_url}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1'
                      '06.0.0.0 Safari/537.36'}
    try:
        rs = session.get(url, headers=headers, timeout=10)
        if rs.status_code != 200:
            print(f"{url} - HTTP {rs.status_code}")
            return []
        pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
        ip_list = re.findall(pattern, rs.html.text)
        # 过滤掉明显错误的 IP
        valid_ips = []
        for ip in ip_list:
            parts = ip.split('.')
            if all(0 <= int(p) <= 255 for p in parts):
                valid_ips.append(ip)
        return valid_ips
    except Exception as ex:
        print(f"get: {url}, error: {type(ex).__name__}: {ex}")
        raise Exception


DNS_SERVER_LIST = [
    "1.1.1.1",  # Cloudflare
    "8.8.8.8",  # Google
    "101.101.101.101",  # Quad101
    "101.102.103.104",  # Quad101
]


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
                return ips
    except Exception as e:
        print(f"{domain}: DoH 查询失败 - {e}")
    return []


def windows_compatibility_check():
    if sys.platform == "win32":
        # 检查 pycares 是否正常加载
        try:
            import pycares
        except ImportError:
            raise RuntimeError("请先执行 'pip install pycares'")


async def get_ip_list_from_dns(
    domain,
    dns_server_list=None,
):
    """使用 aiodns 异步查询域名的 A 记录"""
    if dns_server_list is None:
        dns_server_list = ["1.2.4.8", "114.114.114.114"]

    # Windows 兼容性检查
    windows_compatibility_check()

    try:
        # 配置 DNS 服务器
        resolver = aiodns.DNSResolver(nameservers=dns_server_list)

        # aiodns 3.0+ 的 query 方法: query(self, host, query_type)
        # 注意: query_type 应该是字符串 'A', 'AAAA', 'MX' 等
        result = await resolver.query(domain, 'A')

        # A 记录返回的是 ares_query_a_result 对象列表
        return [answer.host for answer in result]
    except aiodns.error.DNSError as e:
        print(f"{domain}: DNS 查询失败: {e}")
        return []
    except Exception as e:
        print(f"{domain}: DNS 查询异常: {type(e).__name__} - {e}")
        return []


async def get_ip(session: Any, github_url: str) -> Optional[str]:
    # DoH 查询 - 最可靠的方式，优先使用
    ip_list_doh = []
    try:
        ip_list_doh = get_ip_from_doh(github_url) or []
        if ip_list_doh:
            print(f"{github_url}: DoH查询成功 {ip_list_doh}")
    except Exception as ex:
        print(f"{github_url}: DoH查询失败 - {ex}")

    # DNS 查询 - 作为补充
    ip_list_dns = []
    try:
        ip_list_dns = await get_ip_list_from_dns(github_url, dns_server_list=DNS_SERVER_LIST)
        if ip_list_dns:
            print(f"{github_url}: DNS查询成功 {ip_list_dns}")
    except Exception as ex:
        print(f"{github_url}: DNS查询失败 - {ex}")

    # Web 查询 - 优先级最低（已被 403 封禁）
    ip_list_web = []
    # 跳过 Web 查询以提高速度，因为已被 403 封禁
    # try:
    #     ip_list_web = get_ip_list_from_ipaddress_com(session, github_url)
    #     if ip_list_web:
    #         print(f"{github_url}: Web查询成功 {ip_list_web}")
    # except Exception as ex:
    #     print(f"{github_url}: Web查询失败 - {ex}")

    ip_list_set = set(ip_list_doh + ip_list_dns + ip_list_web)
    for discard_ip in DISCARD_LIST:
        ip_list_set.discard(discard_ip)
    ip_list = list(ip_list_set)
    ip_list.sort()

    if len(ip_list) == 0:
        print(f"{github_url}: DoH和DNS均失败,尝试系统 DNS")
        # 尝试使用系统默认 DNS
        try:
            import socket
            system_ip = socket.gethostbyname(github_url)
            if system_ip and system_ip not in DISCARD_LIST:
                ip_list = [system_ip]
                print(f"{github_url}: 系统DNS查询成功 {system_ip}")
        except Exception as e:
            print(f"{github_url}: 系统DNS也失败 - {e}")
            return None

    if len(ip_list) == 0:
        return None

    print(f"{github_url}: 最终IP列表 {ip_list}")
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
