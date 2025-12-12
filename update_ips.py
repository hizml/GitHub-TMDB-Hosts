#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   2025-01-16 15:27
#   Desc    :   GitHub Action 运行的脚本
import os

from requests_html import HTMLSession

from common import get_json, write_hosts_content


def main() -> None:
    """主函数：从远程 API 获取 IP 数据并更新文件"""
    print('Start script.')
    # 检查是否强制更新
    force_update = os.getenv('FORCE_UPDATE', 'false').lower() == 'true'
    if force_update:
        print('Force update mode enabled - will update even if content unchanged')
    
    session = HTMLSession()
    content = ""
    content_list = get_json(session)
    
    if not content_list:
        print('❌ Failed to fetch data from remote API')
        return
    
    for item in content_list:
        content += item[0].ljust(30) + item[1] + "\n"
    
    hosts_content = write_hosts_content(content, content_list, force_update=force_update)
    print(hosts_content)
    print('End script.')


if __name__ == '__main__':
    main()
