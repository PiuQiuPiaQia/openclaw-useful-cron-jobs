#!/bin/bash
# OpenClaw Useful Cron Jobs - 统一安装入口

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 项目根目录
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${CYAN}"
cat << "EOF"
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        OpenClaw Useful Cron Jobs - 安装向导                 ║
║                                                              ║
║        选择要安装的项目                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# 检查 Python3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ 未检测到 Python3，请先安装 Python3${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Python3 已安装: $(python3 --version)${NC}"

# 检查系统配置
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}📋 第一步：选择要安装的项目${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 定义项目列表
declare -A PROJECTS
declare -A PROJECT_DESCRIPTIONS

PROJECTS[1]="gold-price-alert"
PROJECT_DESCRIPTIONS[1]="黄金价格提醒 - 实时金价监控和钉钉推送"

# 显示项目列表
for key in "${!PROJECTS[@]}"; do
    echo -e "  ${CYAN}[${key}]${NC} ${PROJECT_DESCRIPTIONS[$key]}"
done

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 获取用户选择
echo -e "${YELLOW}请输入要安装的项目编号（多个项目用空格分隔，例如: 1）:${NC}"
read -p "> " choices

if [ -z "$choices" ]; then
    echo -e "${RED}❌ 未选择任何项目${NC}"
    exit 1
fi

# 解析用户选择
selected_projects=()
for choice in $choices; do
    if [ -n "${PROJECTS[$choice]}" ]; then
        selected_projects+=("${PROJECTS[$choice]}")
    else
        echo -e "${RED}⚠️  无效的项目编号: $choice（已跳过）${NC}"
    fi
done

if [ ${#selected_projects[@]} -eq 0 ]; then
    echo -e "${RED}❌ 没有有效的项目被选择${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}✅ 已选择项目:${NC}"
for project in "${selected_projects[@]}"; do
    echo -e "  • ${CYAN}$project${NC}"
done
echo ""

# 确认安装
echo -e "${YELLOW}是否开始安装？ [y/N]${NC}"
read -p "> " confirm

if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}❌ 安装已取消${NC}"
    exit 0
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}📋 第二步：配置钉钉 Webhook${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 检查是否已配置
if [ -f "$PROJECT_ROOT/.env" ]; then
    # 检查是否已配置钉钉
    if grep -q "DINGTALK_WEBHOOK_URL=" "$PROJECT_ROOT/.env" && \
       grep -q "DINGTALK_SIGN_SECRET=" "$PROJECT_ROOT/.env" && \
       ! grep -q "YOUR_TOKEN" "$PROJECT_ROOT/.env"; then
        echo -e "${GREEN}✅ 检测到已配置钉钉 Webhook${NC}"
        echo ""
        echo -e "${YELLOW}是否重新配置？ [y/N]${NC}"
        read -p "> " reconfigure

        if [[ ! "$reconfigure" =~ ^[Yy]$ ]]; then
            echo -e "${GREEN}✅ 跳过配置步骤${NC}"
            echo ""
            configure_done=true
        else
            configure_done=false
        fi
    else
        configure_done=false
    fi
else
    configure_done=false
fi

if [ "$configure_done" = false ]; then
    echo -e "${YELLOW}请先在钉钉群中添加自定义机器人：${NC}"
    echo -e "  1. 群设置 → 智能群助手 → 添加机器人 → 自定义"
    echo -e "  2. 机器人名字：黄金价格播报"
    echo -e "  3. 安全设置：选择'加签'"
    echo -e "  4. 复制 Webhook URL 和加签密钥"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    read -p "请输入 Webhook URL: " WEBHOOK_URL
    read -p "请输入加签密钥: " SIGN_SECRET

    if [ -z "$WEBHOOK_URL" ] || [z "$SIGN_SECRET" ]; then
        echo -e "${RED}❌ 错误：Webhook URL 和加签密钥不能为空${NC}"
        exit 1
    fi

    # 写入到 .env 文件
    cat > "$PROJECT_ROOT/.env" << EOF
# 钉钉 Webhook 配置
DINGTALK_WEBHOOK_URL=$WEBHOOK_URL
DINGTALK_SIGN_SECRET=$SIGN_SECRET
EOF

    echo ""
    echo -e "${GREEN}✅ 配置已保存到 $PROJECT_ROOT/.env${NC}"
    echo ""

    # 测试配置
    echo -e "${YELLOW}🧪 测试钉钉推送...${NC}"
    python3 -c "
import sys
from pathlib import Path
lib_path = Path('$PROJECT_ROOT/lib')
sys.path.insert(0, str(lib_path))
from dingtalk import send
send('🔔 配置测试成功！OpenClaw Useful Cron Jobs 已就绪。')
" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ 钉钉推送测试成功${NC}"
    else
        echo -e "${YELLOW}⚠️  钉钉推送测试失败，请检查配置是否正确${NC}"
    fi
    echo ""
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}📋 第三步：安装项目${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 安装每个项目
for project in "${selected_projects[@]}"; do
    project_path="$PROJECT_ROOT/$project"

    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}📦 安装项目: $project${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    # 检查项目目录是否存在
    if [ ! -d "$project_path" ]; then
        echo -e "${RED}❌ 项目目录不存在: $project_path${NC}"
        continue
    fi

    # 检查 setup.sh 是否存在
    if [ ! -f "$project_path/setup.sh" ]; then
        echo -e "${RED}❌ 未找到 setup.sh: $project_path/setup.sh${NC}"
        continue
    fi

    # 执行项目的 setup.sh
    cd "$project_path"
    bash setup.sh

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $project 安装成功${NC}"
    else
        echo -e "${RED}❌ $project 安装失败${NC}"
    fi

    echo ""
done

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ 安装完成！${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${YELLOW}📝 下一步：${NC}"
echo ""
echo -e "  ${CYAN}1. 测试推送${NC}"
echo -e "     ${GREEN}bash $PROJECT_ROOT/gold-price-alert/scripts/push_gold_price.sh${NC}"
echo ""
echo -e "  ${CYAN}2. 设置定时任务${NC}"
echo -e "     ${GREEN}crontab -e${NC}"
echo -e "     ${GREEN}*/5 * * * * $PROJECT_ROOT/gold-price-alert/scripts/push_gold_price.sh${NC}"
echo ""
echo -e "  ${CYAN}3. 查看文档${NC}"
echo -e "     ${GREEN}cat $PROJECT_ROOT/README_CN.md${NC}"
echo ""
echo -e "${YELLOW}💡 提示：${NC}"
echo -e "  如需重新配置钉钉，运行：${GREEN}bash $PROJECT_ROOT/configure.sh${NC}"
echo ""
