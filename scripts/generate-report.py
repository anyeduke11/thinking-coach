#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
汇报文档生成脚本
根据用户输入的教练对话数据，生成结构化的汇报文档
"""

import json
from datetime import datetime
from pathlib import Path

def generate_report(coaching_data: dict) -> str:
    """
    根据教练对话数据生成汇报文档
    
    Args:
        coaching_data: 包含GROW各阶段数据的字典
        
    Returns:
        生成的Markdown格式汇报文档
    """
    
    template = """# {title}

> 生成时间：{timestamp}
> 使用模型：GROW教练模型 + 根因分析 + 二阶思维

---

## 一、目标回顾

| 维度 | 内容 |
|-----|------|
| 核心目标 | {goal_primary} |
| 理想结果 | {goal_ideal} |
| 底线接受 | {goal_baseline} |

---

## 二、现状分析

### 数据概览

{reality_data}

### 根因分析

{reality_root_cause}

### 原因归类

| 类型 | 具体原因 | 能否改进 |
|-----|---------|---------|
{reality_classification}

---

## 三、策略选择

### 策略对比

| 策略 | 做法 | 优点 | 风险 |
|-----|------|-----|------|
{options_strategies}

**选择策略**：{options_selected}

### 改进方案

| 时间 | 方案 |
|-----|------|
{options_plans}

### 预判问题

| 可能的问题 | 准备的回答 |
|-----------|-----------|
{options_qa}

---

## 四、汇报框架

```
一、数据概览（30秒）
├─ {report_data_summary}

二、原因分析（2分钟）
├─ {report_cause_summary}

三、改进方案（2分钟）
├─ {report_plan_summary}

四、预期与承诺（30秒）
├─ {report_commitment}
```

---

## 五、关键话术

### 开场话术

{scripture_opening}

### 讲原因话术

{scripture_cause}

### 讲方案话术

{scripture_plan}

### 结尾话术

{scripture_ending}

---

## 六、改进计划

| 措施 | 具体动作 | 时间节点 | 责任人 | 需要支持 |
|-----|---------|---------|-------|---------|
{action_plan}

---

## 七、检查清单

| 检查项 | 是否准备好？ |
|-------|-----------|
{checklist}

---

*本文档由GROW教练式思维模型引导器自动生成*
"""
    
    # 填充模板
    report = template.format(
        title=coaching_data.get('title', '汇报方案'),
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M'),
        goal_primary=coaching_data.get('goal', {}).get('primary', ''),
        goal_ideal=coaching_data.get('goal', {}).get('ideal', ''),
        goal_baseline=coaching_data.get('goal', {}).get('baseline', ''),
        reality_data=coaching_data.get('reality', {}).get('data', ''),
        reality_root_cause=coaching_data.get('reality', {}).get('root_cause', ''),
        reality_classification=coaching_data.get('reality', {}).get('classification', ''),
        options_strategies=coaching_data.get('options', {}).get('strategies', ''),
        options_selected=coaching_data.get('options', {}).get('selected', ''),
        options_plans=coaching_data.get('options', {}).get('plans', ''),
        options_qa=coaching_data.get('options', {}).get('qa', ''),
        report_data_summary=coaching_data.get('report', {}).get('data_summary', ''),
        report_cause_summary=coaching_data.get('report', {}).get('cause_summary', ''),
        report_plan_summary=coaching_data.get('report', {}).get('plan_summary', ''),
        report_commitment=coaching_data.get('report', {}).get('commitment', ''),
        scripture_opening=coaching_data.get('scripture', {}).get('opening', ''),
        scripture_cause=coaching_data.get('scripture', {}).get('cause', ''),
        scripture_plan=coaching_data.get('scripture', {}).get('plan', ''),
        scripture_ending=coaching_data.get('scripture', {}).get('ending', ''),
        action_plan=coaching_data.get('action_plan', ''),
        checklist=coaching_data.get('checklist', '')
    )
    
    return report


def save_report(report: str, output_path: str) -> None:
    """保存汇报文档到指定路径"""
    Path(output_path).write_text(report, encoding='utf-8')
    print(f"汇报文档已保存到：{output_path}")


# 示例使用
if __name__ == "__main__":
    # 示例数据
    sample_data = {
        "title": "销售业绩下滑汇报方案",
        "goal": {
            "primary": "让领导了解真实情况，争取理解和支持",
            "ideal": "领导理解并协助提供改进建议",
            "baseline": "重新分析并复盘"
        },
        "reality": {
            "data": "销售同比下滑30%，从3月开始，整体下滑",
            "root_cause": "交接机制缺失 + 情报收集机制缺失",
            "classification": "| 外部 | 市场环境轻微下滑 | ❌ |\n| 内部 | 交接机制缺失 | ✅ |"
        },
        "options": {
            "strategies": "| 聚焦机制型 | 重点讲机制缺失，弱化人的问题 | 建设性强，不甩锅 | 可能被追问 |",
            "selected": "聚焦机制型",
            "plans": "| 短期 | 建立交接验收清单 |\n| 中期 | 打通监管单位渠道 |",
            "qa": "| 为什么之前没机制？ | 之前人员稳定，问题不突出 |"
        },
        "report": {
            "data_summary": "销售同比下滑30%，从3月开始",
            "cause_summary": "交接机制缺失、情报机制缺失",
            "plan_summary": "建立交接清单、打通监管渠道",
            "commitment": "每两周汇报进展"
        },
        "scripture": {
            "opening": "\"领导，我来汇报一下近期销售情况。数据确实不太理想，但我已经做了分析...\"",
            "cause": "\"外部有一定影响，但核心问题在我们内部...\"",
            "plan": "\"针对这两个问题，我建议...\"",
            "ending": "\"后续我每两周向您汇报进展。\""
        },
        "action_plan": "| 建立交接清单 | 起草模板，对齐试运行 | 本周 | 我 | 商务侧配合 |",
        "checklist": "| 数据准确 | ☐ |\n| 根因清晰 | ☐ |\n| 方案具体 | ☐ |"
    }
    
    report = generate_report(sample_data)
    print(report)
