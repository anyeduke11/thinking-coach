# 🧠 GROW教练式思维模型引导器

<p align="right">
  <b>🌐 语言 / Language:</b>
  <a href="./README.md"><b>🇨🇳 中文</b></a> | 
  <a href="./README_EN.md">🇺🇸 English</a>
</p>

[![Version](https://img.shields.io/badge/version-v1.6-blue.svg)](https://github.com/anyeduke11/thinking-coach/releases/tag/v1.6)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Models](https://img.shields.io/badge/models-94-orange.svg)](#核心功能)
[![Scenarios](https://img.shields.io/badge/scenarios-9-purple.svg)](#核心功能)
[![Bilingual](https://img.shields.io/badge/lang-CN%20%2F%20EN-red.svg)](#双语支持)

> 一个通过结构化对话帮助你练习思维模型、解决实际问题的 AI Skill。

当你面临汇报、决策、问题分析等场景时，它会使用 **GROW 模型**（Goal-Reality-Options-Will）配合 **根因分析**、**二阶思维** 等工具，一个阶段一个阶段引导你完成思考，最终产出可执行的方案。

**🌐 双语支持**：支持中文和英文，自动检测用户语言并切换。

---

## 📋 目录

- [核心功能](#核心功能)
- [双语支持](#双语支持)
- [快速开始](#快速开始)
- [使用示例](#使用示例)
- [模型组合推荐](#模型组合推荐)
- [可视化学习报告](#可视化学习报告)
- [文件结构](#文件结构)
- [版本历史](#版本历史)
- [安装使用](#安装使用)

---

## ✨ 核心功能

### 📚 94个精选思维模型

从 363 个思维模型中精选 94 个最实用的模型，覆盖 9 大策略场景：

| 场景 | 模型数 | 核心能力 | 示例模型 |
|-----|-------|---------|---------|
| S01 认知校准 | 12 | 识别思维盲区 | 确认偏误、锚定效应、可得性偏差 |
| S02 学习提升 | 10 | 高效掌握新技能 | 费曼学习法、刻意练习、帕累托法则 |
| S03 问题解决 | 10 | 突破复杂难题 | 根因分析、第一性原理、逆向思维 |
| S04 系统洞察 | 10 | 看清全局规律 | 飞轮效应、二阶思维、反馈回路 |
| S05 数据判断 | 10 | 理性分析决策 | 相关性≠因果性、基础比率、贝叶斯定理 |
| S06 决策分析 | 12 | 权衡利弊选择 | 决策矩阵、机会成本、期望价值 |
| S07 冲突应对 | 10 | 处理矛盾谈判 | 博弈论、BATNA、原则性谈判 |
| S08 潜能释放 | 10 | 团队沟通管理 | 皮格马利翁效应、马斯洛需求层次、社会认同 |
| S09 市场策略 | 10 | 竞争差异优势 | 护城河、网络效应、转换成本 |

### 🎯 场景化智能推荐

根据你的问题自动识别场景，推荐最合适的思维模型：

```
用户：我要跟领导汇报项目延期，怎么组织语言？
     ↓
Skill：检测到【S08潜能释放 + S01认知校准】场景
     → 推荐「框架效应」「沉没成本谬误」
     → 启动 GROW 教练式引导
```

### 🔗 模型组合推荐

12个经典模型组合，用于复杂问题的多模型协同分析：

| 组合 | 模型 | 适用场景 |
|-----|------|---------|
| C01 深度诊断 | 根因分析+飞轮效应+确认偏误 | 复杂问题分析 |
| C02 理性决策 | 决策矩阵+沉没成本+第一性原理 | 重大选择 |
| C03 数据判断 | 相关性≠因果+可得性偏差+基础比率 | 信息验证 |
| C04 冲突化解 | 博弈论+框架效应+互惠 | 谈判/矛盾 |
| C05 快速学习 | 费曼学习法+帕累托法则+刻意练习 | 技能突破 |
| C06 系统思考 | 飞轮+惯性+二阶思维+逆向思维 | 全局洞察 |
| C07 创新突破 | 第一性原理+横向思维+重新定义 | 新方案 |
| C08 风险评估 | 二阶思维+黑天鹅+情景分析 | 行动预判 |
| C09 团队激励 | 皮格马利翁+马斯洛+社会认同 | 管理场景 |
| C10 竞争优势 | 护城河+网络效应+转换成本 | 商业策略 |
| C11 汇报说服 | 框架效应+沉没成本+成本收益 | 向上沟通 |
| C12 自我突破 | 成长型思维+冒名顶替+刻意练习 | 个人成长 |

### 📊 学习追踪系统

- 每次对话自动记录使用的模型和场景
- 生成思维成长报告（Markdown + 可视化图表）
- 6级掌握度追踪（未接触 → 入门 → 练习 → 熟练 → 精通 → 专家）

---

## 🌐 双语支持

### 自动语言检测

Skill 自动检测用户首次输入的语言（中文/英文），整个对话使用该语言进行。

### 手动语言切换

| 命令 | 功能 |
|-----|------|
| `/lang cn` 或 `/lang 中文` | 切换到中文模式 |
| `/lang en` 或 `/lang English` | Switch to English mode |

### 英文模式示例

```
User: I need to report a project delay to leadership. How should I frame it?

Skill: 📊 Detected scenario: [S08 Potential Release + S01 Cognitive Calibration]
      Recommended model: Framing Effect
      
      ━━━ GROW Coaching Session ━━━
      
      [G Phase - Goal]
      What is the primary outcome you want from this report?
      A. Leadership understands the delay without blame
      B. Leadership approves your recovery plan
      C. Leadership provides additional resources
      
      Which outcome matters most to you?

User: B, I want them to approve my recovery plan

Skill: [R Phase] Let's use the "Framing Effect" to restructure your message:
      
      ❌ Negative frame: "The project is delayed, I'm sorry"
      ✅ Positive frame: "We've identified key issues and developed a solution plan"
      
      Which frame do you think leadership would be more receptive to?
```

---

## 🚀 快速开始

### 方式一：直接提问

直接描述你的问题，Skill 会自动识别场景并开始引导：

```
用户：拿到两个offer，薪资差30%，怎么选？
```

### 方式二：指定场景

```
用户：帮我用决策矩阵分析一下要不要跳槽
```

### 方式三：查看学习报告

```
用户：/review
```

---

## 💡 使用示例

### 示例1：汇报坏消息

```
用户：项目延期了，要跟领导汇报，怎么说？

Skill：这个问题涉及【向上沟通】，我推荐用「框架效应」模型来组织语言。

      【G阶段】你希望领导听完汇报后：
      A. 理解延期原因，不追究责任
      B. 同意你的补救方案
      C. 给予额外资源支持
      
      你最希望达成哪个目标？
      
用户：B，希望他同意我的补救方案

Skill：【R阶段】让我们用「框架效应」重新框架这个问题：
      
      ❌ 负面框架："项目延期了，很抱歉"
      ✅ 正面框架："发现了几个关键问题，已经制定了解决方案"
      
      你觉得哪种框架更容易让领导接受你的方案？
      
用户：正面框架更好

Skill：【O阶段】现在让我们构建汇报内容：
      
      1. 先说解决方案（正面框架）
      2. 再说问题原因（客观陈述）
      3. 最后说预防措施（闭环思维）
      
      你能试着按这个结构说一下吗？
      
用户：[用户练习...]

Skill：【W阶段】很好！你的汇报结构已经成型。
      
      下一步行动：
      1. 准备数据支撑你的方案
      2. 预演领导可能的提问
      3. 确定汇报时间
      
      需要我帮你完善哪个部分？
```

### 示例2：复杂决策分析

```
用户：拿到两个offer，薪资差30%，怎么选？

Skill：📊 检测到复杂决策问题，推荐使用【理性决策组合】
      
      这个问题涉及多个维度，我建议用3个模型串联分析：
      
      | 步骤 | 模型 | 作用 |
      |-----|------|------|
      | 1️⃣ | 沉没成本谬误 | 检查是否受过往投入影响 |
      | 2️⃣ | 第一性原理 | 剥离所有假设，回到问题本质 |
      | 3️⃣ | 决策矩阵 | 量化打分，得出推荐 |
      
      准备好了吗？
```

---

## 📈 可视化学习报告

生成可视化学习报告，3张图表直观展示学习状态：

| 图表 | 功能 | 命令 |
|-----|------|------|
| 9大场景雷达图 | 一眼看清各场景掌握度百分比 | `/review --radar` |
| 学习成长曲线 | 时间轴展示进步趋势 | `/review --curve` |
| 薄弱场景热力图 | 5维度评估矩阵 | `/review --heatmap` |

```bash
# 生成全部图表
python scripts/generate-visual-report.py --data user_profile.json --output ./reports/

# 使用示例数据演示
python scripts/generate-visual-report.py --demo
```

---

## 📁 文件结构

```
thinking-coach/
├── SKILL.md                              # 核心配置文件（含双语切换逻辑）
├── README.md                             # 本文档（中文版）
├── README_EN.md                          # 英文版文档
├── requirements.txt                      # Python 依赖
│
├── references/                           # 参考文档（中文）
│   ├── thinking-models-library.md        # 94个思维模型库
│   ├── strategy-library.md               # 9大策略场景库
│   ├── model-combinations.md             # 12个模型组合库
│   ├── learning-tracking.md              # 学习追踪机制
│   ├── grow-model-guide.md               # GROW模型指南
│   ├── root-cause-analysis.md            # 根因分析指南
│   └── ...
│
├── references/en/                        # 参考文档（英文）
│   ├── thinking-models-library.md        # 94 Thinking Models (English)
│   ├── strategy-library.md               # 9 Strategic Scenarios (English)
│   └── model-combinations.md             # 12 Model Combinations (English)
│
├── scripts/                              # 自动化脚本
│   ├── generate-visual-report.py         # 可视化报告生成
│   ├── generate-report.py                # Markdown报告生成
│   ├── export-to-docx.py                 # 导出Word文档
│   └── auto-collect.py                   # 对话数据收集
│
└── assets/                               # 模板文件
    ├── welcome-notification.md           # 用户欢迎提示
    ├── user-profile-template.md          # 用户档案模板
    ├── learning-report-template.md       # 学习报告模板
    └── ...
```

---

## 📜 版本历史

| 版本 | 主要更新 |
|-----|---------|
| **v1.6** | **中英双语支持：自动语言检测、`/lang`切换命令、英文参考文档、英文README** |
| **v1.5** | **模型组合推荐：12个经典组合模板、组合工作流引导、组合效果评估** |
| **v1.4** | **可视化学习报告：9大场景雷达图、学习成长曲线、薄弱场景热力图** |
| **v1.3** | **94个精选思维模型、9大策略场景、学习追踪系统** |
| **v1.2** | **快速/标准双模式、流程控制命令、自动对话收集** |
| **v1.1** | **GROW教练式对话框架、根因分析嵌入** |
| **v1.0** | **基础版本** |

---

## 🔧 安装使用

### 前置要求

- Python 3.8+（用于运行脚本）
- matplotlib、numpy（用于可视化报告）

### 安装依赖

```bash
pip install -r requirements.txt
```

### 在 SOLO 中使用

1. 将 `thinking-coach` 文件夹放入 SOLO 的 skills 目录
2. 重启 SOLO 或刷新技能列表
3. 直接提问即可触发 Skill

### 流程控制命令

| 命令 | 功能 |
|-----|------|
| `/coach` | 启动GROW教练模式（标准模式） |
| `/coach [问题]` | 针对特定问题启动教练模式 |
| `/coach --fast [问题]` | 快速模式（R阶段追问3层） |
| `/skip` | 跳过当前步骤，进入下一阶段 |
| `/back` | 返回上一阶段重新分析 |
| `/fast` | 切换到快速模式 |
| `/detail` | 切换到标准模式 |
| `/status` | 查看当前进度和状态 |
| `/export` | 生成汇报文档 |
| `/review` | 查看学习报告（Markdown） |
| `/review --visual` | 生成可视化图表报告（PNG） |
| `/lang cn` | 切换到中文模式 |
| `/lang en` | Switch to English mode |

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 开发计划

- [ ] 增加更多思维模型（目标：120个）
- [ ] 支持用户自定义模型组合
- [ ] 多语言支持（日文、韩文版）
- [ ] 与 Notion/Obsidian 集成

---

## 📄 许可证

[MIT License](LICENSE)

---

## 🙏 致谢

- 思维模型来源：《思考，快与慢》《穷查理宝典》《原则》等经典著作
- GROW 模型：Sir John Whitmore 的教练技术框架
- SOLO 平台：提供 Skill 运行环境

---

<p align="center">
  <b>开始你的思维训练之旅吧！</b><br>
  <a href="https://github.com/anyeduke11/thinking-coach/releases/tag/v1.6">⬇️ 下载最新版本</a>
</p>
