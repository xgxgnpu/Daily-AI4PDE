# Daily-AI4PDE

> AI for PDE 每日文献追踪系统 — 自动检索 arXiv 最新论文

## 5个方向子仓库

| 仓库 | 方向 | 关键方法 | 链接 |
|------|------|---------|------|
| **Daily-PINN** | Physics-Informed Neural Networks | PINN, Physics-Informed Learning | [GitHub](https://github.com/xgxgnpu/Daily-PINN) |
| **Daily-ELM** | Extreme Learning Machine / 随机特征 | ELM, PIELM, Random Feature | [GitHub](https://github.com/xgxgnpu/Daily-ELM) |
| **Daily-KAN** | Kolmogorov-Arnold Networks | KAN, Kolmogorov-Arnold | [GitHub](https://github.com/xgxgnpu/Daily-KAN) |
| **Daily-DataDriven-NeuralOperator** | 数据驱动神经算子 | DeepONet, FNO, Neural Operator | [GitHub](https://github.com/xgxgnpu/Daily-DataDriven-NeuralOperator) |
| **Daily-PhysicsInformed-NeuralOperator** | 物理信息神经算子 | PI-DeepONet, PINO, PIFNO | [GitHub](https://github.com/xgxgnpu/Daily-PhysicsInformed-NeuralOperator) |

## 使用方法

每个子仓库都包含独立的 `fetch_today.py` 脚本，可以单独运行：

```bash
pip install arxiv requests

# 进入任意子仓库目录
cd Daily-PINN
python fetch_today.py                          # 默认返回5篇
python fetch_today.py --max_results 10         # 返回10篇
python fetch_today.py --no_code_search         # 跳过代码搜索（加速）
python fetch_today.py --token YOUR_TOKEN       # 使用 GitHub token
```

## 输出格式

每个仓库生成 Markdown 文件，包含：

- **论文汇总表格**: 发表日期、标题、作者、关键词、论文链接、代码链接
- **详细摘要**: 每篇论文的完整摘要

## 数据来源

- 论文: [arXiv](https://arxiv.org/) API
- 代码: [GitHub](https://github.com/) Search API
