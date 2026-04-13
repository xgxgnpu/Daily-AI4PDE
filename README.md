# Daily-AI4PDE

> **AI4PDE — 用神经网络求解偏微分方程 (PDE) 每日文献追踪系统**
>
> **Daily Paper Tracking System for Neural Network-based PDE Solvers**
>
> 严格筛选：所有论文均为"**用神经网络求解偏微分方程（PDE）**"相关研究，涵盖正问题与反问题

[中文](#中文) | [English](#english)

## 作者 / Author

**熊雄 (Xiong Xiong)**

- 西北工业大学 / Northwestern Polytechnical University (NWPU)
- 研究方向 / Research: AI4PDE, Physics-Informed Deep Learning, Data-Driven Discovery
- Email: xiongxiongnwpu@mail.nwpu.edu.cn
- [Google Scholar](https://scholar.google.com/citations?user=j1M9tkwAAAAJ&hl=zh-CN&oi=sra) | [ResearchGate](https://www.researchgate.net/profile/Xiong-Xiong-19?ev=hdr_xprf)
- [Physics-informed-vibe-coding](https://github.com/xgxgnpu/Physics-informed-vibe-coding) — 首个 PINN Vibe Coding 开源仓库，提供完整 JAX-GPU 实现及中文学术教程

---

## 中文

### 项目简介

**Daily-AI4PDE** 是一个全自动的 AI for PDE 领域每日文献追踪系统。该项目聚焦于**用神经网络（深度学习）求解偏微分方程**这一前沿交叉方向，覆盖以下四大主流技术路线：

```
神经网络求解 PDE 方法体系
├── PINN / KAN — 物理信息神经网络 / Kolmogorov-Arnold 网络
│   ├── 损失函数中嵌入 PDE 残差（无需标注数据）
│   ├── 适用于正/反问题、参数辨识、数据同化
│   └── 代表方法: PINN, cPINN, hp-VPINN, KAN-PINN, J-PIKAN
│
├── ELM / 随机特征网络 — 极限学习机
│   ├── 单隐层网络 + 随机固定权重 + 最小二乘求解
│   ├── 训练速度极快（无需反向传播）
│   └── 代表方法: PIELM, RPNN, Random Feature Method
│
├── 数据驱动神经算子 — DeepONet, FNO 等
│   ├── 学习算子映射（函数→函数），具有泛化能力
│   ├── 训练后可实时推理新参数/新边界条件
│   └── 代表方法: DeepONet, FNO, CNO, GNO, U-NO
│
└── 物理信息神经算子 — PI-DeepONet, PINO 等
    ├── 融合物理约束的算子学习（减少数据需求）
    ├── 兼具泛化性与物理一致性
    └── 代表方法: PI-DeepONet, PINO, PIFNO
```

### 涵盖的典型 PDE 问题

本系统追踪的论文涉及以下常见偏微分方程及其变体：

| 方程类型 | 典型方程 | 应用领域 |
|:---------|:---------|:---------|
| **椭圆型** | Poisson, Laplace, Helmholtz | 静电场、稳态传热、声学 |
| **抛物型** | 热方程, Allen-Cahn, Cahn-Hilliard | 扩散过程、相场模型 |
| **双曲型** | 波动方程, Burgers, Euler | 声波传播、激波、气体动力学 |
| **不可压 NS** | Navier-Stokes (incompressible) | 流体力学、CFD |
| **可压缩流** | Euler, compressible NS | 航空航天、高速流动 |
| **对流扩散** | Convection-Diffusion, Advection | 污染物传输、化学反应 |
| **量子力学** | Schrödinger | 量子系统演化 |
| **守恒律** | Conservation Laws | 交通流、浅水波 |

### 分类仓库

每个分类都有独立仓库和 **双语 GitHub Pages 页面**（支持中英文一键切换）：

| 分类 | GitHub 仓库 | 📄 Pages (双语) | 核心方法 | 说明 |
|:-----|:-----------|:----------------|:---------|:-----|
| **PINN / KAN** | [Daily-PINN](https://github.com/xgxgnpu/Daily-PINN) | [在线浏览](https://xgxgnpu.github.io/Daily-PINN/) | PINN, cPINN, KAN | 物理信息神经网络 + Kolmogorov-Arnold 网络求解 PDE |
| **ELM / 随机特征** | [Daily-ELM](https://github.com/xgxgnpu/Daily-ELM) | [在线浏览](https://xgxgnpu.github.io/Daily-ELM/) | PIELM, RPNN | 极限学习机 / 随机特征网络求解 PDE |
| **数据驱动神经算子** | [Daily-DataDriven-NeuralOperator](https://github.com/xgxgnpu/Daily-DataDriven-NeuralOperator) | [在线浏览](https://xgxgnpu.github.io/Daily-DataDriven-NeuralOperator/) | DeepONet, FNO | 数据驱动的算子学习求解 PDE |
| **物理信息神经算子** | [Daily-PhysicsInformed-NeuralOperator](https://github.com/xgxgnpu/Daily-PhysicsInformed-NeuralOperator) | [在线浏览](https://xgxgnpu.github.io/Daily-PhysicsInformed-NeuralOperator/) | PI-DeepONet, PINO | 融合物理约束的算子学习求解 PDE |

### 功能特点

- ✅ **四大方向全覆盖**：PINN/KAN、ELM/随机特征、数据驱动神经算子、物理信息神经算子
- ✅ **双重 PDE 过滤**：arXiv 查询词精化（方法关键词 AND PDE关键词）+ 摘要 30+ 关键词二次筛查
- ✅ **跨仓库去重**：保证4个分类之间无重复论文
- ✅ **自动关键词提取** + GitHub 代码仓库搜索
- ✅ **中英文双语 GitHub Pages**（点击 Tab 一键切换语言）
- ✅ **Markdown 表格**（日期排序）+ 详细摘要，便于快速浏览
- ✅ 基于 arXiv API + GitHub API 全自动检索与推送

### 每篇论文包含的信息

| 字段 | 说明 |
|:-----|:-----|
| 发表日期 | arXiv 最新更新日期 |
| 标题 | 论文完整标题 |
| 作者 | 第一作者 et al. |
| 关键词 | 自动提取的方法/问题关键词（最多5个）|
| 论文链接 | arXiv 摘要页 + PDF 直链 |
| 代码 | 自动搜索的 GitHub 代码仓库（有/无）|
| 摘要 | 论文完整摘要 |

### 使用方法

每个子仓库都包含 `fetch_today.py` 脚本，可独立运行：

```bash
pip install arxiv requests

# 进入任意子仓库
cd Daily-PINN

# 运行检索（带 PDE 过滤），默认每类 5 篇
python fetch_today.py

# 检索更多论文
python fetch_today.py --max_results 10

# 快速模式（跳过 GitHub 代码搜索，加速检索）
python fetch_today.py --no_code_search

# 使用 GitHub token 提高搜索配额
python fetch_today.py --token YOUR_GITHUB_TOKEN
```

### PDE 过滤机制

为确保论文严格相关，系统采用**三层防线**：

1. **arXiv 查询词限定**：每个类别使用 `(方法关键词) AND (PDE关键词)` 组合查询，从源头过滤
2. **摘要关键词二次筛查**：`is_pde_related()` 函数检测标题+摘要中是否包含 PDE 相关术语（"partial differential equation", "Navier-Stokes", "boundary value", "Helmholtz", "conservation law" 等 30+ 个关键词）
3. **超额检索+过滤**：初始检索 `max_results × 4` 篇候选论文，经 PDE 过滤后保留前 `max_results` 篇

### 相关项目

| 项目 | 说明 |
|:-----|:-----|
| [Physics-informed-vibe-coding](https://github.com/xgxgnpu/Physics-informed-vibe-coding) | 首个 PINN Vibe Coding 开源仓库，包含 NTK-PINN, MultiScale-PINN, VS-PINN, GW-PINN, Scale-PINN 等完整 JAX-GPU 实现 |

---

## English

### Introduction

**Daily-AI4PDE** is a fully automated daily paper tracking system for the AI4PDE (AI for Partial Differential Equations) field. The project focuses on **solving PDEs with neural networks (deep learning)** — a rapidly growing interdisciplinary research direction — covering four major technical approaches:

```
Neural Network Methods for Solving PDEs
├── PINN / KAN — Physics-Informed Neural Networks / Kolmogorov-Arnold Networks
│   ├── Embed PDE residuals in loss function (no labeled data needed)
│   ├── Applicable to forward/inverse problems, parameter identification
│   └── Key methods: PINN, cPINN, hp-VPINN, KAN-PINN, J-PIKAN
│
├── ELM / Random Features — Extreme Learning Machines
│   ├── Single hidden layer + random fixed weights + least squares
│   ├── Extremely fast training (no backpropagation)
│   └── Key methods: PIELM, RPNN, Random Feature Method
│
├── Data-Driven Neural Operators — DeepONet, FNO, etc.
│   ├── Learn operator mappings (function → function) with generalization
│   ├── Real-time inference for new parameters/boundary conditions
│   └── Key methods: DeepONet, FNO, CNO, GNO, U-NO
│
└── Physics-Informed Neural Operators — PI-DeepONet, PINO, etc.
    ├── Operator learning with physics constraints (reduced data needs)
    ├── Combines generalizability with physical consistency
    └── Key methods: PI-DeepONet, PINO, PIFNO
```

### Typical PDE Problems Covered

Papers tracked by this system cover the following common PDEs and their variants:

| PDE Type | Typical Equations | Application Domains |
|:---------|:-----------------|:-------------------|
| **Elliptic** | Poisson, Laplace, Helmholtz | Electrostatics, steady-state heat, acoustics |
| **Parabolic** | Heat equation, Allen-Cahn, Cahn-Hilliard | Diffusion, phase-field models |
| **Hyperbolic** | Wave equation, Burgers, Euler | Wave propagation, shock waves, gas dynamics |
| **Incompressible NS** | Navier-Stokes (incompressible) | Fluid mechanics, CFD |
| **Compressible Flow** | Euler, compressible NS | Aerospace, high-speed flows |
| **Convection-Diffusion** | Convection-Diffusion, Advection | Pollutant transport, chemical reactions |
| **Quantum Mechanics** | Schrödinger | Quantum system evolution |
| **Conservation Laws** | Conservation Laws | Traffic flow, shallow water waves |

### Repositories

Each category has its own repository and **bilingual GitHub Pages** (Chinese/English toggle):

| Category | GitHub Repo | 📄 Pages (Bilingual) | Key Methods | Description |
|:---------|:-----------|:---------------------|:------------|:------------|
| **PINN / KAN** | [Daily-PINN](https://github.com/xgxgnpu/Daily-PINN) | [Browse](https://xgxgnpu.github.io/Daily-PINN/) | PINN, cPINN, KAN | Physics-Informed Neural Networks + KAN for PDEs |
| **ELM / Random Features** | [Daily-ELM](https://github.com/xgxgnpu/Daily-ELM) | [Browse](https://xgxgnpu.github.io/Daily-ELM/) | PIELM, RPNN | Extreme Learning Machines / Random Features for PDEs |
| **Data-Driven Neural Operator** | [Daily-DataDriven-NeuralOperator](https://github.com/xgxgnpu/Daily-DataDriven-NeuralOperator) | [Browse](https://xgxgnpu.github.io/Daily-DataDriven-NeuralOperator/) | DeepONet, FNO | Data-driven operator learning for PDEs |
| **PINN Optimizers** | [Daily-Optimizer4PINN](https://github.com/xgxgnpu/Daily-Optimizer4PINN) | [Browse](https://xgxgnpu.github.io/Daily-Optimizer4PINN/) | Adam, L-BFGS | PINN Optimizers & 2nd-order DL optimization |
| **Singular PDEs** | [Daily-SingularPDE](https://github.com/xgxgnpu/Daily-SingularPDE) | [Browse](https://xgxgnpu.github.io/Daily-SingularPDE/) | PINN, PIELM, PIKAN | Singular PDEs (corner/interface/BL) |
| **High-Dim PDEs** | [Daily-HighDimPDE](https://github.com/xgxgnpu/Daily-HighDimPDE) | [Browse](https://xgxgnpu.github.io/Daily-HighDimPDE/) | Deep BSDE, Deep Ritz | Neural networks for high-dimensional PDEs |
| **Physics-Informed Neural Operator** | [Daily-PhysicsInformed-NeuralOperator](https://github.com/xgxgnpu/Daily-PhysicsInformed-NeuralOperator) | [Browse](https://xgxgnpu.github.io/Daily-PhysicsInformed-NeuralOperator/) | PI-DeepONet, PINO | Physics-constrained operator learning for PDEs |

### Features

- ✅ **Four major directions covered**: PINN/KAN, ELM/Random Features, Data-Driven Neural Operators, Physics-Informed Neural Operators
- ✅ **Dual PDE filtering**: refined arXiv queries (method AND PDE keywords) + abstract screening with 30+ PDE-related terms
- ✅ **Cross-repo deduplication**: no duplicate papers across 4 categories
- ✅ **Auto keyword extraction** + GitHub code repository search
- ✅ **Bilingual GitHub Pages** (click tabs to switch Chinese/English)
- ✅ **Markdown tables** (date-sorted) + detailed abstracts for quick browsing
- ✅ Fully automated via arXiv API + GitHub API

### Information per Paper

| Field | Description |
|:------|:------------|
| Date | arXiv latest update date |
| Title | Full paper title |
| Authors | First author et al. |
| Keywords | Auto-extracted method/problem keywords (up to 5) |
| Paper Link | arXiv abstract page + PDF direct link |
| Code | Auto-searched GitHub repository (if available) |
| Abstract | Full paper abstract |

### Usage

Each sub-repository contains a `fetch_today.py` script that can be run independently:

```bash
pip install arxiv requests

# Enter any sub-repository
cd Daily-PINN

# Run paper fetch (with PDE filter), default 5 per category
python fetch_today.py

# Fetch more papers
python fetch_today.py --max_results 10

# Fast mode (skip GitHub code search for faster retrieval)
python fetch_today.py --no_code_search

# Use GitHub token for higher API quota
python fetch_today.py --token YOUR_GITHUB_TOKEN
```

### PDE Filtering Mechanism

To ensure strict relevance, the system employs a **three-layer defense**:

1. **Refined arXiv queries**: Each category uses `(method keywords) AND (PDE keywords)` combination queries to filter at the source
2. **Abstract keyword screening**: `is_pde_related()` function checks title + abstract for 30+ PDE-related terms ("partial differential equation", "Navier-Stokes", "boundary value", "Helmholtz", "conservation law", etc.)
3. **Over-fetch + filter**: Initially fetches `max_results × 4` candidate papers, then filters down to the top `max_results` PDE-relevant ones

### Related Projects

| Project | Description |
|:--------|:------------|
| [Physics-informed-vibe-coding](https://github.com/xgxgnpu/Physics-informed-vibe-coding) | The first open-source PINN Vibe Coding repository with complete JAX-GPU implementations (NTK-PINN, MultiScale-PINN, VS-PINN, GW-PINN, Scale-PINN) and Chinese tutorials |

---

*Last updated: 2026-04-10*
