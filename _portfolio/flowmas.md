---
title: "FLOWMAS: Exascale Computing for Floating Offshore Wind"
excerpt: "$19M DOE Office of Science project developing algorithms for coupled fluid-structure-mooring dynamics at exascale<br/><img src='/images/flowmas-thumb.jpg' width='600'><br/><em style='font-size: 0.85em;'>Two of the five Energy Earthshots projects NREL is involved in consider wind technology. Photo by Brent Rice, NREL</em>"
collection: portfolio
---

## Project Vision

The FLOating Offshore Wind MAchine Simulator (FLOWMAS) develops simulation capabilities for floating offshore wind turbine design using exascale computing. This $19M DOE Office of Science project, supported by the Exascale Computing Project, focuses on algorithms that can predict coupled aerodynamic-hydrodynamic-structural-mooring dynamics on the world's fastest supercomputers.

## My Contributions

I led the data assimilation and digital twin component of FLOWMAS, developing methods to integrate observational data with the multiscale simulation stack and create operational frameworks for real-time system monitoring and control.

### Data Assimilation Across Scales
- Developed variational data assimilation techniques (3D-Var and 4D-Var) for integrating diverse observational datasets (remote sensing, in situ measurements, satellite data) into coupled E3SM-ExaWind simulations
- Implemented ensemble Kalman filtering (EnKF) for real-time state estimation in nonlinear coupled metocean-turbine systems
- Explored latent diffusion models and Gaussian process state space models for handling strong nonlinearities in floating platform dynamics
- Created multiscale data fusion frameworks integrating climate data from E3SM with wind farm performance data from ExaWind

### Digital Twin Development
- Designed digital twin architecture closing the loop between multiscale high-fidelity modeling, measurement system design, adaptive control, and real-time state observation
- Developed compressed sensing strategies distilling multimodal data into optimal subsets of observables describing combined system dynamics
- Integrated measurement system design with controllability analysis, optimizing sensor placement for observability of coupled nonlinear metocean dynamics
- Implemented uncertainty quantification frameworks providing confidence intervals for state estimates and predictions

### Reduced-Order Modeling
- Developed ROM techniques capturing essential physics while reducing computational complexity by 100-1000x
- Created models continuously updated through data assimilation, incorporating observational data for accurate and computationally efficient system representation
- Enabled efficient propagation of uncertainties from high-fidelity simulations to reduced models

## Technical Challenges

Floating offshore wind simulation presents extreme computational demands:
- **Multi-Physics Coupling**: Simultaneously resolving atmospheric turbulence (1-1000m scales), aerodynamic blade loads (0.01-100m), structural dynamics (0.001-10 Hz), ocean waves (1-100m), and mooring system tension (10-1000m)
- **Platform Motion**: Six degree-of-freedom platform dynamics create time-varying inflow conditions and gyroscopic loads requiring sophisticated coupling algorithms
- **Extreme Events**: Accurately predicting loads during hurricanes, extreme waves, and combined wind-wave events critical for structural design
- **Computational Scale**: Resolving all relevant physics requires O(10^9-10^11) degrees of freedom, achievable only on exascale systems

## Exascale Algorithms

FLOWMAS leverages cutting-edge computational methods:
- **Massively Parallel LES**: Achieving strong scaling to 100,000+ cores using advanced domain decomposition and communication-avoiding algorithms
- **GPU Acceleration**: Porting critical kernels to GPU architectures on Frontier, Aurora, and El Capitan supercomputers
- **Adaptive Mesh Refinement**: Dynamically refining mesh resolution near wakes, free surfaces, and structural components
- **Multi-Fidelity Methods**: Coupling high-fidelity CFD with reduced-order models optimizing computational cost vs accuracy tradeoffs

## Impact on Offshore Wind

FLOWMAS capabilities directly advance floating offshore wind technology:
1. **Design Optimization**: Enabling exploration of novel platform concepts, turbine configurations, and mooring systems through rapid digital prototyping
2. **Load Prediction**: Improving accuracy of fatigue and ultimate load calculations, reducing structural over-design and lowering costs
3. **Control Strategies**: Developing physics-informed control algorithms managing platform motion, turbine loading, and power production
4. **Risk Assessment**: Quantifying uncertainties in extreme event prediction, informing insurance and financing decisions

## Offshore Wind Context

Floating offshore wind represents the next frontier in renewable energy:
- **Resource**: 60% of US offshore wind potential exists in waters too deep for fixed-bottom foundations
- **Technology Gap**: Existing design tools validated primarily for fixed-bottom turbines, requiring exascale simulations for confidence in floating systems
- **Market Potential**: Global offshore wind capacity projected to reach 250+ GW by 2030, with significant floating component
- **US Leadership**: FLOWMAS positions US national laboratories and offshore wind industry to lead global technology development

## Partnerships & Computing Resources

- **Funding**: $19M DOE Office of Science (Exascale Computing Project, Advanced Scientific Computing Research)
- **Duration**: 2020-2025
- **Computing**: Access to Oak Ridge National Laboratory Frontier (exascale), NREL Eagle (HPC), and NERSC resources
- **Collaborators**: NREL, Sandia National Laboratories, LLNL, Texas A&M University, University of Maine, DTU Wind Energy
- **Industry Partners**: Coordinating with floating offshore wind developers for validation case studies

## Software & Open Science

FLOWMAS builds on open-source computational frameworks:
- **Nalu-Wind**: Exascale-capable wind energy LES solver developed at Sandia National Laboratories
- **OpenFAST**: Wind turbine simulation tool integrating aerodynamics, structural dynamics, and controls
- **AMR-Wind**: Adaptive mesh refinement LES code for wind energy applications

Research outputs, validation datasets, and selected simulation results will be released as open-access resources accelerating offshore wind technology development.

## Project Status

FLOWMAS was terminated in 2025 as part of a shift in federal priorities and reorganization of the DOE Office of Energy Efficiency and Renewable Energy (EERE). Despite early termination, the project established foundational frameworks for multiscale data assimilation in complex coupled systems and demonstrated the feasibility of digital twins for offshore wind applications. The methodologies developed—particularly for variational data assimilation in strongly nonlinear systems and measurement system optimization—remain relevant for future wind energy research and other complex energy systems.

## Future Directions

Beyond initial project scope, FLOWMAS capabilities enable:
- **Wind Plant Scale**: Simulating arrays of floating turbines capturing collective dynamics and wake interactions
- **Extreme Events**: Predicting hurricane, typhoon, and extreme wave impacts with confidence
- **Digital Twins**: Real-time simulation frameworks for offshore wind farm operations and predictive maintenance
- **Multi-Use Platforms**: Extending simulations to co-located offshore wind, wave energy, and aquaculture systems

More information in the [press release](https://www.nlr.gov/news/detail/program/2023/nrel-will-lead-two-19m-research-centers-to-spur-decarbonization-efforts-as-part-of-does-energy-earthshots-initiative
).
