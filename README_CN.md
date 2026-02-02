# OpenClaw 实用定时任务

OpenClaw AI 助手的实用定时任务集合。

## 🚀 快速开始

### 1. 安装与配置（交互式）

```bash
cd /home/openclaw-useful-cron-jobs
bash setup.sh
```

交互式安装向导会引导你完成：
1. **选择项目** - 选择要安装的项目
2. **配置钉钉** - 设置 Webhook URL 和密钥
3. **安装依赖** - 自动安装所需依赖
4. **测试推送** - 发送测试消息到钉钉

### 2. 测试推送

```bash
bash /home/openclaw-useful-cron-jobs/gold-price-alert/scripts/push_gold_price.sh
```

### 3. 设置定时任务

```bash
crontab -e
```

添加：
```bash
*/5 * * * * /home/openclaw-useful-cron-jobs/gold-price-alert/scripts/push_gold_price.sh
```

## 📁 项目列表

### 黄金价格提醒 (Gold Price Alert)

实时黄金价格监控和推送通知。

**功能特性：**
- 从京东金融实时抓取黄金价格
- 使用 Selenium + Chrome 无头浏览器
- 钉钉 Webhook 推送（加签验证）
- 简洁的消息模板

**位置：** `/gold-price-alert/`

**使用方法：**
```bash
# 手动触发
bash scripts/push_gold_price.sh

# 添加到 crontab
crontab -e
*/5 * * * * /home/openclaw-useful-cron-jobs/gold-price-alert/scripts/push_gold_price.sh
```

### 公共工具库 (Library)

所有定时任务共享的工具库。

**位置：** `/lib/`

**功能特性：**
- 钉钉 Webhook 推送（加签验证）
- 自动从 `.env` 加载配置
- 支持文本和 Markdown 格式

**快速使用：**
```python
from lib.dingtalk import send

send("你好，钉钉！")
```

详细文档：[lib/README.md](lib/README.md)

实时黄金价格监控和推送通知。

**功能特性：**
- 从京东金融实时抓取黄金价格
- 使用 Selenium + Chrome 无头浏览器
- 钉钉 Webhook 推送（加签验证）
- 简洁的消息模板

**位置：** `/gold-price-alert/`

**快速开始：**
```bash
cd /home/openclaw-useful-cron-jobs/gold-price-alert
bash setup.sh
bash /home/openclaw-useful-cron-jobs/configure.sh
```

## 🔧 配置说明

所有敏感配置都存储在项目根目录的 `.env` 文件中。

### 快速配置

```bash
bash /home/openclaw-useful-cron-jobs/configure.sh
```

或手动编辑 `/home/openclaw-useful-cron-jobs/.env`：

```bash
# 钉钉 Webhook 配置
DINGTALK_WEBHOOK_URL=https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN
DINGTALK_SIGN_SECRET=SECYOUR_SECRET
```

> 💡 **获取钉钉 Webhook：**
> 1. 钉钉群 → 群设置 → 智能群助手 → 添加机器人 → 自定义
> 2. 安全设置：选择"加签"
> 3. 复制 Webhook URL 和加签密钥

## 📚 文档

- [gold-price-alert/README.md](gold-price-alert/README.md) - 黄金价格提醒文档

## 🔒 安全说明

- ✅ 敏感信息存储在 `.env` 中（不在代码中）
- ✅ `.env` 已在 `.gitignore` 中
- ✅ 不要分享 `.env` 文件

## 📝 项目结构

```
openclaw-useful-cron-jobs/
├── README.md                    # 英文文档
├── README_CN.md                 # 本文件（中文）
├── configure.sh                 # 配置向导
├── .env                         # 敏感配置（不提交）
├── .env.example                 # 配置模板
├── .gitignore                   # Git 忽略
├── lib/                         # 公共工具库
│   ├── README.md                # 工具库文档
│   ├── __init__.py
│   └── dingtalk.py              # 钉钉推送工具
└── gold-price-alert/            # 黄金价格监控
    ├── README.md
    ├── requirements.txt
    ├── setup.sh
    └── scripts/
        ├── fetch_gold_price.py
        ├── push_to_dingtalk_webhook.py
        └── push_gold_price.sh
```

## 🚀 添加新任务

添加新的定时任务：

1. 为你的任务创建新目录
2. 添加脚本和文档
3. 更新本 README
4. 如需配置，添加到 `.env`

## 📄 许可证

MIT License

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。
