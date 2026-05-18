# 🧠 GROW Coaching Thinking Model Guide

<p align="right">
  <b>🌐 Language / 语言:</b>
  <a href="./README.md">🇨🇳 中文</a> | 
  <a href="./README_EN.md"><b>🇺🇸 English</b></a>
</p>

[![Version](https://img.shields.io/badge/version-v1.6-blue.svg)](https://github.com/anyeduke11/thinking-coach/releases/tag/v1.6)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Models](https://img.shields.io/badge/models-94-orange.svg)](#core-features)
[![Scenarios](https://img.shields.io/badge/scenarios-9-purple.svg)](#core-features)
[![Bilingual](https://img.shields.io/badge/lang-CN%20%2F%20EN-red.svg)](#bilingual-support)

> An AI Skill that helps you practice thinking models and solve real-world problems through structured coaching conversations.

When you face challenges in reporting, decision-making, or problem analysis, it uses the **GROW Model** (Goal-Reality-Options-Will) combined with tools like **Root Cause Analysis** and **Second-Order Thinking** to guide you step-by-step through your thinking process and produce actionable solutions.

**🌐 Bilingual Support**: Supports both Chinese and English with automatic language detection.

---

## 📋 Table of Contents

- [Core Features](#core-features)
- [Bilingual Support](#bilingual-support)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Model Combinations](#model-combinations)
- [Visual Learning Reports](#visual-learning-reports)
- [File Structure](#file-structure)
- [Version History](#version-history)
- [Installation](#installation)

---

## ✨ Core Features

### 📚 94 Curated Thinking Models

94 practical thinking models selected from 363, organized into 9 strategic scenarios:

| Scenario | Models | Core Ability | Example Models |
|----------|--------|-------------|----------------|
| S01 Cognitive Calibration | 12 | Identify thinking biases | Confirmation Bias, Anchoring Effect, Availability Heuristic |
| S02 Learning & Growth | 10 | Accelerate skill acquisition | Feynman Technique, Deliberate Practice, Pareto Principle |
| S03 Problem Solving | 10 | Break through complex problems | Root Cause Analysis, First Principles, Inversion |
| S04 Systems Insight | 10 | Understand complex systems | Flywheel Effect, Second-Order Thinking, Feedback Loops |
| S05 Data & Evidence | 10 | Evaluate data reliability | Correlation ≠ Causation, Base Rate Fallacy, Bayes' Theorem |
| S06 Decision Analysis | 12 | Weigh trade-offs | Decision Matrix, Opportunity Cost, Expected Value |
| S07 Conflict Resolution | 10 | Navigate conflicts | Game Theory, BATNA, Principled Negotiation |
| S08 Potential Release | 10 | Unlock team potential | Pygmalion Effect, Maslow's Hierarchy, Social Proof |
| S09 Market Strategy | 10 | Build competitive advantage | Economic Moat, Network Effects, Blue Ocean Strategy |

### 🎯 Smart Scenario Detection

Automatically identifies the scenario from your problem and recommends the best thinking models:

```
User: I need to report a project delay to leadership. How should I frame it?
  ↓
Skill: Detected [S08 Potential Release + S01 Cognitive Calibration]
     → Recommended: Framing Effect, Sunk Cost Fallacy
     → Starting GROW coaching session...
```

### 🔗 Model Combinations

12 classic model combinations for complex problems that require multi-model analysis:

| Combo | Models | Best For |
|-------|--------|----------|
| C01 Deep Diagnosis | Root Cause + Flywheel + Confirmation Bias | Complex problem analysis |
| C02 Rational Decision | Decision Matrix + Sunk Cost + First Principles | Major choices |
| C03 Data Judgment | Correlation ≠ Causation + Availability + Base Rate | Information verification |
| C04 Conflict Resolution | Game Theory + Framing + Reciprocity | Negotiations |
| C05 Rapid Learning | Feynman + Pareto + Deliberate Practice | Skill breakthrough |
| C06 Systems Thinking | Flywheel + Second-Order + Inversion | Global insight |
| C07 Innovation | First Principles + Lateral Thinking + Redefine | New solutions |
| C08 Risk Assessment | Second-Order + Black Swan + Scenario Analysis | Pre-action evaluation |
| C09 Team Motivation | Pygmalion + Maslow + Social Proof | Management |
| C10 Competitive Edge | Moat + Network Effects + Switching Costs | Business strategy |
| C11 Persuasive Reporting | Framing + Sunk Cost + Cost-Benefit | Upward communication |
| C12 Self-Breakthrough | Growth Mindset + Impostor + Deliberate Practice | Personal growth |

### 📊 Learning Tracking

- Automatically records every coaching session
- Tracks model usage and scenario coverage
- Generates growth reports (Markdown + visual charts)
- 6-level mastery tracking (Unaware → Novice → Practicing → Proficient → Master → Expert)

---

## 🌐 Bilingual Support

### Automatic Language Detection

The Skill automatically detects your language from your first message and switches accordingly.

### Manual Language Switch

| Command | Function |
|---------|----------|
| `/lang cn` | Switch to Chinese mode |
| `/lang en` | Switch to English mode |

### English Mode Example

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

## 🚀 Quick Start

### Method 1: Just Ask

Describe your problem and the Skill will automatically detect the scenario:

```
User: I have two job offers with a 30% salary difference. How do I choose?
```

### Method 2: Specify a Model

```
User: Help me analyze this decision using a Decision Matrix
```

### Method 3: Review Progress

```
User: /review
```

---

## 💡 Usage Examples

### Example 1: Reporting Bad News

```
User: Project is delayed. How do I tell my boss?

Skill: This involves [Upward Communication]. I recommend using the
      "Framing Effect" model.
      
      [G Phase] What outcome do you want?
      [R Phase] Let's reframe: problem → opportunity
      [O Phase] Build your report structure:
        1. Lead with the solution (positive frame)
        2. Explain root causes (objective)
        3. Prevention measures (closed-loop)
      [W Phase] Practice your delivery
```

### Example 2: Complex Decision

```
User: Should I quit my job and start a company?

Skill: 📊 Complex decision detected. Recommending [Rational Decision Combo]
      
      | Step | Model | Purpose |
      |------|-------|---------|
      | 1️⃣ | Sunk Cost Fallacy | Check if past investment is biasing you |
      | 2️⃣ | First Principles | Strip to fundamentals |
      | 3️⃣ | Decision Matrix | Quantify the comparison |
```

---

## 📈 Visual Learning Reports

Generate visual learning reports with 3 chart types:

| Chart | Function | Command |
|-------|----------|---------|
| 9-Scenario Radar Chart | See mastery across all scenarios at a glance | `/review --radar` |
| Growth Curve | Track progress over time | `/review --curve` |
| Weakness Heatmap | 5-dimension assessment matrix | `/review --heatmap` |

```bash
# Generate all charts
python scripts/generate-visual-report.py --data user_profile.json --output ./reports/

# Demo with sample data
python scripts/generate-visual-report.py --demo
```

---

## 📁 File Structure

```
thinking-coach/
├── SKILL.md                              # Core configuration (with bilingual logic)
├── README.md                             # This document (Chinese version)
├── README_EN.md                          # English version
├── requirements.txt                      # Python dependencies
│
├── references/                           # Reference documents (Chinese)
│   ├── thinking-models-library.md        # 94 thinking models
│   ├── strategy-library.md               # 9 strategic scenarios
│   ├── model-combinations.md             # 12 model combinations
│   ├── learning-tracking.md              # Learning tracking system
│   ├── grow-model-guide.md               # GROW model guide
│   ├── root-cause-analysis.md            # Root cause analysis guide
│   └── ...
│
├── references/en/                        # Reference documents (English)
│   ├── thinking-models-library.md        # 94 Thinking Models (English)
│   ├── strategy-library.md               # 9 Strategic Scenarios (English)
│   └── model-combinations.md             # 12 Model Combinations (English)
│
├── scripts/                              # Automation scripts
│   ├── generate-visual-report.py         # Visual report generation
│   ├── generate-report.py                # Markdown report generation
│   ├── export-to-docx.py                 # Word document export
│   └── auto-collect.py                   # Conversation data collection
│
└── assets/                               # Template files
    ├── welcome-notification.md           # Welcome notification
    ├── user-profile-template.md          # User profile template
    ├── learning-report-template.md       # Learning report template
    └── ...
```

---

## 📜 Version History

| Version | Key Updates |
|---------|-------------|
| **v1.6** | **Bilingual CN/EN support, auto language detection, English reference docs** |
| **v1.5** | **Model combinations: 12 classic templates, workflow guidance, effect evaluation** |
| **v1.4** | **Visual learning reports: radar chart, growth curve, weakness heatmap** |
| **v1.3** | **94 curated models, 9 strategic scenarios, learning tracking system** |
| **v1.2** | **Fast/Standard modes, flow control commands, auto data collection** |
| **v1.1** | **GROW coaching framework, root cause analysis embedding** |
| **v1.0** | **Initial release** |

---

## 🔧 Installation

### Prerequisites

- Python 3.8+ (for running scripts)
- matplotlib, numpy (for visual reports)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Use in SOLO

1. Place the `thinking-coach` folder in your SOLO skills directory
2. Restart SOLO or refresh the skill list
3. Just ask a question to trigger the Skill

### Flow Control Commands

| Command | Function |
|---------|----------|
| `/coach` | Start GROW coaching (standard mode) |
| `/coach --fast` | Start in fast mode |
| `/skip` | Skip current step |
| `/back` | Return to previous phase |
| `/fast` | Switch to fast mode |
| `/detail` | Switch to standard mode |
| `/status` | View current progress |
| `/export` | Export conversation to document |
| `/review` | View learning report |
| `/review --visual` | Generate visual chart report |
| `/lang cn` | Switch to Chinese |
| `/lang en` | Switch to English |

---

## 🗺️ Roadmap

- [ ] Expand to 120+ thinking models
- [ ] User-customizable model combinations
- [ ] Integration with Notion/Obsidian
- [ ] Mobile-friendly visual reports
- [ ] Community model library contributions

---

## 🤝 Contributing

Issues and Pull Requests are welcome!

---

## 📄 License

[MIT License](LICENSE)

---

## 🙏 Acknowledgments

- **Thinking Models**: *Thinking, Fast and Slow*, *Poor Charlie's Almanack*, *Principles* by Ray Dalio
- **GROW Model**: Sir John Whitmore's coaching framework
- **SOLO Platform**: Skill runtime environment

---

<p align="center">
  <b>Start your thinking training journey today!</b><br>
  <a href="https://github.com/anyeduke11/thinking-coach/releases/tag/v1.6">⬇️ Download Latest Release</a>
  &nbsp;|&nbsp;
  <a href="https://github.com/anyeduke11/thinking-coach/blob/main/README.md">🇨🇳 中文版</a>
</p>
