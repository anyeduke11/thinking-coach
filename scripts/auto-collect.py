#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动收集对话数据脚本 (v1.2新增)
在GROW对话过程中，自动收集各阶段关键数据，生成结构化会话记录。
"""

import json
from datetime import datetime
from pathlib import Path


class SessionCollector:
    """GROW会话数据自动收集器"""

    def __init__(self, mode: str = "standard", problem_type: str = ""):
        self.session = {
            "session_id": datetime.now().strftime("%Y%m%d%H%M%S"),
            "timestamp": datetime.now().isoformat(),
            "mode": mode,
            "problem_type": problem_type,
            "models_used": ["GROW"],
            "completion": {
                "G": False,
                "R": False,
                "O": False,
                "W": False,
            },
            "key_outputs": {},
            "rounds": 0,
        }

    def collect_goal(self, primary: str, ideal: str, baseline: str):
        """收集G阶段数据"""
        self.session["key_outputs"]["goal"] = {
            "primary": primary,
            "ideal": ideal,
            "baseline": baseline,
        }
        self.session["completion"]["G"] = True
        self._save()

    def collect_reality(self, facts: str, root_cause: str, classification: str):
        """收集R阶段数据"""
        if "根因分析" not in self.session["models_used"]:
            self.session["models_used"].append("根因分析")
        if "5W1H" not in self.session["models_used"]:
            self.session["models_used"].append("5W1H")
        self.session["key_outputs"]["reality"] = {
            "facts": facts,
            "root_cause": root_cause,
            "classification": classification,
        }
        self.session["completion"]["R"] = True
        self._save()

    def collect_options(self, strategy: str, plans: str, qa: str = ""):
        """收集O阶段数据"""
        if "二阶思维" not in self.session["models_used"]:
            self.session["models_used"].append("二阶思维")
        self.session["key_outputs"]["options"] = {
            "strategy": strategy,
            "plans": plans,
            "qa": qa,
        }
        self.session["completion"]["O"] = True
        self._save()

    def collect_will(self, framework: str, scripture: str, action_plan: str):
        """收集W阶段数据"""
        self.session["key_outputs"]["will"] = {
            "framework": framework,
            "scripture": scripture,
            "action_plan": action_plan,
        }
        self.session["completion"]["W"] = True
        self._save()

    def add_round(self):
        """记录对话轮次"""
        self.session["rounds"] += 1

    def mark_complete(self):
        """标记会话完成"""
        self.session["completed_at"] = datetime.now().isoformat()
        self.session["completion"]["overall"] = all(
            self.session["completion"].values()
        )
        self._save()

    def get_session_data(self) -> dict:
        """获取当前会话数据"""
        return self.session

    def get_status(self) -> dict:
        """获取当前进度状态"""
        completed = [k for k, v in self.session["completion"].items() if v]
        total = ["G", "R", "O", "W"]
        remaining = [k for k in total if k not in completed]
        return {
            "current_mode": self.session["mode"],
            "completed_stages": completed,
            "remaining_stages": remaining,
            "total_rounds": self.session["rounds"],
            "models_used": self.session["models_used"],
        }

    def _save(self):
        """保存会话数据到文件"""
        output_dir = Path("/data/user/work/thinking-coach-sessions")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"{self.session['session_id']}.json"
        output_file.write_text(
            json.dumps(self.session, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def export_markdown(self, output_path: str = None) -> str:
        """将会话数据导出为Markdown报告"""
        if output_path is None:
            output_path = f"/workspace/coaching-report-{self.session['session_id']}.md"

        ko = self.session.get("key_outputs", {})

        lines = [
            f"# GROW教练报告",
            f"",
            f"> 生成时间：{self.session['timestamp']}",
            f"> 引导模式：{'快速' if self.session['mode'] == 'fast' else '标准'}",
            f"> 问题类型：{self.session['problem_type']}",
            f"> 使用模型：{'、'.join(self.session['models_used'])}",
            f"> 对话轮次：{self.session['rounds']}轮",
            f"",
            f"---",
            f"",
        ]

        # G阶段
        goal = ko.get("goal", {})
        if goal:
            lines.extend([
                f"## 🟢 G阶段：目标",
                f"",
                f"| 维度 | 内容 |",
                f"|-----|------|",
                f"| 核心目标 | {goal.get('primary', '')} |",
                f"| 理想结果 | {goal.get('ideal', '')} |",
                f"| 底线接受 | {goal.get('baseline', '')} |",
                f"",
                f"---",
                f"",
            ])

        # R阶段
        reality = ko.get("reality", {})
        if reality:
            lines.extend([
                f"## 🟡 R阶段：现状分析",
                f"",
                f"### 事实",
                f"{reality.get('facts', '')}",
                f"",
                f"### 根因",
                f"{reality.get('root_cause', '')}",
                f"",
                f"### 原因归类",
                f"{reality.get('classification', '')}",
                f"",
                f"---",
                f"",
            ])

        # O阶段
        options = ko.get("options", {})
        if options:
            lines.extend([
                f"## 🟠 O阶段：策略选择",
                f"",
                f"### 选择策略",
                f"{options.get('strategy', '')}",
                f"",
                f"### 改进方案",
                f"{options.get('plans', '')}",
                f"",
            ])
            if options.get("qa"):
                lines.extend([
                    f"### 预判问题",
                    f"{options['qa']}",
                    f"",
                ])
            lines.extend([
                f"---",
                f"",
            ])

        # W阶段
        will = ko.get("will", {})
        if will:
            lines.extend([
                f"## 🔵 W阶段：行动方案",
                f"",
                f"### 汇报框架",
                f"{will.get('framework', '')}",
                f"",
                f"### 关键话术",
                f"{will.get('scripture', '')}",
                f"",
                f"### 改进计划",
                f"{will.get('action_plan', '')}",
                f"",
            ])

        content = "\n".join(lines)
        Path(output_path).write_text(content, encoding="utf-8")
        return output_path


# 命令行使用
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("用法：python auto-collect.py [status|export]")
        print("  status  - 查看当前会话状态")
        print("  export  - 导出会话报告")
        sys.exit(0)

    collector = SessionCollector(mode="standard", problem_type="示例")
    print(json.dumps(collector.get_status(), ensure_ascii=False, indent=2))
