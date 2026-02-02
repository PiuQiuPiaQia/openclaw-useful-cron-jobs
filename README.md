# OpenClaw Useful Cron Jobs

A collection of useful cron jobs for OpenClaw AI assistant.

## 🚀 Quick Start

```bash
cd /home/openclaw-useful-cron-jobs
bash setup.sh
```

## 📁 Projects

| Project | Description | Location |
|---------|-------------|----------|
| **Gold Price Alert** | Real-time gold price monitoring and push notifications via DingTalk | `/gold-price-alert/` |
| **Library** | Shared utilities for DingTalk webhook and configuration management | `/lib/` |

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

### Library

Shared utilities for all cron jobs.

**Features:**
- DingTalk webhook push (with signature verification)
- Auto-load config from `.env`
- Support text and Markdown format

**Quick Start:**
```python
from lib.dingtalk import send

send("Hello, DingTalk!")
```

See [lib/README.md](lib/README.md) for details.

## 🔧 Configuration

All sensitive configurations are stored in `.env` file at project root.

### Quick Configure

```bash
bash /home/openclaw-useful-cron-jobs/configure.sh
```

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

## 📚 Documentation

- [gold-price-alert/README.md](gold-price-alert/README.md) - Gold price alert documentation

## 🔒 Security

- ✅ Sensitive info stored in `.env` (not in code)
- ✅ `.env` is in `.gitignore`
- ✅ Never share your `.env` file

## 📝 Project Structure

```
openclaw-useful-cron-jobs/
├── README.md                    # This file
├── README_CN.md                 # Chinese documentation
├── configure.sh                 # Configuration wizard
├── .env                         # Sensitive configs (not committed)
├── .env.example                 # Config template
├── .gitignore                   # Git ignore
├── lib/                         # Shared library
│   ├── README.md                # Library documentation
│   ├── __init__.py
│   └── dingtalk.py              # DingTalk webhook tool
└── gold-price-alert/            # Gold price monitoring
    ├── README.md
    ├── requirements.txt
    ├── setup.sh
    └── scripts/
        ├── fetch_gold_price.py
        ├── push_to_dingtalk_webhook.py
        └── push_gold_price.sh
```

## 🚀 Adding New Jobs

To add a new cron job:

1. Create a new directory for your job
2. Add your scripts and documentation
3. Update this README
4. Add configuration to `.env` if needed

## 📄 License

MIT License

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
