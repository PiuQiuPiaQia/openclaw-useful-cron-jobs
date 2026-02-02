#!/usr/bin/env python3
"""
抓取真实黄金价格 - 使用 Selenium + Chrome 无头浏览器
完全参考: https://github.com/wanghao221/gold-price-alert
数据来源: 京东金融

使用 webdriver-manager 自动管理 ChromeDriver
"""

import sys
import re
import json
import time
from datetime import datetime

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"缺少依赖库: {e}", file=sys.stderr)
    print("请安装: pip3 install selenium webdriver-manager beautifulsoup4", file=sys.stderr)
    sys.exit(1)

def fetch_gold_price_selenium():
    """
    使用 Selenium + Chrome 无头浏览器从京东金融获取实时金价
    完全参考 wanghao221/gold-price-alert 的实现
    """
    driver = None

    try:
        print("正在启动 Chrome 浏览器...", file=sys.stderr)

        # 设置无头浏览器
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 无头模式
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("window-size=1920,1080")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

        # 使用 webdriver-manager 自动管理 ChromeDriver
        chromedriver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

        print("浏览器启动成功，正在访问京东金融...", file=sys.stderr)

        # 目标页面（与参考脚本完全相同）
        url = 'https://m.jr.jd.com/finance-gold/msjgold/homepage?from=fhc&ip=66.249.71.78&orderSource=6&ptag=16337378.0.1'

        # 访问页面
        driver.get(url)

        # 等待 JS 渲染（与参考脚本相同）
        time.sleep(3)

        print("页面加载完成，正在解析...", file=sys.stderr)

        # 获取页面源码
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 提取实时金价（与参考脚本完全相同的逻辑）
        all_titles = soup.find_all('span', class_='gold-price-persent-title')
        gold_price = None

        for title in all_titles:
            if '实时金价' in title.get_text():
                match = re.search(r'(\d+\.\d+)', title.get_text())
                if match:
                    gold_price = float(match.group(1))
                    break

        if gold_price:
            print(f"✅ 成功获取实时金价: {gold_price} 元/克", file=sys.stderr)
            return {
                'price': round(gold_price, 2),
                'unit': '元/克',
                'source': '京东金融（Selenium 实时抓取）',
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'note': '使用 Selenium + Chrome 无头浏览器，完全参考 wanghao221/gold-price-alert'
            }
        else:
            print("未找到实时金价元素", file=sys.stderr)
            return None

    except Exception as e:
        print(f"Selenium 抓取失败: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return None

    finally:
        # 确保关闭浏览器
        if driver:
            try:
                driver.quit()
                print("浏览器已关闭", file=sys.stderr)
            except:
                pass

def fetch_gold_price():
    """主函数：使用 Selenium 获取真实金价"""

    result = fetch_gold_price_selenium()

    if result:
        return result
    else:
        return None

if __name__ == '__main__':
    result = fetch_gold_price()

    if result:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        # Selenium 失败，返回错误信息
        print(json.dumps({
            'error': '无法获取金价数据',
            'source': '京东金融（Selenium）',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'note': 'Selenium 抓取失败，请检查网络连接和 Chrome 浏览器'
        }, ensure_ascii=False, indent=2))
        sys.exit(1)
