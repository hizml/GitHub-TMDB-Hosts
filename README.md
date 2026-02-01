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
140.82.112.25                 alive.github.com
140.82.114.5                  api.github.com
140.82.112.22                 api.individual.githubcopilot.com
185.199.108.133               avatars.githubusercontent.com
185.199.108.133               avatars0.githubusercontent.com
185.199.108.133               avatars1.githubusercontent.com
185.199.108.133               avatars2.githubusercontent.com
185.199.108.133               avatars3.githubusercontent.com
185.199.108.133               avatars4.githubusercontent.com
185.199.108.133               avatars5.githubusercontent.com
185.199.108.133               camo.githubusercontent.com
140.82.112.22                 central.github.com
185.199.108.133               cloud.githubusercontent.com
140.82.113.10                 codeload.github.com
140.82.112.21                 collector.github.com
185.199.108.133               desktop.githubusercontent.com
185.199.108.133               favicons.githubusercontent.com
140.82.113.3                  gist.github.com
16.15.186.239                 github-cloud.s3.amazonaws.com
16.15.192.41                  github-com.s3.amazonaws.com
16.15.192.225                 github-production-release-asset-2e65be.s3.amazonaws.com
16.15.201.189                 github-production-repository-file-5c1aeb.s3.amazonaws.com
16.15.188.5                   github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.114.4                  github.com
140.82.112.18                 github.community
185.199.108.154               github.githubassets.com
151.101.1.194                 github.global.ssl.fastly.net
185.199.108.153               github.io
185.199.108.133               github.map.fastly.net
185.199.108.153               githubstatus.com
140.82.112.25                 live.github.com
185.199.108.133               media.githubusercontent.com
185.199.108.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.108.133               raw.githubusercontent.com
185.199.108.133               user-images.githubusercontent.com
13.107.213.40                 vscode.dev
140.82.112.22                 education.github.com
185.199.108.133               private-user-images.githubusercontent.com
108.139.29.100                tmdb.org
3.170.19.13                   api.tmdb.org
3.170.42.109                  files.tmdb.org
3.168.73.124                  themoviedb.org
3.170.19.104                  api.themoviedb.org
3.168.73.124                  www.themoviedb.org
3.170.3.114                   auth.themoviedb.org
169.150.236.99                image.tmdb.org
185.93.1.247                  images.tmdb.org
44.215.137.99                 imdb.com
18.67.70.32                   www.imdb.com
98.82.155.134                 secure.imdb.com
18.67.70.32                   s.media-imdb.com
98.82.158.179                 us.dd.imdb.com
18.67.70.32                   www.imdb.to
44.215.137.99                 origin-www.imdb.com
2.18.67.68                    ia.media-imdb.com
18.67.76.111                  imdb-video.media-imdb.com
151.101.1.16                  f.media-amazon.com
3.171.75.86                   thetvdb.com
18.164.130.112                api.thetvdb.com


# Update time: 2026-02-02T02:17:59+08:00
# Update url: https://raw.githubusercontent.com/hizml/GitHub-TMDB-Hosts/main/hosts
# Star me: https://github.com/hizml/GitHub-TMDB-Hosts
# Star original: https://github.com/521xueweihan/GitHub520
# GitHub-TMDB-Hosts End

```

该内容会自动定时更新，数据更新时间：2026-02-02T02:17:59+08:00

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
