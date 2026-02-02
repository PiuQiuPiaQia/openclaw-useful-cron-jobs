# 公共工具库

## 📁 目录结构

```
lib/
├── __init__.py       # Python 包初始化
└── dingtalk.py       # 钉钉推送工具库
```

## 🔔 dingtalk.py - 钉钉推送工具

### 功能特性

- ✅ 自动从项目 `.env` 文件读取配置
- ✅ 支持加签验证
- ✅ 支持文本和 Markdown 格式
- ✅ 简洁的 API

### 使用方法

#### 方式一：快捷函数（推荐）

```python
from lib.dingtalk import send, send_markdown

# 发送文本消息
send("这是一条测试消息")

# 发送 Markdown 消息
send_markdown("标题", "**粗体**文字")
```

#### 方式二：完整函数

```python
from lib.dingtalk import send_to_dingtalk, send_markdown_to_dingtalk

# 发送文本消息
message = """📈 价格提醒

━━━━━━━━━━━━━━━
💰 价格：100 元
🕐 时间：2024-02-02 12:00:00
━━━━━━━━━━━━━━━"""

send_to_dingtalk(message)

# 发送 Markdown 消息
markdown_text = """
### 标题
**粗体**
*斜体*
- 列表项1
- 列表项2
"""

send_markdown_to_dingtalk("标题", markdown_text)
```

#### 方式三：自定义 Webhook

```python
from lib.dingtalk import send_to_dingtalk

# 使用自定义 Webhook（不读取 .env）
custom_url = "https://oapi.dingtalk.com/robot/send?access_token=CUSTOM_TOKEN"
custom_secret = "SECCUSTOM_SECRET"

send_to_dingtalk(
    "消息内容",
    webhook_url=custom_url,
    sign_secret=custom_secret
)
```

### API 参考

#### `send_to_dingtalk(message, webhook_url=None, sign_secret=None)`

发送文本消息到钉钉

**参数：**
- `message` (str): 消息内容
- `webhook_url` (str, 可选): Webhook URL，默认从环境变量读取
- `sign_secret` (str, 可选): 加签密钥，默认从环境变量读取

**返回：**
- `bool`: 发送成功返回 True，失败返回 False

#### `send_markdown_to_dingtalk(title, text, webhook_url=None, sign_secret=None)`

发送 Markdown 格式消息到钉钉

**参数：**
- `title` (str): 消息标题
- `text` (str): Markdown 格式的消息内容
- `webhook_url` (str, 可选): Webhook URL，默认从环境变量读取
- `sign_secret` (str, 可选): 加签密钥，默认从环境变量读取

**返回：**
- `bool`: 发送成功返回 True，失败返回 False

#### `send(message)`

快捷发送文本消息（使用环境变量配置）

**参数：**
- `message` (str): 消息内容

**返回：**
- `bool`: 发送成功返回 True，失败返回 False

#### `send_markdown(title, text)`

快捷发送 Markdown 消息（使用环境变量配置）

**参数：**
- `title` (str): 消息标题
- `text` (str): Markdown 格式的消息内容

**返回：**
- `bool`: 发送成功返回 True，失败返回 False

### 配置

工具会自动从项目根目录的 `.env` 文件读取配置：

```bash
# 钉钉 Webhook 配置
DINGTALK_WEBHOOK_URL=https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN
DINGTALK_SIGN_SECRET=SECYOUR_SECRET
```

### 示例

#### 示例 1：简单消息推送

```python
#!/usr/bin/env python3
import sys
from pathlib import Path

# 添加 lib 目录到路径
lib_path = Path(__file__).parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from dingtalk import send

# 发送消息
message = "✅ 任务完成！"
send(message)
```

#### 示例 2：价格提醒

```python
#!/usr/bin/env python3
import sys
from pathlib import Path
from datetime import datetime

lib_path = Path(__file__).parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from dingtalk import send

price = 999.99
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

message = f"""📈 价格提醒

━━━━━━━━━━━━━━━
💰 当前价格：{price} 元
🕐 更新时间：{timestamp}
━━━━━━━━━━━━━━━"""

send(message)
```

#### 示例 3：Markdown 格式

```python
#!/usr/bin/env python3
import sys
from pathlib import Path

lib_path = Path(__file__).parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from dingtalk import send_markdown

title = "系统通知"
text = """
### 📊 数据报告

| 项目 | 数值 |
|------|------|
| CPU  | 50%  |
| 内存 | 60%  |
| 磁盘 | 70%  |

> 备注信息
"""

send_markdown(title, text)
```

### 测试

```bash
cd /home/openclaw-useful-cron-jobs
python3 lib/dingtalk.py
```

## 🚀 添加新的工具

要添加新的公共工具：

1. 在 `lib/` 目录创建新的 Python 文件
2. 实现功能并导出接口
3. 在 `lib/__init__.py` 中导出
4. 更新本文档

## 📝 依赖

工具库依赖以下 Python 包：

- `requests` - HTTP 请求

确保在项目中安装：

```bash
pip3 install requests
```
