# 物理信息神经算子 (PI-DeepONet, PINO, etc.) — 每日文献追踪

> 更新日期: 2026.04.10
> 检索关键词: PI-DeepONet, PINO, Physics-Informed Neural Operator, PIFNO
> 共 5 篇论文

## 论文列表

| # | 发表日期 | 标题 | 作者 | 关键词 | 论文链接 | 代码 |
|:---:|:--------:|:-----|:-----|:-------|:-------:|:----:|
| 1 | 2026-04-09 | **$φ-$DeepONet: A Discontinuity Capturing Neural Operator** | Sumanta Roy et al. | Physics-Informed, Neural Operator, DeepONet, Domain Decomposition | [2604.08076](https://arxiv.org/abs/2604.08076) | 无 |
| 2 | 2026-04-08 | **Physics-informed neural operators for the in situ characterization of locally reacting sound absorbers** | Jonas M. Schmid et al. | Physics-Informed, Neural Operator, ELM | [2604.07412](https://arxiv.org/abs/2604.07412) | 无 |
| 3 | 2026-03-26 | **Physics-Informed Neural Operator for Electromagnetic Inverse Scattering Problems** | Q. C. Dong et al. | Physics-Informed, Neural Operator, FNO, Fourier Neural Operator, PINO | [2603.25404](https://arxiv.org/abs/2603.25404) | 无 |
| 4 | 2026-03-23 | **SPINONet: Scalable Spiking Physics-informed Neural Operator for Computational Mechanics Applications** | Shailesh Garg et al. | Physics-Informed, Neural Operator, Operator Learning, PINO | [2603.21674](https://arxiv.org/abs/2603.21674) | 无 |
| 5 | 2026-03-17 | **What if Pinocchio Were a Reinforcement Learning Agent: A Normative End-to-End Pipeline** | Benoît Alcaraz et al. | PINO | [2603.16651](https://arxiv.org/abs/2603.16651) | 无 |

## 详细摘要

### 1. $φ-$DeepONet: A Discontinuity Capturing Neural Operator

- **作者**: Sumanta Roy, Stephen T. Castonguay, Pratanu Roy, Michael D. Shields
- **发表日期**: 2026-04-09
- **关键词**: Physics-Informed, Neural Operator, DeepONet, Domain Decomposition
- **论文链接**: [2604.08076](https://arxiv.org/abs/2604.08076) | [PDF](https://arxiv.org/pdf/2604.08076)
- **代码**: 无

> We present $φ-$DeepONet, a physics-informed neural operator designed to learn mappings between function spaces that may contain discontinuities or exhibit non-smooth behavior. Classical neural operators are based on the universal approximation theorem which assumes that both the operator and the functions it acts on are continuous. However, many scientific and engineering problems involve naturally discontinuous input fields as well as strong and weak discontinuities in the output fields caused by material interfaces. In $φ$-DeepONet, discontinuities in the input are handled using multiple branch networks, while discontinuities in the output are learned through a nonlinear latent embedding of the interface. This embedding is constructed from a {\it one-hot} representation of the domain decomposition that is combined with the spatial coordinates in a modified trunk network. The outputs of the branch and trunk networks are then combined through a dot product to produce the final solution, which is trained using a physics- and interface-informed loss function. We evaluate $φ$-DeepONet on several one- and two-dimensional benchmark problems and demonstrate that it delivers accurate and stable predictions even in the presence of strong interface-driven discontinuities.

---

### 2. Physics-informed neural operators for the in situ characterization of locally reacting sound absorbers

- **作者**: Jonas M. Schmid, Johannes D. Schmid, Martin Eser, Steffen Marburg
- **发表日期**: 2026-04-08
- **关键词**: Physics-Informed, Neural Operator, ELM
- **论文链接**: [2604.07412](https://arxiv.org/abs/2604.07412) | [PDF](https://arxiv.org/pdf/2604.07412)
- **代码**: 无

> Accurate knowledge of acoustic surface admittance or impedance is essential for reliable wave-based simulations, yet its in situ estimation remains challenging due to noise, model inaccuracies, and restrictive assumptions of conventional methods. This work presents a physics-informed neural operator approach for estimating frequency-dependent surface admittance directly from near-field measurements of sound pressure and particle velocity. A deep operator network is employed to learn the mapping from measurement data, spatial coordinates, and frequency to acoustic field quantities, while simultaneously inferring a globally consistent surface admittance spectrum without requiring an explicit forward model. The governing acoustic relations, including the Helmholtz equation, the linearized momentum equation, and Robin boundary conditions, are embedded into the training process as physics-based regularization, enabling physically consistent and noise-robust predictions while avoiding frequency-wise inversion. The method is validated using synthetically generated data from a simulation model for two planar porous absorbers under semi free-field conditions across a broad frequency range. Results demonstrate accurate reconstruction of both real and imaginary admittance components and reliable prediction of acoustic field quantities. Parameter studies confirm improved robustness to noise and sparse sampling compared to purely data-driven approaches, highlighting the potential of physics-informed neural operators for in situ acoustic material characterization.

---

### 3. Physics-Informed Neural Operator for Electromagnetic Inverse Scattering Problems

- **作者**: Q. C. Dong, Zi-Xuan Su, Qing Huo Liu, Wen Chen, Zhizhang, Chen
- **发表日期**: 2026-03-26
- **关键词**: Physics-Informed, Neural Operator, FNO, Fourier Neural Operator, PINO
- **论文链接**: [2603.25404](https://arxiv.org/abs/2603.25404) | [PDF](https://arxiv.org/pdf/2603.25404)
- **代码**: 无

> This paper proposes a physics-informed neural operator (PINO) framework for solving inverse scattering problems, enabling rapid and accurate reconstructions under diverse measurement conditions. In the proposed approach, the dielectric property is represented as a learnable tensor, while a neural operator is employed to predict the induced current distribution. A hybrid loss function, consisting of the state loss, data loss and total-variation (TV) regularization, is constructed to establish a fully differentiable formulation for a joint optimization of network parameters and dielectric property. To demonstrate the framework's generality and flexibility, PINO is implemented using three representative neural operators, i.e., the Fourier Neural Operator (FNO), the enhanced Fourier Neural Operator (U-FNO) and the Factorized Fourier Neural Operator (F-FNO). Compared with conventional approaches, the proposed framework offers a simpler formulation and universal modeling capability, making it readily applicable to various measurement scenarios, including multi-frequency and phaseless inversion. Numerical simulations demonstrate that the proposed PINO achieves high accuracy and robust reconstruction across samples with and without phase information, under single-frequency and multi-frequency settings in the presence of noise. The results demonstrate that PINO consistently outperforms conventional contrast-source inversion (CSI) methods and provides an efficient, unified solution to complex electromagnetic inverse-scattering problems.

---

### 4. SPINONet: Scalable Spiking Physics-informed Neural Operator for Computational Mechanics Applications

- **作者**: Shailesh Garg, Luis Mandl, Somdatta Goswami, Souvik Chakraborty
- **发表日期**: 2026-03-23
- **关键词**: Physics-Informed, Neural Operator, Operator Learning, PINO
- **论文链接**: [2603.21674](https://arxiv.org/abs/2603.21674) | [PDF](https://arxiv.org/pdf/2603.21674)
- **代码**: 无

> Energy efficiency remains a critical challenge in deploying physics-informed operator learning models for computational mechanics and scientific computing, particularly in power-constrained settings such as edge and embedded devices, where repeated operator evaluations in dense networks incur substantial computational and energy costs. To address this challenge, we introduce the Separable Physics-informed Neuroscience-inspired Operator Network (SPINONet), a neuroscience-inspired framework that reduces redundant computation across repeated evaluations while remaining compatible with physics-informed training. SPINONet incorporates regression-friendly neuroscience-inspired spiking neurons through an architecture-aware design that enables sparse, event-driven computation, improving energy efficiency while preserving the continuous, coordinate-differentiable pathways required for computing spatio-temporal derivatives. We evaluate SPINONet on a range of partial differential equations representative of computational mechanics problems, with spatial, temporal, and parametric dependencies in both time-dependent and steady-state settings, and demonstrate predictive performance comparable to conventional physics-informed operator learning approaches despite the induced sparse communication. In addition, limited data supervision in a hybrid setup is shown to improve performance in challenging regimes where purely physics-informed training may converge to spurious solutions. Finally, we provide an analytical discussion linking architectural components and design choices of SPINONet to reductions in computational load and energy consumption.

---

### 5. What if Pinocchio Were a Reinforcement Learning Agent: A Normative End-to-End Pipeline

- **作者**: Benoît Alcaraz
- **发表日期**: 2026-03-17
- **关键词**: PINO
- **论文链接**: [2603.16651](https://arxiv.org/abs/2603.16651) | [PDF](https://arxiv.org/pdf/2603.16651)
- **代码**: 无

> In the past decade, artificial intelligence (AI) has developed quickly. With this rapid progression came the need for systems capable of complying with the rules and norms of our society so that they can be successfully and safely integrated into our daily lives. Inspired by the story of Pinocchio in ``Le avventure di Pinocchio - Storia di un burattino'', this thesis proposes a pipeline that addresses the problem of developing norm compliant and context-aware agents. Building on the AJAR, Jiminy, and NGRL architectures, the work introduces \pino, a hybrid model in which reinforcement learning agents are supervised by argumentation-based normative advisors. In order to make this pipeline operational, this thesis also presents a novel algorithm for automatically extracting the arguments and relationships that underlie the advisors' decisions. Finally, this thesis investigates the phenomenon of \textit{norm avoidance}, providing a definition and a mitigation strategy within the context of reinforcement learning agents. Each component of the pipeline is empirically evaluated. The thesis concludes with a discussion of related work, current limitations, and directions for future research.

---
