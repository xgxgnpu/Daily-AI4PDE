# Daily-AI4PDE

每日自动追踪 AI for PDE 领域最新 arXiv 论文，按方法论分为4大方向。

## 分类

| 文件 | 方向 | 关键方法 |
|------|------|---------|
| [PINN_today.md](PINN_today.md) | Physics-Informed Neural Networks | PINN, Physics-Informed Learning |
| [ELM_today.md](ELM_today.md) | ELM / 随机特征 / KAN | Extreme Learning Machine, Random Feature, Kolmogorov-Arnold |
| [DataDriven_NeuralOperator_today.md](DataDriven_NeuralOperator_today.md) | 数据驱动神经算子 | DeepONet, FNO, Neural Operator |
| [PhysicsInformed_NeuralOperator_today.md](PhysicsInformed_NeuralOperator_today.md) | 物理信息神经算子 | PI-DeepONet, PINO, PIFNO |

## 使用

```bash
pip install arxiv requests pyyaml

# 每个分类返回5篇最新论文
python ai4pde_today.py

# 自定义数量
python ai4pde_today.py --max_results 10

# 快速模式（跳过代码搜索）
python ai4pde_today.py --no_code_search
```

## 输出格式

每个分类文件包含：
- 论文汇总表格（发表日期、标题、作者、关键词、论文链接、代码链接）
- 详细摘要部分
