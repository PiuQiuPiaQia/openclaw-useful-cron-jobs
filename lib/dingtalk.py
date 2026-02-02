#!/usr/bin/env python3
"""
钉钉 Webhook 推送工具库
从项目根目录的 .env 文件读取配置
"""

import os
import sys
import json
import hmac
import hashlib
import base64
import urllib.parse
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

def generate_sign(timestamp, secret):
    """
    生成钉钉加签
    
    Args:
        timestamp: 时间戳（毫秒）
        secret: 加签密钥
    
    Returns:
        str: 加签后的签名
    """
    secret_enc = secret.encode('utf-8')
    string_to_sign = f'{timestamp}\n{secret}'
    string_to_sign_enc = string_to_sign.encode('utf-8')
    
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    
    return sign

def send_to_dingtalk(message, webhook_url=None, sign_secret=None):
    """
    发送消息到钉钉 Webhook（支持加签）
    
    Args:
        message: 要发送的消息内容
        webhook_url: Webhook URL（可选，默认从环境变量读取）
        sign_secret: 加签密钥（可选，默认从环境变量读取）
    
    Returns:
        bool: 发送成功返回 True，失败返回 False
    """
    # 加载环境变量配置
    load_env_config()
    
    # 从参数或环境变量获取配置
    webhook_url = webhook_url or os.getenv('DINGTALK_WEBHOOK_URL', '')
    sign_secret = sign_secret or os.getenv('DINGTALK_SIGN_SECRET', '')
    
    if not webhook_url:
        print("❌ 错误：未配置钉钉 Webhook URL", file=sys.stderr)
        return False
    
    try:
        # 如果有加签密钥，使用加签
        if sign_secret:
            timestamp = str(int(datetime.now().timestamp() * 1000))
            sign = generate_sign(timestamp, sign_secret)
            url = f"{webhook_url}&timestamp={timestamp}&sign={sign}"
        else:
            url = webhook_url
        
        payload = {
            "msgtype": "text",
            "text": {
                "content": message
            }
        }
        
        response = requests.post(url, json=payload, timeout=10)
        
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

def send_markdown_to_dingtalk(title, text, webhook_url=None, sign_secret=None):
    """
    发送 Markdown 格式消息到钉钉
    
    Args:
        title: 消息标题
        text: Markdown 格式的消息内容
        webhook_url: Webhook URL（可选）
        sign_secret: 加签密钥（可选）
    
    Returns:
        bool: 发送成功返回 True，失败返回 False
    """
    # 加载环境变量配置
    load_env_config()
    
    # 从参数或环境变量获取配置
    webhook_url = webhook_url or os.getenv('DINGTALK_WEBHOOK_URL', '')
    sign_secret = sign_secret or os.getenv('DINGTALK_SIGN_SECRET', '')
    
    if not webhook_url:
        print("❌ 错误：未配置钉钉 Webhook URL", file=sys.stderr)
        return False
    
    try:
        # 如果有加签密钥，使用加签
        if sign_secret:
            timestamp = str(int(datetime.now().timestamp() * 1000))
            sign = generate_sign(timestamp, sign_secret)
            url = f"{webhook_url}&timestamp={timestamp}&sign={sign}"
        else:
            url = webhook_url
        
        payload = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            }
        }
        
        response = requests.post(url, json=payload, timeout=10)
        
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
