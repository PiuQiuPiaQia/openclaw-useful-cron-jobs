#!/usr/bin/env python3
"""
钉钉 Webhook 推送工具库
从项目根目录的 .env 文件读取配置
"""

import os
import sys
import json
import requests
from datetime import datetime
from pathlib import Path

def load_env_config():
    """
    从项目根目录的 .env 文件加载配置
    """
    # 查找项目根目录（从当前脚本向上查找）
    current_path = Path(__file__).resolve()
    root_path = current_path.parent.parent

    env_file = root_path / '.env'

    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

    return root_path

def send_to_dingtalk(message, webhook_url=None):
    """
    发送消息到钉钉 Webhook（企业机器人，无需加签）

    Args:
        message: 要发送的消息内容
        webhook_url: Webhook URL（可选，默认从环境变量读取）

    Returns:
        bool: 发送成功返回 True，失败返回 False
    """
    # 加载环境变量配置
    load_env_config()

    # 从参数或环境变量获取配置
    webhook_url = webhook_url or os.getenv('DINGTALK_WEBHOOK_URL', '')

    if not webhook_url:
        print("❌ 错误：未配置钉钉 Webhook URL", file=sys.stderr)
        return False

    try:
        payload = {
            "msgtype": "text",
            "text": {
                "content": message
            }
        }

        response = requests.post(webhook_url, json=payload, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            if result.get('errcode') == 0:
                return True
            else:
                print(f"❌ 钉钉返回错误: {result}", file=sys.stderr)
                return False
        else:
            print(f"❌ HTTP 错误: {response.status_code}", file=sys.stderr)
            return False
    
    except Exception as e:
        print(f"❌ 发送到钉钉失败: {e}", file=sys.stderr)
        return False

def send_markdown_to_dingtalk(title, text, webhook_url=None):
    """
    发送 Markdown 格式消息到钉钉

    Args:
        title: 消息标题
        text: Markdown 格式的消息内容
        webhook_url: Webhook URL（可选）

    Returns:
        bool: 发送成功返回 True，失败返回 False
    """
    # 加载环境变量配置
    load_env_config()

    # 从参数或环境变量获取配置
    webhook_url = webhook_url or os.getenv('DINGTALK_WEBHOOK_URL', '')

    if not webhook_url:
        print("❌ 错误：未配置钉钉 Webhook URL", file=sys.stderr)
        return False

    try:
        payload = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            }
        }

        response = requests.post(webhook_url, json=payload, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            if result.get('errcode') == 0:
                return True
            else:
                print(f"❌ 钉钉返回错误: {result}", file=sys.stderr)
                return False
        else:
            print(f"❌ HTTP 错误: {response.status_code}", file=sys.stderr)
            return False
    
    except Exception as e:
        print(f"❌ 发送到钉钉失败: {e}", file=sys.stderr)
        return False


# 快捷函数
def send(message):
    """
    快捷发送文本消息（使用环境变量配置）
    """
    return send_to_dingtalk(message)


def send_markdown(title, text):
    """
    快捷发送 Markdown 消息（使用环境变量配置）
    """
    return send_markdown_to_dingtalk(title, text)


# if __name__ == '__main__': 用于测试
if __name__ == '__main__':
    # 测试发送
    test_message = """📈 测试消息

━━━━━━━━━━━━━━━
💰 这是一个测试消息
🕐 时间：""" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """
━━━━━━━━━━━━━━━"""

    if send(test_message):
        print("✅ 测试消息发送成功")
    else:
        print("❌ 测试消息发送失败")
        sys.exit(1)
