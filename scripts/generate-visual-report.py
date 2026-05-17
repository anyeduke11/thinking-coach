#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
可视化学习报告生成器 - GROW教练式思维模型引导器 v1.4

功能：
1. 9大场景雷达图（可视化展示掌握度）
2. 学习成长曲线（时间轴展示进步）
3. 薄弱场景热力图（直观显示需要加强的地方）

用法：
  python generate-visual-report.py --data user_profile.json --output ./reports/
  python generate-visual-report.py --demo  # 使用示例数据生成演示报告
"""

import json
import os
import argparse
from datetime import datetime, timedelta

import matplotlib
matplotlib.use('Agg')  # 无头模式，不弹出窗口
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ============================================================
# 中文字体配置
# ============================================================
def setup_chinese_font():
    """配置中文字体，优先使用系统中可用的中文字体"""
    chinese_fonts = [
        'Microsoft YaHei', 'SimHei', 'PingFang SC', 'Noto Sans CJK SC',
        'WenQuanYi Micro Hei', 'STHeiti', 'Hiragino Sans GB', 'Source Han Sans CN'
    ]
    
    available_fonts = set(f.name for f in fm.fontManager.ttflist)
    
    for font_name in chinese_fonts:
        if font_name in available_fonts:
            plt.rcParams['font.sans-serif'] = [font_name] + plt.rcParams['font.sans-serif']
            plt.rcParams['axes.unicode_minus'] = False
            print(f"[字体] 使用: {font_name}")
            return font_name
    
    # 回退方案：尝试查找系统中任意中文字体文件
    print("[字体] 警告: 未找到推荐中文字体，尝试自动检测...")
    plt.rcParams['axes.unicode_minus'] = False
    return None

# ============================================================
# 配色方案
# ============================================================
COLORS = {
    'primary': '#4A90D9',      # 主色蓝
    'secondary': '#50C878',    # 绿色
    'accent': '#FF6B6B',       # 红色
    'warning': '#FFB347',      # 橙色
    'bg': '#FAFBFC',           # 背景色
    'grid': '#E8ECF0',         # 网格色
    'text': '#2C3E50',         # 文字色
    'text_light': '#7F8C8D',   # 浅文字色
    'radar_fill': '#4A90D9',
    'radar_line': '#4A90D9',
    'heatmap_high': '#FF6B6B',
    'heatmap_mid': '#FFB347',
    'heatmap_low': '#50C878',
}

# 9大场景定义
SCENARIOS = [
    ('S01', '认知校准'),
    ('S02', '学习提升'),
    ('S03', '问题解决'),
    ('S04', '系统洞察'),
    ('S05', '数据判断'),
    ('S06', '决策分析'),
    ('S07', '冲突应对'),
    ('S08', '潜能释放'),
    ('S09', '市场策略'),
]

# ============================================================
# 图表1: 9大场景雷达图
# ============================================================
def create_radar_chart(scenario_data, output_path):
    """
    生成9大场景掌握度雷达图
    
    Args:
        scenario_data: dict, 格式 {'S01': {'name': '认知校准', 'score': 8, 'max': 10}, ...}
        output_path: str, 图片保存路径
    """
    labels = []
    values = []
    
    for code, name in SCENARIOS:
        if code in scenario_data:
            labels.append(f"{code}\n{scenario_data[code]['name']}")
            # 归一化到 0-100
            score = scenario_data[code].get('score', 0)
            max_score = scenario_data[code].get('max', 10)
            values.append(round(score / max_score * 100, 1))
        else:
            labels.append(f"{code}\n{name}")
            values.append(0)
    
    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    
    # 闭合雷达图
    values_closed = values + values[:1]
    angles_closed = angles + angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 11), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor(COLORS['bg'])
    ax.set_facecolor(COLORS['bg'])
    
    # 绘制雷达区域
    ax.fill(angles_closed, values_closed, color=COLORS['radar_fill'], alpha=0.3)
    ax.plot(angles_closed, values_closed, color=COLORS['radar_line'], linewidth=2.5, linestyle='-')
    
    # 绘制数据点
    ax.scatter(angles, values, color=COLORS['radar_line'], s=80, zorder=5, edgecolors='white', linewidth=2)
    
    # 在数据点旁标注分数
    for angle, value, label in zip(angles, values, labels):
        short_label = label.split('\n')[0]
        offset = 8 if value > 50 else -12
        ax.annotate(
            f"{value}%", 
            xy=(angle, value),
            xytext=(angle, value + offset),
            textcoords='data',
            ha='center', va='center',
            fontsize=11, fontweight='bold',
            color=COLORS['text'],
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=COLORS['grid'], alpha=0.8)
        )
    
    # 设置刻度
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], fontsize=8, color=COLORS['text_light'])
    
    # 设置标签
    ax.set_xticks(angles)
    ax.set_xticklabels(labels, fontsize=11, fontweight='bold', color=COLORS['text'])
    
    # 网格样式
    ax.grid(color=COLORS['grid'], linestyle='-', linewidth=0.8, alpha=0.7)
    ax.spines['polar'].set_color(COLORS['grid'])
    
    # 标题
    ax.set_title('9大场景掌握度雷达图', fontsize=18, fontweight='bold', 
                  color=COLORS['text'], pad=30)
    
    # 添加掌握度等级标注
    avg_score = np.mean(values)
    if avg_score >= 80:
        level = "精通级"
        level_color = COLORS['secondary']
    elif avg_score >= 60:
        level = "熟练级"
        level_color = COLORS['primary']
    elif avg_score >= 40:
        level = "练习级"
        level_color = COLORS['warning']
    else:
        level = "入门级"
        level_color = COLORS['accent']
    
    fig.text(0.5, 0.02, f"综合掌握度: {avg_score:.0f}% | 训练等级: {level}", 
             ha='center', fontsize=13, fontweight='bold', color=level_color,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=level_color, alpha=0.9))
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['bg'])
    plt.close()
    print(f"[雷达图] 已保存: {output_path}")


# ============================================================
# 图表2: 学习成长曲线
# ============================================================
def create_growth_curve(history_data, output_path):
    """
    生成学习成长曲线（时间轴展示进步）
    
    Args:
        history_data: list, 格式 [{'date': '2026-05-01', 'total_sessions': 5, 'scenarios_covered': 3, 'models_mastered': 8, 'avg_score': 65}, ...]
        output_path: str, 图片保存路径
    """
    if not history_data or len(history_data) < 2:
        print("[成长曲线] 数据不足，需要至少2个时间点的数据")
        return
    
    dates = [h['date'] for h in history_data]
    total_sessions = [h.get('total_sessions', 0) for h in history_data]
    scenarios_covered = [h.get('scenarios_covered', 0) for h in history_data]
    models_mastered = [h.get('models_mastered', 0) for h in history_data]
    avg_scores = [h.get('avg_score', 0) for h in history_data]
    
    # 格式化日期标签
    date_labels = []
    for d in dates:
        try:
            dt = datetime.strptime(d, '%Y-%m-%d')
            date_labels.append(dt.strftime('%m/%d'))
        except:
            date_labels.append(d)
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.patch.set_facecolor(COLORS['bg'])
    fig.suptitle('学习成长曲线', fontsize=20, fontweight='bold', color=COLORS['text'], y=0.98)
    
    # --- 子图1: 累计使用次数 ---
    ax1 = axes[0, 0]
    ax1.set_facecolor(COLORS['bg'])
    ax1.fill_between(range(len(dates)), total_sessions, alpha=0.15, color=COLORS['primary'])
    ax1.plot(range(len(dates)), total_sessions, color=COLORS['primary'], linewidth=2.5, marker='o', markersize=8)
    for i, v in enumerate(total_sessions):
        ax1.annotate(str(v), (i, v), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')
    ax1.set_xticks(range(len(dates)))
    ax1.set_xticklabels(date_labels, fontsize=10)
    ax1.set_title('累计使用次数', fontsize=14, fontweight='bold', color=COLORS['text'])
    ax1.set_ylabel('次数', fontsize=11, color=COLORS['text_light'])
    ax1.grid(axis='y', color=COLORS['grid'], linestyle='--', alpha=0.5)
    
    # --- 子图2: 场景覆盖数 ---
    ax2 = axes[0, 1]
    ax2.set_facecolor(COLORS['bg'])
    ax2.bar(range(len(dates)), scenarios_covered, color=COLORS['secondary'], alpha=0.7, width=0.6, edgecolor='white', linewidth=1.5)
    ax2.axhline(y=9, color=COLORS['accent'], linestyle='--', linewidth=1.5, alpha=0.7, label='全覆盖目标(9)')
    for i, v in enumerate(scenarios_covered):
        ax2.annotate(f"{v}/9", (i, v), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, fontweight='bold')
    ax2.set_xticks(range(len(dates)))
    ax2.set_xticklabels(date_labels, fontsize=10)
    ax2.set_title('场景覆盖数', fontsize=14, fontweight='bold', color=COLORS['text'])
    ax2.set_ylabel('场景数', fontsize=11, color=COLORS['text_light'])
    ax2.set_ylim(0, 10)
    ax2.legend(fontsize=9, loc='upper left')
    ax2.grid(axis='y', color=COLORS['grid'], linestyle='--', alpha=0.5)
    
    # --- 子图3: 模型掌握数 ---
    ax3 = axes[1, 0]
    ax3.set_facecolor(COLORS['bg'])
    ax3.fill_between(range(len(dates)), models_mastered, alpha=0.15, color=COLORS['warning'])
    ax3.plot(range(len(dates)), models_mastered, color=COLORS['warning'], linewidth=2.5, marker='s', markersize=8)
    for i, v in enumerate(models_mastered):
        ax3.annotate(f"{v}/94", (i, v), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')
    ax3.set_xticks(range(len(dates)))
    ax3.set_xticklabels(date_labels, fontsize=10)
    ax3.set_title('掌握模型数', fontsize=14, fontweight='bold', color=COLORS['text'])
    ax3.set_ylabel('模型数', fontsize=11, color=COLORS['text_light'])
    ax3.grid(axis='y', color=COLORS['grid'], linestyle='--', alpha=0.5)
    
    # --- 子图4: 平均掌握度 ---
    ax4 = axes[1, 1]
    ax4.set_facecolor(COLORS['bg'])
    gradient_colors = []
    for s in avg_scores:
        if s >= 80:
            gradient_colors.append(COLORS['secondary'])
        elif s >= 60:
            gradient_colors.append(COLORS['primary'])
        elif s >= 40:
            gradient_colors.append(COLORS['warning'])
        else:
            gradient_colors.append(COLORS['accent'])
    ax4.bar(range(len(dates)), avg_scores, color=gradient_colors, alpha=0.7, width=0.6, edgecolor='white', linewidth=1.5)
    ax4.axhline(y=80, color=COLORS['secondary'], linestyle='--', linewidth=1.5, alpha=0.7, label='精通(80)')
    ax4.axhline(y=60, color=COLORS['primary'], linestyle='--', linewidth=1.5, alpha=0.7, label='熟练(60)')
    for i, v in enumerate(avg_scores):
        ax4.annotate(f"{v}%", (i, v), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, fontweight='bold')
    ax4.set_xticks(range(len(dates)))
    ax4.set_xticklabels(date_labels, fontsize=10)
    ax4.set_title('平均掌握度', fontsize=14, fontweight='bold', color=COLORS['text'])
    ax4.set_ylabel('掌握度', fontsize=11, color=COLORS['text_light'])
    ax4.set_ylim(0, 105)
    ax4.legend(fontsize=9, loc='upper left')
    ax4.grid(axis='y', color=COLORS['grid'], linestyle='--', alpha=0.5)
    
    # 通用样式
    for ax in axes.flat:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(COLORS['grid'])
        ax.spines['bottom'].set_color(COLORS['grid'])
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['bg'])
    plt.close()
    print(f"[成长曲线] 已保存: {output_path}")


# ============================================================
# 图表3: 薄弱场景热力图
# ============================================================
def create_weakness_heatmap(weakness_data, output_path):
    """
    生成薄弱场景热力图
    
    Args:
        weakness_data: dict, 格式 {
            'dimensions': ['使用频率', '掌握深度', '完成度', '满意度', '活跃度'],
            'scenarios': {
                'S01': {'name': '认知校准', 'scores': [85, 70, 90, 80, 75]},
                ...
            }
        }
        output_path: str, 图片保存路径
    """
    dimensions = weakness_data.get('dimensions', ['使用频率', '掌握深度', '完成度', '满意度', '活跃度'])
    scenarios = weakness_data.get('scenarios', {})
    
    if not scenarios:
        print("[热力图] 无数据")
        return
    
    # 构建矩阵
    scenario_codes = [code for code, _ in SCENARIOS if code in scenarios]
    scenario_names = [f"{code}\n{scenarios[code]['name']}" for code in scenario_codes]
    
    matrix = np.array([scenarios[code]['scores'] for code in scenario_codes])
    
    fig, ax = plt.subplots(figsize=(14, 9))
    fig.patch.set_facecolor(COLORS['bg'])
    ax.set_facecolor(COLORS['bg'])
    
    # 自定义颜色映射
    from matplotlib.colors import LinearSegmentedColormap
    cmap_colors = ['#FF6B6B', '#FFB347', '#FFE066', '#A8E6CF', '#50C878']
    cmap = LinearSegmentedColormap.from_list('custom', cmap_colors, N=256)
    
    # 绘制热力图
    im = ax.imshow(matrix, cmap=cmap, aspect='auto', vmin=0, vmax=100)
    
    # 添加数值标注
    for i in range(len(scenario_codes)):
        for j in range(len(dimensions)):
            val = matrix[i, j]
            text_color = 'white' if val < 40 else COLORS['text']
            ax.text(j, i, f"{val}", ha='center', va='center', 
                    fontsize=13, fontweight='bold', color=text_color)
    
    # 设置坐标轴
    ax.set_xticks(range(len(dimensions)))
    ax.set_xticklabels(dimensions, fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_yticks(range(len(scenario_codes)))
    ax.set_yticklabels(scenario_names, fontsize=11, fontweight='bold', color=COLORS['text'])
    
    # 添加颜色条
    cbar = plt.colorbar(im, ax=ax, shrink=0.8, aspect=30, pad=0.02)
    cbar.set_label('评分 (0-100)', fontsize=11, color=COLORS['text_light'])
    cbar.ax.tick_params(labelsize=10, colors=COLORS['text_light'])
    
    # 标注薄弱区域（低于40分的单元格加边框）
    for i in range(len(scenario_codes)):
        for j in range(len(dimensions)):
            if matrix[i, j] < 40:
                rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, 
                                     linewidth=3, edgecolor=COLORS['accent'], facecolor='none')
                ax.add_patch(rect)
    
    # 标题
    ax.set_title('薄弱场景热力图', fontsize=18, fontweight='bold', color=COLORS['text'], pad=15)
    
    # 图例说明
    fig.text(0.5, 0.01, 
             "颜色越绿 = 表现越好 | 颜色越红 = 越需加强 | 红框标注 = 薄弱区域（<40分）",
             ha='center', fontsize=11, color=COLORS['text_light'],
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=COLORS['grid'], alpha=0.9))
    
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['bg'])
    plt.close()
    print(f"[热力图] 已保存: {output_path}")


# ============================================================
# 综合报告生成
# ============================================================
def generate_full_report(scenario_data, history_data, weakness_data, output_dir):
    """
    生成完整的可视化学习报告（包含3张图表）
    
    Args:
        scenario_data: dict, 9大场景掌握度数据
        history_data: list, 历史成长数据
        weakness_data: dict, 薄弱环节分析数据
        output_dir: str, 输出目录
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # 1. 雷达图
    radar_path = os.path.join(output_dir, f'radar_chart_{timestamp}.png')
    create_radar_chart(scenario_data, radar_path)
    
    # 2. 成长曲线
    growth_path = os.path.join(output_dir, f'growth_curve_{timestamp}.png')
    create_growth_curve(history_data, growth_path)
    
    # 3. 热力图
    heatmap_path = os.path.join(output_dir, f'weakness_heatmap_{timestamp}.png')
    create_weakness_heatmap(weakness_data, heatmap_path)
    
    print(f"\n[报告] 可视化报告已生成到: {output_dir}")
    print(f"  - 雷达图: {radar_path}")
    print(f"  - 成长曲线: {growth_path}")
    print(f"  - 热力图: {heatmap_path}")
    
    return {
        'radar_chart': radar_path,
        'growth_curve': growth_path,
        'weakness_heatmap': heatmap_path,
        'timestamp': timestamp
    }


