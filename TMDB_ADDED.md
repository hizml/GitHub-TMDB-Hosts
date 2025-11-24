# TMDB/IMDb 域名已添加

## 📝 更新说明

本 fork 版本在原 GitHub520 基础上添加了以下域名支持：

### TMDB (The Movie Database)
- tmdb.org
- api.tmdb.org
- files.tmdb.org
- themoviedb.org
- api.themoviedb.org
- www.themoviedb.org
- auth.themoviedb.org
- image.tmdb.org
- images.tmdb.org

### IMDb (Internet Movie Database)
- imdb.com
- www.imdb.com
- secure.imdb.com
- s.media-imdb.com
- us.dd.imdb.com
- www.imdb.to
- origin-www.imdb.com
- ia.media-imdb.com
- imdb-video.media-imdb.com
- f.media-amazon.com

### TheTVDB
- thetvdb.com
- api.thetvdb.com

## 🎯 适用场景

添加这些域名后，本项目不仅可以解决 GitHub 访问问题，还可以：

1. **影视刮削工具**
   - TinyMediaManager (TMM)
   - Plex Server
   - Emby Server
   - Jellyfin
   - Kodi

2. **NAS 应用**
   - 群晖 Video Station
   - 威联通 Video Station

3. **播放器**
   - Infuse
   - nPlayer

## 📊 域名统计

- **原 GitHub520**: 38 个域名
- **新增 TMDB/IMDb**: 21 个域名
- **总计**: 59 个域名

## 🚀 使用方法

### 快速使用
运行脚本自动获取最佳 IP：

```bash
# 完整模式（本地运行，全面测试）
python fetch_ips.py

# 快速模式（GitHub Actions 运行）
python update_ips.py
```

### 手动使用
1. 查看生成的 `hosts` 文件
2. 复制内容到系统 hosts 文件
3. 刷新 DNS 缓存

## 🔄 自动更新

GitHub Actions 会每 2 小时自动运行一次，更新所有域名的最佳 IP。

## 📌 与原项目的区别

| 项目 | GitHub520 原版 | 本 Fork 版本 |
|------|---------------|-------------|
| **GitHub 域名** | ✅ 支持 | ✅ 支持 |
| **TMDB 域名** | ❌ 不支持 | ✅ 支持 |
| **IMDb 域名** | ❌ 不支持 | ✅ 支持 |
| **TheTVDB 域名** | ❌ 不支持 | ✅ 支持 |
| **域名数量** | 38 个 | 59 个 |

## 🙏 致谢

- 感谢 [@521xueweihan](https://github.com/521xueweihan) 创建的优秀项目 [GitHub520](https://github.com/521xueweihan/GitHub520)
- 本项目是在其基础上的扩展版本

## 📖 相关链接

- **原项目**: https://github.com/521xueweihan/GitHub520
- **本 Fork**: https://github.com/hizml/GitHub520

---

*最后更新: 2025-11-24*
