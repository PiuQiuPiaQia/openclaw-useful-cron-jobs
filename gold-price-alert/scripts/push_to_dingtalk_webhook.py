#!/usr/bin/env python3
"""
通过钉钉 Webhook 直接推送黄金价格（使用加签验证）
"""

import subprocess
import json
import sys
from datetime import datetime
from pathlib import Path

# 添加项目 lib 目录到 Python 路径
lib_path = Path(__file__).parent.parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

# 导入钉钉推送工具
from dingtalk import send_to_dingtalk

def push_gold_price_to_dingtalk():
    """获取金价并推送到钉钉"""

    # 1. 获取金价
    try:
        # 获取脚本所在目录
        script_dir = Path(__file__).parent
        fetch_script = script_dir / 'fetch_gold_price.py'

        result = subprocess.run(
            ['python3', str(fetch_script)],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            print(f"获取金价失败: {result.stderr}", file=sys.stderr)
            return False
            if result.returncode != 0:
                print(f"模拟数据也失败: {result.stderr}", file=sys.stderr)
                return False

        gold_data = json.loads(result.stdout)

    except Exception as e:
        print(f"获取金价异常: {e}", file=sys.stderr)
        return False

    # 2. 格式化消息
    price = gold_data.get('price', 'N/A')
    unit = gold_data.get('unit', '元/克')
    source = gold_data.get('source', '未知')
    timestamp = gold_data.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # 简化数据来源显示
    if '京东金融' in source:
        source_display = '京东金融'
    else:
        source_display = source

    message = f"""📈 实时黄金价格播报

━━━━━━━━━━━━━━━
💰 当前金价：{price} {unit}
🕐 更新时间：{timestamp}
📍 数据来源：{source_display}
━━━━━━━━━━━━━━━"""

    # 3. 发送到钉钉
    success = send_to_dingtalk(message)

    if success:
        print(f"✅ 金价已推送到钉钉: {price} {unit}", file=sys.stderr)
    else:
        print(f"❌ 推送失败", file=sys.stderr)

    return success

if __name__ == '__main__':
    success = push_gold_price_to_dingtalk()
    sys.exit(0 if success else 1)
