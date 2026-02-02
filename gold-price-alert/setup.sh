#!/bin/bash
# 黄金价格推送 - 一键安装脚本

set -e

echo "🚀 开始安装黄金价格推送系统..."

# 检查 Python3
if ! command -v python3 &> /dev/null; then
    echo "❌ 未检测到 Python3，请先安装 Python3"
    exit 1
fi

echo "✅ Python3 已安装: $(python3 --version)"

# 安装 Python 依赖
echo "📦 安装 Python 依赖..."
pip3 install -r requirements.txt

# 检查 Chrome
if ! command -v google-chrome &> /dev/null && ! command -v chromium-browser &> /dev/null; then
    echo "⚠️  未检测到 Chrome 浏览器"
    echo "正在安装 Chrome..."

    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$ID
    else
        echo "❌ 无法检测系统类型，请手动安装 Chrome"
        exit 1
    fi

    case $OS in
        ubuntu|debian)
            wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/chrome.deb
            sudo dpkg -i /tmp/chrome.deb || sudo apt-get install -f -y
            rm /tmp/chrome.deb
            ;;
        centos|rhel|fedora)
            sudo yum install -y google-chrome-stable
            ;;
        *)
            echo "❌ 不支持的系统: $OS"
            exit 1
            ;;
    esac
fi

echo "✅ Chrome 已安装"

# 设置执行权限
chmod +x scripts/*.sh scripts/*.py

echo ""
echo "✅ 安装完成！"
echo ""
echo "📝 下一步："
echo "1. 编辑 scripts/push_to_dingtalk_webhook.py，配置钉钉 Webhook"
echo "2. 运行测试：bash scripts/push_gold_price.sh"
echo "3. 设置定时任务：crontab -e"
