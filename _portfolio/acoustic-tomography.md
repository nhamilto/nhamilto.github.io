---
title: "Acoustic Tomography for Wind Energy"
excerpt: "Principle Investigator developing sensing technology that reconstructs three-dimensional atmospheric wind and temperature fields from sound propagation<br/><img src='/images/acoustic-thumb.png' width='600'>"
collection: portfolio
---

## Technology Overview

Acoustic tomography reconstructs volumetric wind and temperature fields by analyzing sound propagation through the atmosphere. Unlike conventional point measurements or line-of-sight remote sensing, this approach provides three-dimensional characterization of turbulent flows. I've been developing and deploying these systems for wind energy applications, where they capture flow structures that are difficult to measure with traditional instruments.

## How It Works

Acoustic tomography exploits the physics of sound propagation:
- **Sound Speed Variation**: Acoustic travel time depends on wind velocity and temperature along the propagation path
- **Multiple Paths**: Arrays of speakers and microphones create intersecting acoustic paths through the measurement volume
- **Inverse Problem**: Advanced algorithms reconstruct 3D wind and temperature fields from travel time measurements
- **High Temporal Resolution**: 1-10 Hz sampling captures turbulent fluctuations at scales critical for wind turbine interactions

## Technical Innovations

My research has advanced acoustic tomography capabilities:

### System Design
- **Scalable Arrays**: Designed deployable systems spanning 100-500m measurement volumes appropriate for wind turbine rotor planes
- **Weather Hardening**: Developed ruggedized hardware surviving months-long field campaigns in harsh wind plant environments
- **Signal Processing**: Implemented noise filtering, echo cancellation, and adaptive algorithms enabling operation in turbulent flows

### Reconstruction Algorithms
- **Regularization Methods**: Applied Tikhonov regularization, L1-norm minimization, and Bayesian approaches balancing resolution and noise sensitivity
- **Modal Decomposition**: Integrated proper orthogonal decomposition (POD) and dynamic mode decomposition (DMD) to extract coherent flow structures
- **Uncertainty Quantification**: Developed Monte Carlo and ensemble methods characterizing reconstruction confidence

### Wind Energy Applications
- **Wake Characterization**: Captured three-dimensional wake structure revealing meandering dynamics and turbulence evolution
- **Inflow Monitoring**: Provided real-time atmospheric condition measurements for turbine control and power forecasting
- **Model Validation**: Generated volumetric datasets for validating large eddy simulation and wind plant models

## Field Campaign Deployments

I've deployed acoustic tomography systems in multiple major campaigns:
- **AWAKEN**: Dual-array deployment capturing wake-atmosphere interactions
- **RAAW**: Rotor-plane measurements revealing inflow heterogeneity and wake formation
- **SWiFT**: Development and validation testbed at Sandia wind energy facilities
- **M5 Tower**: Atmospheric boundary layer characterization at NREL's Colorado site

## Impact & Applications

Acoustic tomography has enabled new measurements of turbulent processes in wind energy environments:
- Volumetric wake structure revealing meandering dynamics and turbulence evolution
- Real-time atmospheric condition monitoring for turbine control and power forecasting
- Validation datasets for large eddy simulation and wind plant models

This work has supported 15+ peer-reviewed publications and collaborations with DTU Wind Energy, TU Delft, and other wind energy research institutions. The technology has been deployed in multiple field campaigns including AWAKEN, RAAW, SWiFT, and M5 Tower measurements.

## Technical Challenges Overcome

Deploying acoustic tomography in wind energy required solving hard problems:
1. **Environmental Noise**: Wind turbine operation, ambient weather, and wildlife create acoustic interference requiring sophisticated filtering
2. **Atmospheric Variability**: Temperature gradients, humidity, and pressure variations affect sound propagation, demanding real-time calibration
3. **Scale**: Wind energy applications require 100m+ measurement volumes, pushing acoustic tomography to unprecedented scales
4. **Data Volume**: High sampling rates and large arrays generate TB-scale datasets requiring efficient processing pipelines

## Current Research Directions

Ongoing work advances acoustic tomography capabilities:
- **Machine Learning Integration**: Using physics-informed neural networks to improve reconstruction from sparse measurements
- **Multi-Modal Fusion**: Combining acoustic tomography with lidar, sodar, and tower data for comprehensive atmospheric characterization
- **Real-Time Implementation**: Developing edge computing solutions enabling on-site reconstruction for turbine control applications
- **Advanced Configurations**: Exploring 3D arrays, passive acoustic sensing, and distributed acoustic sensing (DAS) integration

## Publications & Software

See [Publications](/publications/) for acoustic tomography research outputs. Open-source reconstruction algorithms and field campaign datasets available upon request for collaborative research.

