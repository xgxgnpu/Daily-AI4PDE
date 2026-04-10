# 数据驱动神经算子 (DeepONet, FNO, etc.) — 每日文献追踪

> 更新日期: 2026.04.10
> 检索关键词: DeepONet, FNO, Neural Operator, Operator Learning, Fourier Neural Operator
> 共 5 篇论文

## 论文列表

| # | 发表日期 | 标题 | 作者 | 关键词 | 论文链接 | 代码 |
|:---:|:--------:|:-----|:-----|:-------|:-------:|:----:|
| 1 | 2026-04-09 | **Numerical approximation of the Koopman-von Neumann equation: Operator learning and quantum computing** | Stefan Klus et al. | Operator Learning | [2604.08414](https://arxiv.org/abs/2604.08414) | 无 |
| 2 | 2026-04-09 | **$φ-$DeepONet: A Discontinuity Capturing Neural Operator** | Sumanta Roy et al. | Physics-Informed, Neural Operator, DeepONet, Domain Decomposition | [2604.08076](https://arxiv.org/abs/2604.08076) | 无 |
| 3 | 2026-04-08 | **Physics-informed neural operators for the in situ characterization of locally reacting sound absorbers** | Jonas M. Schmid et al. | Physics-Informed, Neural Operator, ELM | [2604.07412](https://arxiv.org/abs/2604.07412) | 无 |
| 4 | 2026-04-08 | **MENO: MeanFlow-Enhanced Neural Operators for Dynamical Systems** | Tianyue Yang et al. | Neural Operator, Surrogate, Diffusion, Multi-scale | [2604.06881](https://arxiv.org/abs/2604.06881) | 无 |
| 5 | 2026-04-07 | **Operator Learning for Surrogate Modeling of Wave-Induced Forces from Sea Surface Waves** | Shukai Cai et al. | DeepONet, Operator Learning, Surrogate | [2604.06433](https://arxiv.org/abs/2604.06433) | 无 |

## 详细摘要

### 1. Numerical approximation of the Koopman-von Neumann equation: Operator learning and quantum computing

- **作者**: Stefan Klus, Feliks Nüske, Patrick Gelß
- **发表日期**: 2026-04-09
- **关键词**: Operator Learning
- **论文链接**: [2604.08414](https://arxiv.org/abs/2604.08414) | [PDF](https://arxiv.org/pdf/2604.08414)
- **代码**: 无

> The Koopman-von Neumann equation describes the evolution of wavefunctions associated with autonomous ordinary differential equations and can be regarded as a quantum physics-inspired formulation of classical mechanics. The main advantage compared to conventional transfer operators such as Koopman and Perron-Frobenius operators is that the Koopman-von Neumann operator is unitary even if the dynamics are non-Hamiltonian. Projecting this operator onto a finite-dimensional subspace allows us to represent it by a unitary matrix, which in turn can be expressed as a quantum circuit. We will exploit relationships between the Koopman-von Neumann framework and classical transfer operators in order to derive numerical methods to approximate the Koopman-von Neumann operator and its eigenvalues and eigenfunctions from data. Furthermore, we will show that the choice of basis functions and domain are crucial to ensure that the operator is well-defined. We will illustrate the results with the aid of guiding examples, including simple undamped and damped oscillators and the Lotka-Volterra model.

---

### 2. $φ-$DeepONet: A Discontinuity Capturing Neural Operator

- **作者**: Sumanta Roy, Stephen T. Castonguay, Pratanu Roy, Michael D. Shields
- **发表日期**: 2026-04-09
- **关键词**: Physics-Informed, Neural Operator, DeepONet, Domain Decomposition
- **论文链接**: [2604.08076](https://arxiv.org/abs/2604.08076) | [PDF](https://arxiv.org/pdf/2604.08076)
- **代码**: 无

> We present $φ-$DeepONet, a physics-informed neural operator designed to learn mappings between function spaces that may contain discontinuities or exhibit non-smooth behavior. Classical neural operators are based on the universal approximation theorem which assumes that both the operator and the functions it acts on are continuous. However, many scientific and engineering problems involve naturally discontinuous input fields as well as strong and weak discontinuities in the output fields caused by material interfaces. In $φ$-DeepONet, discontinuities in the input are handled using multiple branch networks, while discontinuities in the output are learned through a nonlinear latent embedding of the interface. This embedding is constructed from a {\it one-hot} representation of the domain decomposition that is combined with the spatial coordinates in a modified trunk network. The outputs of the branch and trunk networks are then combined through a dot product to produce the final solution, which is trained using a physics- and interface-informed loss function. We evaluate $φ$-DeepONet on several one- and two-dimensional benchmark problems and demonstrate that it delivers accurate and stable predictions even in the presence of strong interface-driven discontinuities.

---

### 3. Physics-informed neural operators for the in situ characterization of locally reacting sound absorbers

- **作者**: Jonas M. Schmid, Johannes D. Schmid, Martin Eser, Steffen Marburg
- **发表日期**: 2026-04-08
- **关键词**: Physics-Informed, Neural Operator, ELM
- **论文链接**: [2604.07412](https://arxiv.org/abs/2604.07412) | [PDF](https://arxiv.org/pdf/2604.07412)
- **代码**: 无

> Accurate knowledge of acoustic surface admittance or impedance is essential for reliable wave-based simulations, yet its in situ estimation remains challenging due to noise, model inaccuracies, and restrictive assumptions of conventional methods. This work presents a physics-informed neural operator approach for estimating frequency-dependent surface admittance directly from near-field measurements of sound pressure and particle velocity. A deep operator network is employed to learn the mapping from measurement data, spatial coordinates, and frequency to acoustic field quantities, while simultaneously inferring a globally consistent surface admittance spectrum without requiring an explicit forward model. The governing acoustic relations, including the Helmholtz equation, the linearized momentum equation, and Robin boundary conditions, are embedded into the training process as physics-based regularization, enabling physically consistent and noise-robust predictions while avoiding frequency-wise inversion. The method is validated using synthetically generated data from a simulation model for two planar porous absorbers under semi free-field conditions across a broad frequency range. Results demonstrate accurate reconstruction of both real and imaginary admittance components and reliable prediction of acoustic field quantities. Parameter studies confirm improved robustness to noise and sparse sampling compared to purely data-driven approaches, highlighting the potential of physics-informed neural operators for in situ acoustic material characterization.

---

### 4. MENO: MeanFlow-Enhanced Neural Operators for Dynamical Systems

- **作者**: Tianyue Yang, Xiao Xue
- **发表日期**: 2026-04-08
- **关键词**: Neural Operator, Surrogate, Diffusion, Multi-scale
- **论文链接**: [2604.06881](https://arxiv.org/abs/2604.06881) | [PDF](https://arxiv.org/pdf/2604.06881)
- **代码**: 无

> Neural operators have emerged as powerful surrogates for dynamical systems due to their grid-invariant properties and computational efficiency. However, the Fourier-based neural operator framework inherently truncates high-frequency components in spectral space, resulting in the loss of small-scale structures and degraded prediction quality at high resolutions when trained on low-resolution data. While diffusion-based enhancement methods can recover multi-scale features, they introduce substantial inference overhead that undermines the efficiency advantage of neural operators. In this work, we introduce \textbf{M}eanFlow-\textbf{E}nhanced \textbf{N}eural \textbf{O}perators (MENO), a novel framework that achieves accurate all-scale predictions with minimal inference cost. By leveraging the improved MeanFlow method, MENO restores both small-scale details and large-scale dynamics with superior physical fidelity and statistical accuracy. We evaluate MENO on three challenging dynamical systems, including phase-field dynamics, 2D Kolmogorov flow, and active matter dynamics, at resolutions up to 256$\times$256. Across all benchmarks, MENO improves the power spectrum density accuracy by up to a factor of 2 compared to baseline neural operators while achieving 12$\times$ faster inference than the state-of-the-art Diffusion Denoising Implicit Model (DDIM)-enhanced counterparts, effectively bridging the gap between accuracy and efficiency. The flexibility and efficiency of MENO position it as an efficient surrogate model for scientific machine learning applications where both statistical integrity and computational efficiency are paramount.

---

### 5. Operator Learning for Surrogate Modeling of Wave-Induced Forces from Sea Surface Waves

- **作者**: Shukai Cai, Sourav Dutta, Mark Loveland, Eirik Valseth, Peter Rivera-Casillas, Corey Trahan, Clint Dawson
- **发表日期**: 2026-04-07
- **关键词**: DeepONet, Operator Learning, Surrogate
- **论文链接**: [2604.06433](https://arxiv.org/abs/2604.06433) | [PDF](https://arxiv.org/pdf/2604.06433)
- **代码**: 无

> Wave setup plays a significant role in transferring wave-induced energy to currents and causing an increase in water elevation. This excess momentum flux, known as radiation stress, motivates the coupling of circulation models with wave models to improve the accuracy of storm surge prediction, however, traditional numerical wave models are complex and computationally expensive. As a result, in practical coupled simulations, wave models are often executed at much coarser temporal resolution than circulation models. In this work, we explore the use of Deep Operator Networks (DeepONets) as a surrogate for the Simulating WAves Nearshore (SWAN) numerical wave model. The proposed surrogate model was tested on three distinct 1-D and 2-D steady-state numerical examples with variable boundary wave conditions and wind fields. When applied to a realistic numerical example of steady state wave simulation in Duck, NC, the model achieved consistently high accuracy in predicting the components of the radiation stress gradient and the significant wave height across representative scenarios.

---
