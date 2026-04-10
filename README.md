# Daily-AI4PDE

> AI4PDE (AI for Partial Differential Equations) 每日文献追踪系统 | Daily Paper Tracking System
>
> 严格筛选：所有论文均为"**用神经网络求解偏微分方程（PDE）**"相关研究

[中文](#中文) | [English](#english)

---

## 中文

### 简介

Daily-AI4PDE 是一个自动化的 AI4PDE 领域每日文献追踪系统，覆盖四大研究方向。每个分类都有独立仓库和 **双语 GitHub Pages 页面**（支持中英文一键切换）。

所有论文经过**双重 PDE 相关性过滤**（arXiv 查询词限定 + 摘要关键词二次筛查），确保返回的文献严格与"用神经网络求解 PDE"相关。

> KAN (Kolmogorov-Arnold Networks) 已合并至 PINN 分类中。

### 分类仓库

| 分类 | GitHub 仓库 | 📄 Pages (双语) | 说明 |
|:-----|:-----------|:----------------|:-----|
| **PINN / KAN** | [Daily-PINN](https://github.com/xgxgnpu/Daily-PINN) | [在线浏览](https://xgxgnpu.github.io/Daily-PINN/) | PINN、KAN 等求解 PDE |
| **ELM / 随机特征** | [Daily-ELM](https://github.com/xgxgnpu/Daily-ELM) | [在线浏览](https://xgxgnpu.github.io/Daily-ELM/) | 极限学习机 / 随机特征网络求解 PDE |
| **数据驱动神经算子** | [Daily-DataDriven-NeuralOperator](https://github.com/xgxgnpu/Daily-DataDriven-NeuralOperator) | [在线浏览](https://xgxgnpu.github.io/Daily-DataDriven-NeuralOperator/) | DeepONet, FNO 等求解 PDE |
| **物理信息神经算子** | [Daily-PhysicsInformed-NeuralOperator](https://github.com/xgxgnpu/Daily-PhysicsInformed-NeuralOperator) | [在线浏览](https://xgxgnpu.github.io/Daily-PhysicsInformed-NeuralOperator/) | PI-DeepONet, PINO 等求解 PDE |

### 功能特点

- ✅ 每类每日追踪最新 5 篇 arXiv 论文
- ✅ **双重 PDE 过滤**：arXiv 查询词精化 + 摘要关键词二次筛查
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

# 运行检索（带 PDE 过滤）
python fetch_today.py

# 检索更多论文
python fetch_today.py --max_results 10

# 快速模式（跳过代码搜索）
python fetch_today.py --no_code_search

# 使用 GitHub token 提高搜索配额
python fetch_today.py --token YOUR_GITHUB_TOKEN
```

### PDE 过滤机制

1. **arXiv 查询词限定**：每个类别的查询词采用 `(方法关键词) AND (PDE关键词)` 的组合查询
2. **摘要二次筛查**：`is_pde_related()` 函数对标题+摘要做关键词匹配，检查是否包含 PDE 相关术语（如 "partial differential equation", "Navier-Stokes", "boundary value" 等 30+ 个关键词）
3. **超额检索+过滤**：初始检索 `max_results * 4` 篇论文，过滤后保留前 `max_results` 篇

---

## English

### Introduction

Daily-AI4PDE is an automated daily paper tracking system for the AI4PDE field, covering four major research directions. Each category has its own repository and **bilingual GitHub Pages** (Chinese/English toggle).

All papers are **strictly filtered for PDE relevance** (refined arXiv queries + abstract keyword secondary screening), ensuring every listed paper is about solving PDEs with neural networks.

> KAN (Kolmogorov-Arnold Networks) has been merged into the PINN category.

### Repositories

| Category | GitHub Repo | 📄 Pages (Bilingual) | Description |
|:---------|:-----------|:---------------------|:------------|
| **PINN / KAN** | [Daily-PINN](https://github.com/xgxgnpu/Daily-PINN) | [Browse](https://xgxgnpu.github.io/Daily-PINN/) | PINN, KAN for solving PDEs |
| **ELM / Random Features** | [Daily-ELM](https://github.com/xgxgnpu/Daily-ELM) | [Browse](https://xgxgnpu.github.io/Daily-ELM/) | ELM / Random Feature Networks for PDEs |
| **Data-Driven Neural Operator** | [Daily-DataDriven-NeuralOperator](https://github.com/xgxgnpu/Daily-DataDriven-NeuralOperator) | [Browse](https://xgxgnpu.github.io/Daily-DataDriven-NeuralOperator/) | DeepONet, FNO, etc. for PDEs |
| **Physics-Informed Neural Operator** | [Daily-PhysicsInformed-NeuralOperator](https://github.com/xgxgnpu/Daily-PhysicsInformed-NeuralOperator) | [Browse](https://xgxgnpu.github.io/Daily-PhysicsInformed-NeuralOperator/) | PI-DeepONet, PINO, etc. for PDEs |

### Features

- ✅ Daily tracking of latest 5 arXiv papers per category
- ✅ **Dual PDE filtering**: refined arXiv queries + abstract keyword secondary screening
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

# Run paper fetch (with PDE filter)
python fetch_today.py

# Fetch more papers
python fetch_today.py --max_results 10

# Fast mode (skip GitHub code search)
python fetch_today.py --no_code_search

# Use GitHub token for higher API quota
python fetch_today.py --token YOUR_GITHUB_TOKEN
```

### PDE Filtering Mechanism

1. **Refined arXiv queries**: Each category uses `(method keywords) AND (PDE keywords)` combination queries
2. **Abstract secondary screening**: `is_pde_related()` function checks title + abstract for PDE-related terms (30+ keywords like "partial differential equation", "Navier-Stokes", "boundary value", etc.)
3. **Over-fetch + filter**: Initially fetches `max_results * 4` papers, then filters down to top `max_results` PDE-relevant ones

---

*Last updated: 2026-04-10*
