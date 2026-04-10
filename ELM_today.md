# ELM / 随机特征网络 / KAN — 每日文献追踪

> 更新日期: 2026.04.10
> 检索关键词: Extreme Learning Machine, PIELM, Random Feature, KAN, Kolmogorov-Arnold
> 共 5 篇论文

## 论文列表

| # | 发表日期 | 标题 | 作者 | 关键词 | 论文链接 | 代码 |
|:---:|:--------:|:-----|:-----|:-------|:-------:|:----:|
| 1 | 2026-04-09 | **Small-scale photonic Kolmogorov-Arnold networks using standard telecom nonlinear modules** | Luca Nogueira Calçado et al. | KAN, Kolmogorov-Arnold | [2604.08432](https://arxiv.org/abs/2604.08432) | 无 |
| 2 | 2026-04-07 | **Forecasting the first Edge Localized Mode (ELM) after LH-transition with a neural network trained on Doppler Backscattering data from DIII-D** | Nathan Qi Xuan Teo et al. | ELM | [2604.06508](https://arxiv.org/abs/2604.06508) | 无 |
| 3 | 2026-04-06 | **Non-monotonic causal discovery with Kolmogorov-Arnold Fuzzy Cognitive Maps** | Jose L. Salmeron et al. | Kolmogorov-Arnold | [2604.05136](https://arxiv.org/abs/2604.05136) | 无 |
| 4 | 2026-04-06 | **Interpretation of Crystal Energy Landscapes with Kolmogorov-Arnold Networks** | Gen Zu et al. | KAN, Kolmogorov-Arnold | [2604.04636](https://arxiv.org/abs/2604.04636) | 无 |
| 5 | 2026-04-06 | **Integer-Only Operations on Extreme Learning Machine Test Time Classification** | Emerson Lopes Machadoa et al. | ELM, Extreme Learning Machine | [2604.04363](https://arxiv.org/abs/2604.04363) | 无 |

## 详细摘要

### 1. Small-scale photonic Kolmogorov-Arnold networks using standard telecom nonlinear modules

- **作者**: Luca Nogueira Calçado, Sergei K. Turitsyn, Egor Manuylovich
- **发表日期**: 2026-04-09
- **关键词**: KAN, Kolmogorov-Arnold
- **论文链接**: [2604.08432](https://arxiv.org/abs/2604.08432) | [PDF](https://arxiv.org/pdf/2604.08432)
- **代码**: 无

> Photonic neural networks promise ultrafast inference, yet most architectures rely on linear optical meshes with electronic nonlinearities, reintroducing optical-electrical-optical bottlenecks. Here we introduce small-scale photonic Kolmogorov-Arnold networks (SSP-KANs) implemented entirely with standard telecommunications components. Each network edge employs a trainable nonlinear module composed of a Mach-Zehnder interferometer, semiconductor optical amplifier, and variable optical attenuators, providing a four-parameter transfer function derived from gain saturation and interferometric mixing. Despite this constrained expressivity, SSP-KANs comprising only a few optical modules achieve strong nonlinear inference performance across classification, regression, and image recognition tasks, approaching software baselines with significantly fewer parameters. A four-module network achieves 98.4\% accuracy on nonlinear classification benchmarks inaccessible to linear models. Performance remains robust under realistic hardware impairments, maintaining high accuracy down to 6-bit input resolution and 14 dB signal-to-noise ratio. By using a fully differentiable physics model for end-to-end optimisation of optical parameters, this work establishes a practical pathway from simulation to experimental demonstration of photonic KANs using commodity telecom hardware.

---

### 2. Forecasting the first Edge Localized Mode (ELM) after LH-transition with a neural network trained on Doppler Backscattering data from DIII-D

- **作者**: Nathan Qi Xuan Teo, Kshitish Barada, Valerian Hall-Chen, Lin Gu, Terry Lee Rhodes
- **发表日期**: 2026-04-07
- **关键词**: ELM
- **论文链接**: [2604.06508](https://arxiv.org/abs/2604.06508) | [PDF](https://arxiv.org/pdf/2604.06508)
- **代码**: 无

> In H-mode tokamak and stellarator plasmas, edge localized modes (ELMs) lead to the expulsion of heat and particles beyond the edge transport barrier. ELMs cause a loss of energy and have the potential to damage the divertor and other plasma facing components, which motivates efforts to forecast such events to work alongside mitigation systems. In this paper, we use the Doppler backscattering (DBS) diagnostic data as input to train a neural network model, adapted from DeepHit [Lee et al., Deephit, AAAI 2018], to forecast the first ELM crash of H-mode discharges in DIII-D. The model takes 50 ms of DBS spectrogram data and predicts the probability of an ELM crash occurring within set time windows. Training and testing on shots found in the DIII-D database, we find the initial results promising, with the model reliably forecasting the first ELM 100 ms before it occurs. This successful proof-of-concept lays a strong foundation for a predictive tool that can deploy ELM-mitigation techniques before an ELM crash occurs. Future work will expand the training set with carefully selected shots and refine the neural network architecture to improve model robustness to noise and data variation.

---

### 3. Non-monotonic causal discovery with Kolmogorov-Arnold Fuzzy Cognitive Maps

- **作者**: Jose L. Salmeron
- **发表日期**: 2026-04-06
- **关键词**: Kolmogorov-Arnold
- **论文链接**: [2604.05136](https://arxiv.org/abs/2604.05136) | [PDF](https://arxiv.org/pdf/2604.05136)
- **代码**: 无

> Fuzzy Cognitive Maps constitute a neuro-symbolic paradigm for modeling complex dynamic systems, widely adopted for their inherent interpretability and recurrent inference capabilities. However, the standard FCM formulation, characterized by scalar synaptic weights and monotonic activation functions, is fundamentally constrained in modeling non-monotonic causal dependencies, thereby limiting its efficacy in systems governed by saturation effects or periodic dynamics. To overcome this topological restriction, this research proposes the Kolmogorov-Arnold Fuzzy Cognitive Map (KA-FCM), a novel architecture that redefines the causal transmission mechanism. Drawing upon the Kolmogorov-Arnold representation theorem, static scalar weights are replaced with learnable, univariate B-spline functions located on the model edges. This fundamental modification shifts the non-linearity from the nodes' aggregation phase directly to the causal influence phase. This modification allows for the modeling of arbitrary, non-monotonic causal relationships without increasing the graph density or introducing hidden layers. The proposed architecture is validated against both baselines (standard FCM trained with Particle Swarm Optimization) and universal black-box approximators (Multi-Layer Perceptron) across three distinct domains: non-monotonic inference (Yerkes-Dodson law), symbolic regression, and chaotic time-series forecasting. Experimental results demonstrate that KA-FCMs significantly outperform conventional architectures and achieve competitive accuracy relative to MLPs, while preserving graph- based interpretability and enabling the explicit extraction of mathematical laws from the learned edges.

---

### 4. Interpretation of Crystal Energy Landscapes with Kolmogorov-Arnold Networks

- **作者**: Gen Zu, Ning Mao, Claudia Felser, Yang Zhang
- **发表日期**: 2026-04-06
- **关键词**: KAN, Kolmogorov-Arnold
- **论文链接**: [2604.04636](https://arxiv.org/abs/2604.04636) | [PDF](https://arxiv.org/pdf/2604.04636)
- **代码**: 无

> Characterizing crystalline energy landscapes is essential to predicting thermodynamic stability, electronic structure, and functional behavior. While machine learning (ML) enables rapid property predictions, the "black-box" nature of most models limits their utility for generating new scientific insights. Here, we introduce Kolmogorov-Arnold Networks (KANs) as an interpretable framework to bridge this gap. Unlike conventional neural networks with fixed activation functions, KANs employ learnable functions that reveal underlying physical relationships. We developed the Element-Weighted KAN, a composition-only model that achieves state-of-the-art accuracy in predicting formation energy, band gap, and work function across large-scale datasets. Crucially, without any explicit physical constraints, KANs uncover interpretable chemical trends aligned with the periodic table and quantum mechanical principles through embedding analysis, correlation studies, and principal component analysis. These results demonstrate that KANs provide a powerful framework with high predictive performance and scientific interpretability, establishing a new paradigm for transparent, chemistry-based materials informatics.

---

### 5. Integer-Only Operations on Extreme Learning Machine Test Time Classification

- **作者**: Emerson Lopes Machadoa, Cristiano Jacques Miosso, Ricardo Pezzuol Jacobi
- **发表日期**: 2026-04-06
- **关键词**: ELM, Extreme Learning Machine
- **论文链接**: [2604.04363](https://arxiv.org/abs/2604.04363) | [PDF](https://arxiv.org/pdf/2604.04363)
- **代码**: 无

> We present a theoretical analysis and empirical evaluations of a novel set of techniques for computational cost reduction of test time operations of network classifiers based on extreme learning machine (ELM). By exploring some characteristics we derived from these models, we show that the classification at test time can be performed using solely integer operations without compromising the classification accuracy. Our contributions are as follows: (i) We show empirical evidence that the input weights values can be drawn from the ternary set with limited reduction of the classification accuracy. This has the computational advantage of dismissing multiplications; (ii) We prove the classification accuracy of normalized and non-normalized test signals are the same; (iii) We show how to create an integer version of the output weights that results in a limited reduction of the classification accuracy. We tested our techniques on 5 computer vision datasets commonly used in the literature and the results indicate that our techniques can allow the reduction of the computational cost of the operations necessary for the classification at test time in FPGAs. This is important in embedded applications, where power consumption is limited, and crucial in data centers of large corporations, where power consumption is expensive.

---
