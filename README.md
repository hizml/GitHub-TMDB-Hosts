# GitHub-TMDB-Hosts

<p align="center">
😘 解决 GitHub 访问慢、图片加载失败问题<br>
🎬 解决 TMDB、IMDb、TheTVDB 等影视数据库访问问题
</p>

> 本项目基于 [GitHub520](https://github.com/521xueweihan/GitHub520)，添加了 TMDB/IMDb 相关域名支持

## 📝 介绍

**本项目无需安装任何程序，仅需 5 分钟。**

通过修改本地 hosts 文件，解决：

### GitHub 相关
- ✅ GitHub 访问速度慢
- ✅ GitHub 图片加载失败

### 影视刮削相关  
- ✅ TMDB (The Movie Database) 访问问题
- ✅ IMDb (Internet Movie Database) 访问问题
- ✅ TheTVDB 访问问题

**适用工具**: TinyMediaManager、Plex、Emby、Jellyfin、Kodi、群晖 Video Station、Infuse、nPlayer 等

## 🚀 使用方法
下面的地址无需访问 GitHub 即可获取到最新的 hosts 内容：

- 文件：`https://raw.githubusercontent.com/hizml/GitHub-TMDB-Hosts/main/hosts`
- JSON：`https://raw.githubusercontent.com/hizml/GitHub-TMDB-Hosts/main/hosts.json`

### 方式一：手动复制（最简单）

#### 1. 复制下面的内容

```bash
# GitHub-TMDB-Hosts Start
# IP Address Not Found        alive.github.com
# IP Address Not Found        api.github.com
# IP Address Not Found        api.individual.githubcopilot.com
# IP Address Not Found        avatars.githubusercontent.com
# IP Address Not Found        avatars0.githubusercontent.com
# IP Address Not Found        avatars1.githubusercontent.com
# IP Address Not Found        avatars2.githubusercontent.com
# IP Address Not Found        avatars3.githubusercontent.com
# IP Address Not Found        avatars4.githubusercontent.com
# IP Address Not Found        avatars5.githubusercontent.com
# IP Address Not Found        camo.githubusercontent.com
# IP Address Not Found        central.github.com
# IP Address Not Found        cloud.githubusercontent.com
# IP Address Not Found        codeload.github.com
# IP Address Not Found        collector.github.com
# IP Address Not Found        desktop.githubusercontent.com
# IP Address Not Found        favicons.githubusercontent.com
# IP Address Not Found        gist.github.com
# IP Address Not Found        github-cloud.s3.amazonaws.com
# IP Address Not Found        github-com.s3.amazonaws.com
# IP Address Not Found        github-production-release-asset-2e65be.s3.amazonaws.com
# IP Address Not Found        github-production-repository-file-5c1aeb.s3.amazonaws.com
# IP Address Not Found        github-production-user-asset-6210df.s3.amazonaws.com
# IP Address Not Found        github.blog
# IP Address Not Found        github.com
# IP Address Not Found        github.community
# IP Address Not Found        github.githubassets.com
# IP Address Not Found        github.global.ssl.fastly.net
# IP Address Not Found        github.io
# IP Address Not Found        github.map.fastly.net
# IP Address Not Found        githubstatus.com
# IP Address Not Found        live.github.com
# IP Address Not Found        media.githubusercontent.com
# IP Address Not Found        objects.githubusercontent.com
# IP Address Not Found        pipelines.actions.githubusercontent.com
# IP Address Not Found        raw.githubusercontent.com
# IP Address Not Found        user-images.githubusercontent.com
# IP Address Not Found        vscode.dev
# IP Address Not Found        education.github.com
# IP Address Not Found        private-user-images.githubusercontent.com
# IP Address Not Found        tmdb.org
# IP Address Not Found        api.tmdb.org
# IP Address Not Found        files.tmdb.org
# IP Address Not Found        themoviedb.org
# IP Address Not Found        api.themoviedb.org
# IP Address Not Found        www.themoviedb.org
# IP Address Not Found        auth.themoviedb.org
# IP Address Not Found        image.tmdb.org
# IP Address Not Found        images.tmdb.org
# IP Address Not Found        imdb.com
# IP Address Not Found        www.imdb.com
# IP Address Not Found        secure.imdb.com
# IP Address Not Found        s.media-imdb.com
# IP Address Not Found        us.dd.imdb.com
# IP Address Not Found        www.imdb.to
# IP Address Not Found        origin-www.imdb.com
# IP Address Not Found        ia.media-imdb.com
# IP Address Not Found        imdb-video.media-imdb.com
# IP Address Not Found        f.media-amazon.com
# IP Address Not Found        thetvdb.com
# IP Address Not Found        api.thetvdb.com


# Update time: 2025-12-12T17:52:18+08:00
# Update url: https://raw.githubusercontent.com/hizml/GitHub-TMDB-Hosts/main/hosts
# Star me: https://github.com/hizml/GitHub-TMDB-Hosts
# Star original: https://github.com/521xueweihan/GitHub520
# GitHub-TMDB-Hosts End

```

该内容会自动定时更新，数据更新时间：2025-12-12T17:52:18+08:00

#### 2. 修改 hosts 文件

hosts 文件在每个系统的位置：

- Windows: `C:\Windows\System32\drivers\etc\hosts`
- Linux: `/etc/hosts`
- macOS: `/etc/hosts`
- Android: `/system/etc/hosts`
- iOS: `/etc/hosts`

修改方法：

1. Windows 使用记事本（需要管理员权限）
2. Linux/Mac 使用 Root 权限：`sudo vi /etc/hosts`
3. 将上面的内容复制到文件末尾

#### 3. 刷新 DNS 缓存

```bash
# Windows
ipconfig /flushdns

# macOS
sudo killall -HUP mDNSResponder

# Linux
sudo systemctl restart systemd-resolved
```

### 方式二：SwitchHosts（推荐，自动更新）

**推荐使用 [SwitchHosts](https://github.com/oldj/SwitchHosts) 工具管理 hosts**

配置如下：

- **类型**: Remote（远程）
- **标题**: GitHub-TMDB-Hosts
- **URL**: `https://raw.githubusercontent.com/hizml/GitHub-TMDB-Hosts/main/hosts`
- **自动刷新**: 1 小时

配置后启用规则即可，每次 hosts 有更新都会自动同步。

### 方式三：命令行（一键更新）

#### macOS/Linux
```bash
curl https://raw.githubusercontent.com/hizml/GitHub-TMDB-Hosts/main/hosts | sudo tee -a /etc/hosts
```

#### Windows (Git Bash)
```bash
curl https://raw.githubusercontent.com/hizml/GitHub-TMDB-Hosts/main/hosts >> /c/Windows/System32/drivers/etc/hosts
```

在**CMD**中执行以下命令，执行前需要替换**git-bash.exe**和**fetch_github_hosts**为你本地的路径，注意前者为windows路径格式后者为shell路径格式

`"C:\Program Files\Git\git-bash.exe" -c "/c/Users/XXX/fetch_github_hosts"`

可以将上述命令添加到windows的task schedular（任务计划程序）中以定时执行

#### GNU（Ubuntu/CentOS/Fedora）

`sudo sh -c 'sed -i "/# GitHub520 Host Start/Q" /etc/hosts && curl https://raw.hellogithub.com/hosts >> /etc/hosts'`

#### BSD/macOS

`sudo sed -i "" "/# GitHub520 Host Start/,/# Github520 Host End/d" /etc/hosts && curl https://raw.hellogithub.com/hosts | sudo tee -a /etc/hosts`

将上面的命令添加到 cron，可定时执行。使用前确保 GitHub520 内容在该文件最后部分。

**在 Docker 中运行，若遇到 `Device or resource busy` 错误，可使用以下命令执行**

`cp /etc/hosts ~/hosts.new && sed -i "/# GitHub520 Host Start/Q" ~/hosts.new && curl https://raw.hellogithub.com/hosts >> ~/hosts.new && cp -f ~/hosts.new /etc/hosts`

### 方式四：AdGuard 用户（自动方式）

在 **过滤器>DNS 封锁清单>添加阻止列表>添加一个自定义列表**，配置如下：

- 名称：随意

- URL：`https://raw.hellogithub.com/hosts`（和上面 SwitchHosts 使用的一样）

如图：

![](./img/AdGuard-rules.png)

更新间隔在 **设置 > 常规设置 > 过滤器更新间隔（设置一小时一次即可）**，记得勾选上 **使用过滤器和 Hosts 文件以拦截指定域名**

![](./img/AdGuard-rules2.png)

**Tip**：不要添加在 **DNS 允许清单** 内，只能添加在 **DNS 封锁清单** 才管用。 另外，AdGuard for Mac、AdGuard for Windows、AdGuard for Android、AdGuard for IOS 等等 **AdGuard 家族软件** 添加方法均类似。


## 三、效果对比
之前的样子：

![](./img/old.png)

修改完 hosts 的样子：

![](./img/new.png)

## 📦 支持的域名

### GitHub 域名 (38 个)
github.com, api.github.com, raw.githubusercontent.com, avatars.githubusercontent.com 等

### TMDB 域名 (9 个)
tmdb.org, api.tmdb.org, themoviedb.org, www.themoviedb.org, image.tmdb.org 等

### IMDb 域名 (10 个)
imdb.com, www.imdb.com, ia.media-imdb.com 等

### TheTVDB 域名 (2 个)
thetvdb.com, api.thetvdb.com

**总计：59 个域名** - 详见 [TMDB_ADDED.md](./TMDB_ADDED.md)

## 🔄 自动更新

本项目配置了 GitHub Actions，每 2 小时自动运行一次：
- 自动测试并选择最快的 IP
- 自动提交更新
- 无需手动操作

## 📖 相关文档

- [快速开始指南](./快速开始.md) - 详细使用说明
- [TMDB 域名说明](./TMDB_ADDED.md) - 添加的域名列表

## 🙏 致谢

感谢 [@521xueweihan](https://github.com/521xueweihan) 创建的优秀项目 [GitHub520](https://github.com/521xueweihan/GitHub520)

## ⚠️ 免责声明

本项目仅供学习和研究使用，请遵守相关法律法规。使用本项目产生的任何后果由使用者自行承担。
