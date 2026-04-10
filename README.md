# Daily-AI4PDE

> AI4PDE (AI for Partial Differential Equations) 每日文献追踪系统 | Daily Paper Tracking System

[中文](#中文) | [English](#english)

---

## 中文

### 简介

Daily-AI4PDE 是一个自动化的 AI4PDE 领域每日文献追踪系统，覆盖五大研究方向。每个分类都有独立仓库和 **双语 GitHub Pages 页面**（支持中英文一键切换）。

### 分类仓库

| 分类 | GitHub 仓库 | 📄 Pages (双语) | 说明 |
|:-----|:-----------|:----------------|:-----|
| **PINN** | [Daily-PINN](https://github.com/xgxgnpu/Daily-PINN) | [在线浏览](https://xgxgnpu.github.io/Daily-PINN/) | 物理信息神经网络 |
| **ELM** | [Daily-ELM](https://github.com/xgxgnpu/Daily-ELM) | [在线浏览](https://xgxgnpu.github.io/Daily-ELM/) | 极限学习机 / 随机特征网络 |
| **KAN** | [Daily-KAN](https://github.com/xgxgnpu/Daily-KAN) | [在线浏览](https://xgxgnpu.github.io/Daily-KAN/) | Kolmogorov-Arnold 网络 |
| **数据驱动神经算子** | [Daily-DataDriven-NeuralOperator](https://github.com/xgxgnpu/Daily-DataDriven-NeuralOperator) | [在线浏览](https://xgxgnpu.github.io/Daily-DataDriven-NeuralOperator/) | DeepONet, FNO 等 |
| **物理信息神经算子** | [Daily-PhysicsInformed-NeuralOperator](https://github.com/xgxgnpu/Daily-PhysicsInformed-NeuralOperator) | [在线浏览](https://xgxgnpu.github.io/Daily-PhysicsInformed-NeuralOperator/) | PI-DeepONet, PINO 等 |

### 功能特点

- ✅ 每类每日追踪最新 5 篇 arXiv 论文
- ✅ 自动提取关键词、搜索 GitHub 代码
- ✅ **中英文双语 GitHub Pages**（点击 Tab 切换语言）
- ✅ Markdown 表格 + 详细摘要输出
- ✅ GitHub API 自动推送

### 使用方法

每个子仓库都包含 `fetch_today.py` 脚本：

```bash
pip install arxiv requests

# 进入任意子仓库
cd Daily-PINN

# 运行检索
python fetch_today.py

# 检索更多论文
python fetch_today.py --max_results 10

# 使用 GitHub token 提高搜索配额
python fetch_today.py --token YOUR_GITHUB_TOKEN
```

---

## English

### Introduction

Daily-AI4PDE is an automated daily paper tracking system for the AI4PDE field, covering five major research directions. Each category has its own repository and **bilingual GitHub Pages** (Chinese/English toggle).

### Repositories

| Category | GitHub Repo | 📄 Pages (Bilingual) | Description |
|:---------|:-----------|:---------------------|:------------|
| **PINN** | [Daily-PINN](https://github.com/xgxgnpu/Daily-PINN) | [Browse](https://xgxgnpu.github.io/Daily-PINN/) | Physics-Informed Neural Networks |
| **ELM** | [Daily-ELM](https://github.com/xgxgnpu/Daily-ELM) | [Browse](https://xgxgnpu.github.io/Daily-ELM/) | Extreme Learning Machine / Random Features |
| **KAN** | [Daily-KAN](https://github.com/xgxgnpu/Daily-KAN) | [Browse](https://xgxgnpu.github.io/Daily-KAN/) | Kolmogorov-Arnold Networks |
| **Data-Driven Neural Operator** | [Daily-DataDriven-NeuralOperator](https://github.com/xgxgnpu/Daily-DataDriven-NeuralOperator) | [Browse](https://xgxgnpu.github.io/Daily-DataDriven-NeuralOperator/) | DeepONet, FNO, etc. |
| **Physics-Informed Neural Operator** | [Daily-PhysicsInformed-NeuralOperator](https://github.com/xgxgnpu/Daily-PhysicsInformed-NeuralOperator) | [Browse](https://xgxgnpu.github.io/Daily-PhysicsInformed-NeuralOperator/) | PI-DeepONet, PINO, etc. |

### Features

- ✅ Daily tracking of latest 5 arXiv papers per category
- ✅ Auto keyword extraction and GitHub code search
- ✅ **Bilingual GitHub Pages** (click tabs to switch Chinese/English)
- ✅ Markdown table + detailed abstract output
- ✅ Automated GitHub API push

### Usage

Each sub-repository contains a `fetch_today.py` script:

```bash
pip install arxiv requests

# Enter any sub-repository
cd Daily-PINN

# Run paper fetch
python fetch_today.py

# Fetch more papers
python fetch_today.py --max_results 10

# Use GitHub token for higher API quota
python fetch_today.py --token YOUR_GITHUB_TOKEN
```

---

*Last updated: 2026-04-10*
