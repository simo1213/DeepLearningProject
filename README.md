# Multi-Camera Vehicle Tracking (MCMT)
> **Disclaimer**  
> This repository is created **for academic study and research purposes only**.  
> The copyrights of the ELECTRICITY framework, Synthehicle dataset, CityFlow dataset, and other third-party resources remain with their original authors.


This repository presents a technical implementation and analysis of **Multi-Camera Multi-Target (MCMT) vehicle tracking** based on the **ELECTRICITY framework**, with a focus on **Vehicle Re-Identification (ReID)** and cross-camera identity association.

The project evaluates tracking performance across **synthetic** and **real-world** datasets and analyzes the **sim-to-real domain gap** in multi-camera tracking systems.

---

## What I Learned

- ✅ Built a complete **MCMT pipeline** including single-camera tracking and cross-camera association  
- ✅ Applied **graph-based energy minimization** for efficient tracklet association  
- ✅ Fine-tuned a **ResNet-101–based ReID model** using Triplet Loss (hard mining) and Cross-Entropy Loss  
- ✅ Preprocessed large-scale tracking datasets into image-level ReID training data  
- ✅ Evaluated tracking robustness using **IDF1, ID Precision (IDP), and ID Recall (IDR)**  

---

## Tech Stack

| Component | Technologies |
|---------|--------------|
| Detection | Mask R-CNN |
| Single-Camera Tracking | DeepSORT, Kalman Filter |
| Re-Identification | ResNet-101, Triplet Loss |
| Cross-Camera Tracking | ELECTRICITY (Energy Minimization) |
| Datasets | Synthehicle, CityFlow |
| Simulation | CARLA |
| Language | Python |

---

## Project Pipeline

The project follows a **two-stage experimental pipeline**:

1. **Baseline Evaluation**
   - Use the **pre-trained ELECTRICITY model**
   - Perform MCMT tracking on:
     - Synthehicle (synthetic dataset)
     - CityFlow (real-world dataset)
   - Evaluate tracking performance using IDF1, IDP, and IDR

2. **Model Fine-Tuning**
   - Fine-tune the ELECTRICITY ReID module separately on:
     - Synthehicle
     - CityFlow
   - Re-run MCMT tracking on both datasets
   - Compare results before and after fine-tuning to analyze:
     - Domain gap
     - Cross-camera identity consistency

---

## Datasets

### Synthehicle (Synthetic Dataset)

- Synthetic multi-camera vehicle tracking dataset generated using **CARLA**
- Provides perfectly annotated multi-camera trajectories
- Dataset generation code:
  - https://github.com/fubel/synthehicle
- Dataset download:
  - https://github.com/fubel/synthehicle/wiki/Download

---

### CityFlow (Real-World Dataset)

- Large-scale real-world urban traffic dataset
- Collected from city surveillance cameras with challenging lighting and occlusion
- We use **Track 1: City-Scale Multi-Camera Vehicle Tracking**
- Dataset and evaluation:
  - https://www.aicitychallenge.org/2022-data-and-evaluation/

---

## Experiments & Evaluation

- Conducted experiments on both **synthetic** and **real-world** datasets
- Evaluated performance using standard **MTMCT metrics**:
  - IDF1
  - ID Precision (IDP)
  - ID Recall (IDR)
- Analyzed performance degradation caused by:
  - Domain shift (synthetic → real)
  - Night-time conditions
  - Viewpoint and appearance variation across cameras

---

## Results Summary

- Synthetic data enables stable ReID training with high identity consistency  
- Fine-tuned models show limited generalization to real-world scenes  
- **IDF1** is the most reliable metric for evaluating global identity consistency in MCMT systems  

---

## Report

📄 Full technical details, loss formulation, and experimental analysis are documented in **`report.pdf`**.
