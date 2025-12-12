# CODEBUDDY.md

This file provides guidance to CodeBuddy Code when working with code in this repository.

## 项目概述

GitHub-TMDB-Hosts 是基于 GitHub520 的扩展版本，在原有 GitHub 域名基础上添加了 TMDB、IMDb、TheTVDB 等影视数据库域名支持。项目通过修改 hosts 文件来解决访问慢和图片加载问题。

## 核心架构

### 1. 三层模块设计

项目采用清晰的职责分离架构:

- **`common.py`**: 公共基础模块
  - 定义了需要解析的 GitHub 域名列表 (`GITHUB_URLS`)
  - 提供文件写入功能 (README.md、hosts、hosts.json)
  - 实现 hosts 模板渲染和内容去重检测

- **`fetch_ips.py`**: IP 获取和优选模块 (本地手动运行)
  - 使用 Cloudflare DoH (DNS over HTTPS) 查询域名 IP
  - 失败时回退到系统 DNS
  - 使用 ping 测试选择最优 IP (取 3 次中位数)
  - 异步执行提升性能 (asyncio)

- **`update_ips.py`**: GitHub Actions 自动更新模块
  - 从远程 API (raw.githubusercontent.com/hizml/GitHub-TMDB-Hosts/main/hosts.json) 获取已验证的 IP 列表
  - 简化流程,仅负责格式化和写入

### 2. 数据流转

```
本地手动流程:
fetch_ips.py → Cloudflare DoH 查询 → Ping 测试优选 → common.py 写入文件

GitHub Actions流程:
update_ips.py → 远程 API 获取 → common.py 写入文件 → Git 提交
```

## 常用命令

### 安装依赖

本地完整开发 (需要 ping 测试和 DoH 查询):
```bash
pip install -r requirements.txt
```

GitHub Actions 环境 (仅需远程 API):
```bash
pip install -r actions_requirements.txt
```

### 手动获取最新 IP

完整流程，包括 DoH 查询和 ping 测试:
```bash
python fetch_ips.py
```

**推荐**: 使用 `sudo` 运行以启用 ping 测试:
```bash
sudo python3 fetch_ips.py
```

**注意**: 非 sudo 模式下，ping 将使用默认优先级 (999)，无法真正测试延迟

### 从远程 API 更新

使用已验证的 IP 列表快速更新:
```bash
python update_ips.py
```

## 重要实现细节

### IP 选择策略

1. **主要来源 - Cloudflare DoH**: 
   - 使用 DNS over HTTPS (https://cloudflare-dns.com/dns-query)
   - 查询域名的 A 记录获取 IP 列表
   - HTTPS 协议，更容易穿透防火墙
   - 高可用性，单一来源通常返回多个 IP（如 CDN 域名返回 4+ 个 IP）
   
2. **备用来源 - 系统 DNS**:
   - DoH 失败时回退到系统默认 DNS
   - 使用 `socket.gethostbyname()` 查询
   
3. **去重和过滤**:
   - 过滤掉无效 IP (DISCARD_LIST: 1.0.1.1, 1.2.1.1, 127.0.0.1)
   - 自动去重确保 IP 唯一性

4. **Ping 优选**:
   - 对每个 IP 执行 3 次 ping
   - 取中位数避免极端值
   - 带缓存避免重复测试 (PING_LIST)
   - 超时设置: 1 秒
   - **需要 sudo 权限**才能真正执行 ping 测试

### 文件更新机制

`common.py:write_file()` 实现智能去重:
- 对比旧 README.md 中的 hosts 内容
- 仅在内容变化时才更新文件和 JSON
- 避免无意义的 Git 提交

### 时区处理

所有时间戳使用 UTC+8 (中国标准时间):
```python
timezone(timedelta(hours=8))
```

## GitHub Actions 工作流

`.github/workflows/GitHub520.yml`:
- 触发条件: 每 2 小时自动运行 (`cron: '0 */2 * * *'`)
- Python 版本: 3.9
- 运行脚本: `update_ips.py` (轻量级远程 API 方案)
- 自动提交: 使用 action_bot 账户提交更新

## 输出文件

- `hosts`: 纯 hosts 格式,供用户直接使用
- `hosts.json`: JSON 格式的 IP-域名映射,供 API 调用
- `README.md`: 从 `README_template.md` 生成,嵌入最新 hosts 内容和时间戳

## 代码约定

- 所有 Python 文件使用 UTF-8 编码
- 重试机制: `common.py:get_json()` 手动实现 3 次重试逻辑
- 异步 IO: 使用 asyncio 实现并发执行
- 类型提示: 使用 typing 模块标注返回类型
- 依赖最小化: 仅依赖 requests-html、pythonping、lxml_html_clean
