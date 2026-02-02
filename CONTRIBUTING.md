# Contributing to OpenClaw Useful Cron Jobs

感谢你对本项目的关注！

## 如何贡献

### 报告问题

如果你发现了 bug 或有功能建议，请：

1. 检查是否已有相关 issue
2. 创建新的 issue，详细描述问题或建议
3. 提供复现步骤和环境信息

### 提交代码

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

### 添加新的定时任务

要添加新的定时任务：

1. 在项目根目录创建新目录，如 `new-job/`
2. 创建 `setup.sh` 安装脚本
3. 创建 `scripts/` 目录存放脚本
4. 在根目录的 `setup.sh` 中添加项目信息：

```bash
PROJECTS[2]="new-job"
PROJECT_DESCRIPTIONS[2]="新任务描述"
```

5. 更新 README.md 和 README_CN.md

### 代码规范

- Shell 脚本使用 4 空格缩进
- Python 脚本遵循 PEP 8
- 添加适当的注释
- 确保脚本有执行权限

## 开发环境

```bash
# 克隆仓库
git clone https://github.com/yourusername/openclaw-useful-cron-jobs.git
cd openclaw-useful-cron-jobs

# 运行安装
bash setup.sh
```

## 许可证

提交代码即表示你同意将代码以 MIT License 发布。