# ============================================================
# 示例数据
# ============================================================
def get_demo_data():
    """生成演示用的示例数据"""
    # 9大场景掌握度
    scenario_data = {
        'S01': {'name': '认知校准', 'score': 8, 'max': 10},
        'S02': {'name': '学习提升', 'score': 4, 'max': 10},
        'S03': {'name': '问题解决', 'score': 6, 'max': 10},
        'S04': {'name': '系统洞察', 'score': 2, 'max': 10},
        'S05': {'name': '数据判断', 'score': 5, 'max': 10},
        'S06': {'name': '决策分析', 'score': 8, 'max': 10},
        'S07': {'name': '冲突应对', 'score': 3, 'max': 10},
        'S08': {'name': '潜能释放', 'score': 7, 'max': 10},
        'S09': {'name': '市场策略', 'score': 1, 'max': 10},
    }
    
    # 历史成长数据（模拟8周）
    history_data = []
    base_date = datetime(2026, 3, 1)
    for i in range(8):
        week_date = base_date + timedelta(weeks=i)
        history_data.append({
            'date': week_date.strftime('%Y-%m-%d'),
            'total_sessions': 2 + i * 3 + np.random.randint(0, 3),
            'scenarios_covered': min(9, 2 + i),
            'models_mastered': min(94, 3 + i * 7 + np.random.randint(0, 5)),
            'avg_score': min(100, 25 + i * 10 + np.random.randint(-5, 8)),
        })
    
    # 薄弱环节分析
    weakness_data = {
        'dimensions': ['使用频率', '掌握深度', '完成度', '满意度', '活跃度'],
        'scenarios': {
            'S01': {'name': '认知校准', 'scores': [85, 70, 90, 82, 75]},
            'S02': {'name': '学习提升', 'scores': [40, 35, 55, 60, 30]},
            'S03': {'name': '问题解决', 'scores': [60, 55, 70, 65, 50]},
            'S04': {'name': '系统洞察', 'scores': [20, 15, 30, 35, 10]},
            'S05': {'name': '数据判断', 'scores': [50, 45, 60, 55, 40]},
            'S06': {'name': '决策分析', 'scores': [90, 85, 95, 88, 80]},
            'S07': {'name': '冲突应对', 'scores': [30, 25, 45, 50, 20]},
            'S08': {'name': '潜能释放', 'scores': [70, 65, 80, 75, 60]},
            'S09': {'name': '市场策略', 'scores': [10, 8, 20, 25, 5]},
        }
    }
    
    return scenario_data, history_data, weakness_data


