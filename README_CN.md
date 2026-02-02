# OpenClaw 实用定时任务

OpenClaw AI 助手的实用定时任务。

## 🚀 快速开始

```bash
cd /home/openclaw-useful-cron-jobs
bash setup.sh
```

## 📁 项目列表

| 项目 | 描述 | 位置 |
|------|------|------|
| **黄金价格提醒** | 实时黄金价格监控和钉钉推送通知 | `/gold-price-alert/` |

### 黄金价格提醒 (Gold Price Alert)

实时黄金价格监控和推送通知。

**功能特性：**
- 从京东金融实时抓取黄金价格
- 使用 Selenium + Chrome 无头浏览器
- 钉钉 Webhook 推送（加签验证）
- 简洁的消息模板

**使用方法：**
```bash
# 手动触发
bash /home/openclaw-useful-cron-jobs/gold-price-alert/scripts/push_gold_price.sh

# 添加到 crontab
crontab -e
*/5 * * * * /home/openclaw-useful-cron-jobs/gold-price-alert/scripts/push_gold_price.sh
```

## 🔧 配置说明

所有敏感配置都存储在项目根目录的 `.env` 文件中。

手动编辑 `/home/openclaw-useful-cron-jobs/.env`：

```bash
# 钉钉 Webhook 配置
DINGTALK_WEBHOOK_URL=https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN
DINGTALK_SIGN_SECRET=SECYOUR_SECRET
```

> 💡 **获取钉钉 Webhook：**
> 1. 钉钉群 → 群设置 → 智能群助手 → 添加机器人 → 自定义
> 2. 安全设置：选择"加签"
> 3. 复制 Webhook URL 和加签密钥

## 📝 项目结构

```
openclaw-useful-cron-jobs/
├── README.md                    # 英文文档
├── README_CN.md                 # 本文件（中文）
├── .env                         # 敏感配置（不提交）
├── .env.example                 # 配置模板
├── .gitignore                   # Git 忽略
└── gold-price-alert/            # 黄金价格监控
    ├── README.md
    ├── requirements.txt
    ├── setup.sh
    └── scripts/
        ├── fetch_gold_price.py
        ├── push_to_dingtalk_webhook.py
        └── push_gold_price.sh
```

## 📄 许可证

MIT License
