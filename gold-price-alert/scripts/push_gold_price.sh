#!/bin/bash
# 黄金价格监控和推送脚本

# 1. 运行金价获取脚本
python3 /root/.openclaw/workspace/gold-price/scripts/fetch_gold_price.py > /tmp/gold_price_data.json

# 2. 读取金价数据
PRICE=$(python3 -c "import json; print(json.load(open('/tmp/gold_price_data.json'))['price'])")
UNIT=$(python3 -c "import json; print(json.load(open('/tmp/gold_price_data.json'))['unit'])")
SOURCE=$(python3 -c "import json; print(json.load(open('/tmp/gold_price_data.json'))['source'])")
TIMESTAMP=$(python3 -c "import json; print(json.load(open('/tmp/gold_price_data.json'))['timestamp'])")
NOTE=$(python3 -c "import json; print(json.load(open('/tmp/gold_price_data.json')).get('note', ''))")

# 3. 格式化消息
MESSAGE="📈 实时黄金价格播报

━━━━━━━━━━━━━━━
💰 当前金价：${PRICE} ${UNIT}
🕐 更新时间：${TIMESTAMP}"

if [ -n "$NOTE" ]; then
    MESSAGE="${MESSAGE}
📝 ${NOTE}"
fi

MESSAGE="${MESSAGE}
━━━━━━━━━━━━━━━"

# 4. 保存到文件供主会话读取
echo "$MESSAGE" > /tmp/gold_price_latest.txt

# 5. 推送到钉钉 Webhook
python3 /root/.openclaw/workspace/gold-price/scripts/push_to_dingtalk_webhook.py

echo "✅ 金价已更新并推送到钉钉: ${PRICE} ${UNIT}"