# ============================================================
# 从用户档案JSON加载数据
# ============================================================
def load_user_data(json_path):
    """
    从用户档案JSON文件加载数据
    
    JSON格式示例:
    {
        "scenarios": {
            "S01": {"name": "认知校准", "score": 8, "max": 10},
            ...
        },
        "history": [
            {"date": "2026-05-01", "total_sessions": 5, "scenarios_covered": 3, "models_mastered": 8, "avg_score": 65},
            ...
        ],
        "weakness": {
            "dimensions": ["使用频率", "掌握深度", "完成度", "满意度", "活跃度"],
            "scenarios": {
                "S01": {"name": "认知校准", "scores": [85, 70, 90, 82, 75]},
                ...
            }
        }
    }
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    scenario_data = data.get('scenarios', {})
    history_data = data.get('history', [])
    weakness_data = data.get('weakness', {})
    
    return scenario_data, history_data, weakness_data


# ============================================================
# 主入口
# ============================================================
def main():
    parser = argparse.ArgumentParser(description='GROW教练式思维模型引导器 - 可视化学习报告生成器')
    parser.add_argument('--data', type=str, help='用户档案JSON文件路径')
    parser.add_argument('--output', type=str, default='./reports/', help='输出目录（默认: ./reports/）')
    parser.add_argument('--demo', action='store_true', help='使用示例数据生成演示报告')
    parser.add_argument('--radar-only', action='store_true', help='仅生成雷达图')
    parser.add_argument('--curve-only', action='store_true', help='仅生成成长曲线')
    parser.add_argument('--heatmap-only', action='store_true', help='仅生成热力图')
    
    args = parser.parse_args()
    
    # 配置字体
    setup_chinese_font()
    
    if args.demo:
        scenario_data, history_data, weakness_data = get_demo_data()
    elif args.data:
        scenario_data, history_data, weakness_data = load_user_data(args.data)
    else:
        print("请指定 --data <用户档案.json> 或使用 --demo 生成演示报告")
        parser.print_help()
        return
    
    os.makedirs(args.output, exist_ok=True)
    
    if args.radar_only:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        create_radar_chart(scenario_data, os.path.join(args.output, f'radar_chart_{timestamp}.png'))
    elif args.curve_only:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        create_growth_curve(history_data, os.path.join(args.output, f'growth_curve_{timestamp}.png'))
    elif args.heatmap_only:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        create_weakness_heatmap(weakness_data, os.path.join(args.output, f'weakness_heatmap_{timestamp}.png'))
    else:
        generate_full_report(scenario_data, history_data, weakness_data, args.output)


if __name__ == '__main__':
    main()
