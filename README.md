# OpenClaw Useful Cron Jobs

Useful cron jobs for OpenClaw AI assistant.

## 🚀 Quick Start

```bash
cd /home/openclaw-useful-cron-jobs
bash setup.sh
```

## 📁 Projects

| Project | Description | Location |
|---------|-------------|----------|
| **Gold Price Alert** | Real-time gold price monitoring and push notifications via DingTalk | `/gold-price-alert/` |

### Gold Price Alert

Real-time gold price monitoring and push notifications.

**Features:**
- Real-time gold price scraping from JD Finance
- Selenium + Chrome headless browser
- DingTalk Webhook push (with signature verification)
- Clean message template

**Usage:**
```bash
# Manual trigger
bash /home/openclaw-useful-cron-jobs/gold-price-alert/scripts/push_gold_price.sh

# Add to crontab
crontab -e
*/5 * * * * /home/openclaw-useful-cron-jobs/gold-price-alert/scripts/push_gold_price.sh
```

## 🔧 Configuration

All sensitive configurations are stored in `.env` file at project root.

Or manually edit `/home/openclaw-useful-cron-jobs/.env`:

```bash
# DingTalk Webhook Configuration
DINGTALK_WEBHOOK_URL=https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN
DINGTALK_SIGN_SECRET=SECYOUR_SECRET
```

> 💡 **How to get DingTalk Webhook:**
> 1. DingTalk Group → Group Settings → Smart Group Assistant → Add Robot → Custom
> 2. Security Settings: Select "Signature"
> 3. Copy Webhook URL and Signature Secret

## 📝 Project Structure

```
openclaw-useful-cron-jobs/
├── README.md                    # This file
├── README_CN.md                 # Chinese documentation
├── .env                         # Sensitive configs (not committed)
├── .env.example                 # Config template
├── .gitignore                   # Git ignore
└── gold-price-alert/            # Gold price monitoring
    ├── README.md
    ├── requirements.txt
    ├── setup.sh
    └── scripts/
        ├── fetch_gold_price.py
        ├── push_to_dingtalk_webhook.py
        └── push_gold_price.sh
```

## 📄 License

MIT License
