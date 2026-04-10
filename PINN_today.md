# PINN (Physics-Informed Neural Networks) — 每日文献追踪

> 更新日期: 2026.04.10
> 检索关键词: PINN, 物理信息神经网络, Physics-Informed Learning
> 共 5 篇论文

## 论文列表

| # | 发表日期 | 标题 | 作者 | 关键词 | 论文链接 | 代码 |
|:---:|:--------:|:-----|:-----|:-------|:-------:|:----:|
| 1 | 2026-04-09 | **Hard-constrained Physics-informed Neural Networks for Interface Problems** | Seung Whan Chung et al. | PINN, PINNs, Physics-Informed, PDE | [2604.08453](https://arxiv.org/abs/2604.08453) | 无 |
| 2 | 2026-04-09 | **A Helicity-Conservative Domain-Decomposed Physics-Informed Neural Network for Incompressible Non-Newtonian Flow** | Zheng Lu et al. | PINN, PINNs, Physics-Informed, Finite Element, Domain Decomposition | [2604.08002](https://arxiv.org/abs/2604.08002) | 无 |
| 3 | 2026-04-09 | **Second Order Physics-Informed Learning of Road Density using Probe Vehicles** | S. Betancur Giraldo et al. | Physics-Informed | [2604.07918](https://arxiv.org/abs/2604.07918) | 无 |
| 4 | 2026-04-08 | **Physics-Informed Discrete-Event Simulation of Polarization-Encoded Quantum Networks** | Abderrahim Amlou et al. | Physics-Informed | [2604.07289](https://arxiv.org/abs/2604.07289) | 无 |
| 5 | 2026-04-08 | **Physics-Informed 3D Atomic Reconstruction and Dynamics of Free-Standing Graphene from Single Low-Dose TEM Images** | Xiaojun Zhang et al. | Physics-Informed | [2604.07271](https://arxiv.org/abs/2604.07271) | 无 |

## 详细摘要

### 1. Hard-constrained Physics-informed Neural Networks for Interface Problems

- **作者**: Seung Whan Chung, Stephen Castonguay, Sumanta Roy, Michael Penwarden, Yucheng Fu, Pratanu Roy
- **发表日期**: 2026-04-09
- **关键词**: PINN, PINNs, Physics-Informed, PDE
- **论文链接**: [2604.08453](https://arxiv.org/abs/2604.08453) | [PDF](https://arxiv.org/pdf/2604.08453)
- **代码**: 无

> Physics-informed neural networks (PINNs) have emerged as a flexible framework for solving partial differential equations, but their performance on interface problems remains challenging because continuity and flux conditions are typically imposed through soft penalty terms. The standard soft-constraint formulation leads to imperfect interface enforcement and degraded accuracy near interfaces. We introduce two ansatz-based hard-constrained PINN formulations for interface problems that embed the interface physics into the solution representation and thereby decouple interface enforcement from PDE residual minimization. The first, termed the windowing approach, constructs the trial space from compactly supported windowed subnetworks so that interface continuity and flux balance are satisfied by design. The second, called the buffer approach, augments unrestricted subnetworks with auxiliary buffer functions that enforce boundary and interface constraints at discrete points through a lightweight correction. We study these formulations on one- and two-dimensional elliptic interface benchmarks and compare them with soft-constrained baselines. In one-dimensional problems, hard constraints consistently improve interface fidelity and remove the need for loss-weight tuning; the windowing approach attains very high accuracy (as low as $O(10^{-9})$) on simple structured cases, whereas the buffer approach remains accurate ($\sim O(10^{-5})$) across a wider range of source terms and interface configurations. In two dimensions, the buffer formulation is shown to be more robust because it enforces constraints through a discrete buffer correction, as the windowing construction becomes more sensitive to overlap and corner effects and over-constrains the problem. This positions the buffer method as a straightforward and geometrically flexible approach to complex interface problems.

---

### 2. A Helicity-Conservative Domain-Decomposed Physics-Informed Neural Network for Incompressible Non-Newtonian Flow

- **作者**: Zheng Lu, Young Ju Lee, Jiwei Jia, Ziqian Li
- **发表日期**: 2026-04-09
- **关键词**: PINN, PINNs, Physics-Informed, Finite Element, Domain Decomposition
- **论文链接**: [2604.08002](https://arxiv.org/abs/2604.08002) | [PDF](https://arxiv.org/pdf/2604.08002)
- **代码**: 无

> This paper develops a helicity-aware physics-informed neural network framework for incompressible non-Newtonian flow in rotational form. In addition to the energy law and the incompressibility constraint, helicity is a fundamental geometric quantity that characterizes the topology of vortex lines and plays an important role in the physical fidelity of long-time flow simulations. While helicity-preserving discretizations have been studied extensively in finite difference, finite element, and other structure-preserving settings, their realization within neural network solvers remains largely unexplored. Motivated by this gap, we propose a neural formulation in which vorticity is computed directly from the neural velocity field by automatic differentiation rather than learned as an independent output, thereby avoiding compatibility errors that pollute the helicity balance. To improve robustness and scalability, we combine two algorithmic ingredients: an overlapping spatial domain decomposition inspired by finite-basis physics-informed neural networks (FBPINNs), and a causal slab-wise temporal continuation strategy for long-time transient simulations. The local subnetworks are blended by explicitly normalized super-Gaussian window functions, which yield a smooth partition of unity, while the temporal evolution is advanced sequentially across time slabs by transferring the converged solution on one slab to the next. The resulting spatiotemporal framework provides a stable and physically meaningful approach for helicity-aware simulation of incompressible non-Newtonian flows.

---

### 3. Second Order Physics-Informed Learning of Road Density using Probe Vehicles

- **作者**: S. Betancur Giraldo, J. Mårtensson, M. Barreau
- **发表日期**: 2026-04-09
- **关键词**: Physics-Informed
- **论文链接**: [2604.07918](https://arxiv.org/abs/2604.07918) | [PDF](https://arxiv.org/pdf/2604.07918)
- **代码**: 无

> We propose a Physics Informed Learning framework for reconstructing traffic density from sparse trajectory data. The approach combines a second-order Aw-Rascle and Zhang model with a first-order training stage to estimate the equilibrium velocity. The method is evaluated in both equilibrium and transient traffic regimes using SUMO simulations. Results show that while learning the equilibrium velocity improves reconstruction under steady state conditions, it becomes unstable in transient regimes due to the breakdown of the equilibrium assumption. In contrast, the second-order model consistently provides more accurate and robust reconstructions than first-order approaches, particularly in nonequilibrium conditions.

---

### 4. Physics-Informed Discrete-Event Simulation of Polarization-Encoded Quantum Networks

- **作者**: Abderrahim Amlou, Amar Abane, Cory M. Nunn, M. V. Jabir, Van Sy Mai, Abdella Battou, Ahmed Lbath
- **发表日期**: 2026-04-08
- **关键词**: Physics-Informed
- **论文链接**: [2604.07289](https://arxiv.org/abs/2604.07289) | [PDF](https://arxiv.org/pdf/2604.07289)
- **代码**: 无

> We extend the SeQUeNCe discrete-event simulator with physics-based models for polarization-encoded photonic quantum networks. Our framework integrates Jones-calculus optical components, including an SPDC Bell-state source, wave plates, and polarizing beam splitters, together with a multi-section fiber model capturing polarization mode dispersion, chromatic dispersion, and Raman noise from coexisting classical traffic. We validate the simulator by reproducing experimentally reported spectra, polarization correlations, quantum state tomography, and dispersion- and Raman-induced noise. The resulting platform enables hardware-parameterized prediction of entanglement distribution performance under realistic deployment conditions.

---

### 5. Physics-Informed 3D Atomic Reconstruction and Dynamics of Free-Standing Graphene from Single Low-Dose TEM Images

- **作者**: Xiaojun Zhang, Shih-Wei Hung, Yawei Wu, Jyh-Pin Chou, Angus I. Kirkland, Roar Kilaas, Fu-Rong Chen
- **发表日期**: 2026-04-08
- **关键词**: Physics-Informed
- **论文链接**: [2604.07271](https://arxiv.org/abs/2604.07271) | [PDF](https://arxiv.org/pdf/2604.07271)
- **代码**: 无

> Resolving the three-dimensional (3D) atomic geometry of free-standing graphene in real time is essential for understanding how intrinsic rippling governs its electronic properties. However, the low electron doses required to mitigate radiation damage impose severe signal-to-noise constraints that limit conventional reconstruction methods. Here, we present a physics-informed computational framework that reconstructs 3D atomic coordinates of single-layer graphene from individual low-dose transmission electron microscopy (TEM) frames (8x10^3 e-/Ang^2, 1 ms temporal resolution). The approach combines simulated annealing optimisation with molecular dynamics regularisation, achieving sub-angstrom out-of-plane accuracy (sigma_z < 0.45 Ang), validated against ground-truth simulations. A Kullback-Leibler divergence-based calibration aligns the forward model with experimental image statistics, reducing systematic bias. Applied to high-speed time-series data, the framework enables simultaneous extraction of real-time ripple dynamics, strain tensors, surface curvature, bond-length distributions, and density functional theory (DFT)-derived electron localisation functions (ELF). We establish quantitative relationships linking local geometry, strain, and bond-length variations to electron localisation, demonstrating that sub-angstrom structural fluctuations drive spatially localised, millisecond-scale electronic modulation. A critical dose threshold is identified below which structural information becomes irrecoverable, providing practical guidance for experimental design. The framework is broadly applicable to beam-sensitive two-dimensional materials.

---
