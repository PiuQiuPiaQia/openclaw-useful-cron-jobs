# 推送到 GitHub

## 仓库信息

- **远程地址**: https://github.com/PiuQiuPiaQia/openclaw-useful-cron-jobs.git
- **本地路径**: /home/openclaw-useful-cron-jobs
- **分支**: main

## 推送步骤

### 方式一：使用 GitHub Token（推荐）

1. **创建 GitHub Token**
   - 访问：https://github.com/settings/tokens
   - 点击 "Generate new token" → "Generate new token (classic)"
   - 勾选权限：
     - ✅ repo（完整仓库访问权限）
   - 点击 "Generate token"
   - 复制生成的 token（只显示一次）

2. **推送到 GitHub**

   ```bash
   cd /home/openclaw-useful-cron-jobs

   # 推送时会提示输入用户名和密码
   # 用户名：输入你的 GitHub 用户名
   # 密码：粘贴刚才生成的 Token（不是 GitHub 密码）
   git push -u origin main
   ```

### 方式二：使用 GitHub CLI

如果你已安装 `gh` CLI 并登录：

```bash
cd /home/openclaw-useful-cron-jobs
gh auth login
git push -u origin main
```

### 方式三：配置 SSH 密钥

```bash
# 生成 SSH 密钥
ssh-keygen -t ed25519 -C "your_email@example.com"

# 查看公钥
cat ~/.ssh/id_ed25519.pub

# 将公钥添加到 GitHub：
# 1. 访问 https://github.com/settings/keys
# 2. 点击 "New SSH key"
# 3. 粘贴公钥内容
# 4. 点击 "Add SSH key"

# 切换回 SSH URL
git remote set-url origin git@github.com:PiuQiuPiaQia/openclaw-useful-cron-jobs.git

# 推送
git push -u origin main
```

## 验证推送成功

推送成功后，访问：
https://github.com/PiuQiuPiaQia/openclaw-useful-cron-jobs

## 后续推送

配置好认证后，以后推送只需要：

```bash
git add .
git commit -m "your message"
git push
```

## 当前状态

✅ Git 仓库已初始化
✅ 远程仓库已添加
✅ 代码已提交（2 个提交）
⏳ 等待推送到 GitHub

## 提交内容

- **初始提交**: 项目完整代码和文档
- **第二次提交**: GitHub 设置指南

共 17 个文件，1581+ 行代码。
