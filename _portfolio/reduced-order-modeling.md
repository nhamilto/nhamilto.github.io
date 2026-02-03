---
title: "Reduced-Order Modeling & Physics-Informed Machine Learning"
excerpt: "Developing computationally efficient models of turbulent flows using modal decomposition, POD, and physics-informed machine learning<br/><img src='/images/rom-thumb.png' width='650'>"
collection: portfolio
---

## Research Approach

Wind turbine wakes and atmospheric turbulence are governed by the Navier-Stokes equations, which can't be solved analytically, and high-fidelity computational simulations are expensive. My research develops reduced-order models (ROMs) that capture essential physics while remaining computationally tractable—enabling real-time control, rapid design iteration, and physics-informed machine learning that respects fundamental conservation laws.

## Methodological Foundations

### Modal Decomposition Techniques

We apply advanced decomposition methods to extract coherent structures from turbulent flows:

**Proper Orthogonal Decomposition (POD)**
- Identifies optimal basis functions representing dominant flow features
- Enables reconstruction of wind turbine wakes using 10-20 modes instead of millions of grid points
- Provides energy-ranked representation highlighting most important scales

**Dynamic Mode Decomposition (DMD)**
- Extracts spatiotemporal coherent structures with associated frequencies and growth rates
- Reveals wake meandering modes, vortex shedding frequencies, and instability mechanisms
- Enables linear prediction of nonlinear wake evolution

**HAVOK & Koopman Operator Theory**
- HAVOK (Hankel Atlernative View Of Koopman) leverages time-delay embedding and sparse regression to uncover governing equations from data
- Koopman operator theory lifts nonlinear dynamics into a higher-dimensional linear space, enabling analytic prediction and modal decomposition
- Critical for identifying dominant dynamical modes, forecasting wake evolution, and revealing underlying mechanisms in complex turbulent flows

### Physics-Informed Machine Learning

Rather than pure data-driven approaches, we integrate physical constraints into machine learning architectures:

**Physics-Informed Neural Networks (PINNs)**
- Enforce conservation of mass, momentum, and energy as hard constraints within loss functions
- Train on sparse field campaign data while respecting fundamental fluid mechanics
- Generalize beyond training data by embedding physical laws

**Reduced-Order Modeling via Neural ODEs**
- Learn governing equations for modal coefficients, creating data-driven dynamical systems
- Capture nonlinear modal interactions governing wake evolution
- Enable long-time prediction with quantified uncertainty

**Operator Learning (FNO, DeepONet)**
- Learn mappings between function spaces (e.g., inflow conditions → wake structure)
- Achieve orders of magnitude speedup over traditional simulation
- Incorporate physics through conservation form and boundary conditions

## Applications to Wind Energy

### Wake Prediction & Control

ROMs enable real-time wake steering and plant-level optimization:
- **Yaw Control**: Predict wake deflection from turbine yaw misalignment in milliseconds, enabling closed-loop control
- **Load Estimation**: Rapidly evaluate fatigue loads across design parameter space
- **Power Forecasting**: Incorporate ROM predictions into short-term power forecasting systems

### Digital Twins

Physics-based ROMs form the core of digital twin systems:
- **State Estimation**: Combine sparse sensor data with ROMs to estimate full flow field
- **Anomaly Detection**: Identify deviations from physics-based predictions indicating degradation or faults
- **Predictive Maintenance**: Forecast component loads and remaining useful life

### Design Optimization

ROMs accelerate turbine and wind plant design:
- **Rapid Prototyping**: Evaluate thousands of design variants in hours instead of months
- **Uncertainty Quantification**: Efficiently propagate atmospheric uncertainties through design process
- **Multidisciplinary Optimization**: Couple aerodynamics, structures, and controls at minimal computational cost

## Key Research Areas

### Wake Meandering Models

We've developed ROMs capturing large-scale wake oscillations:
- Identified dominant POD modes representing wake meandering dynamics
- Derived nonlinear ordinary differential equations (ODEs) governing modal evolution
- Validated against field campaign data (AWAKEN, RAAW) demonstrating 10-100x speedup vs LES

### Turbulence Reconstruction

Our methods reconstruct turbulent inflow from limited measurements:
- Applied compressed sensing and sparse reconstruction to tower/lidar data
- Developed stochastic models generating synthetic turbulence matching measured statistics
- Integrated with wind turbine simulation tools for load validation

### Hybrid Physics-ML Frameworks

We've explored hybrid approaches combining traditional ROMs with machine learning:
- Use POD/DMD to reduce dimensionality, then ML to learn modal dynamics
- Enforce conservation laws while learning unclosed terms (e.g., turbulence closure)
- Achieve interpretability and generalization difficult with pure black-box ML

## Validation & Impact

ROMs developed in my research have been validated against:
- **Field Data**: AWAKEN, RAAW, and SWiFT measurements demonstrating accuracy within 5-10% of observations
- **High-Fidelity Simulation**: Large eddy simulations confirming ROM predictions at fraction of computational cost
- **Wind Plant Operations**: Deployment at operational wind plants showing real-time forecasting capabilities

Impact includes:
- **15+ peer-reviewed publications** on ROM methods, modal decomposition, and physics-informed ML
- **Open-source software** released to wind energy community
- **Industry adoption** by turbine OEMs and wind plant operators for control and forecasting
- **Educational impact** through workshops, tutorials, and graduate student training

## Technical Challenges Overcome

Developing ROMs for wind energy required solving fundamental problems:
1. **Nonlinearity**: Wake dynamics exhibit strong nonlinearities requiring careful modal truncation and closure modeling
2. **Multiscale Coupling**: Capturing interactions between turbulent eddies (cm-m scales) and wind plant wakes (km scales)
3. **Data Sparsity**: Field campaigns provide limited spatiotemporal coverage, demanding clever interpolation and extrapolation
4. **Uncertainty**: Atmospheric conditions vary continuously, requiring robust methods accounting for variability

## Current Research Directions

Ongoing work pushes ROM capabilities:
- **Koopman Operators**: Lifting nonlinear dynamics to infinite-dimensional linear spaces enabling analytic prediction
- **Sparse Identification**: Using sparse regression (SINDy) to discover governing equations directly from data
- **Multi-Fidelity Methods**: Optimally blending low-fidelity ROMs with occasional high-fidelity simulations
- **Transfer Learning**: Adapting ROMs trained on one wind plant to new sites with minimal retraining

## Future Directions
The future of reduced-order modeling lies in tightly coupling ROMs for nonlinear dynamical systems with neural operators that learn complex nonlinear forcing and system responses. By integrating metriplectic system frameworks, we can enforce dissipative processes and losses as intrinsic physical mechanisms—rather than relying on artificial numerical constraints or loss functions. This approach enables:

- Physics-consistent modeling of energy dissipation, turbulence, and wake losses
- Neural operators that map nonlinear inputs (e.g., atmospheric variability) to system responses while respecting conservation and dissipation laws
- ROMs that capture both dominant modal dynamics and nonlinear interactions, with metriplectic structure ensuring thermodynamic consistency
- Scalable, interpretable models for real-time wind plant optimization, adaptive control, and robust forecasting

This next-generation framework bridges fundamental nonlinear physics and data-driven modeling, unlocking reliable, efficient wind energy systems.

