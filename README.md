# SCX-Tools

一款轻量级渗透测试辅助工具，支持存活探测、域名收集、端口扫描、指纹识别（需配合 FOFA）等功能。

> ⚠️ **首次运行前请务必安装依赖！**  
> 执行以下命令安装所需库：
> ```bash
> pip install requests mmh3
> ```

---

## 🔧 功能列表

- ✅ **存活扫描**：快速探测目标 IP/域名是否在线
- ✅ **域名收集**：从公开数据源聚合子域名
- ✅ **端口扫描**：TCP 快速端口探测
- ✅ **指纹识别**：基于 favicon.ico 的哈希匹配（需配合 FOFA 使用）

---

## 🖥️ 运行方式

> 💡 请将 `你的项目路径` 替换为你本地的实际路径（如 `D:\Tools\SCX-Tools` 或 `C:\Users\Name\Desktop\SCX-Tools`）

### 方法一：进入目录后运行（最推荐）
```bash
python 你的项目路径\SCX-Tools.py
```

## 🚀 快速开始
1. 克隆本仓库：
 ```bash
 git clone https://github.com/yourname/SCX-Tools.git
 cd SCX-Tools
