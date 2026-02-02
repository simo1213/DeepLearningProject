# Multi-Camera Vehicle Tracking (MCMT)

This repository presents a technical implementation and analysis of **Multi-Camera Multi-Target (MCMT) vehicle tracking** based on the **ELECTRICITY framework**, with an emphasis on **Vehicle Re-Identification (ReID)** and cross-camera identity association.

The project evaluates model performance across **synthetic** and **real-world** datasets and analyzes the **sim-to-real domain gap** in multi-camera tracking systems.

---

## What I Learned

- ✅ Built a complete **MCMT pipeline** including single-camera tracking and cross-camera association  
- ✅ Applied **graph-based energy minimization** for efficient tracklet association  
- ✅ Fine-tuned a **ResNet-101 ReID model** using Triplet Loss (hard mining) and Cross-Entropy Loss  
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

## Project Scope

This project demonstrates:

- 🚗 Vehicle detection and tracklet generation in single-camera views  
- 🔗 Cross-camera ReID and global identity assignment  
- 🌍 Sim-to-real transfer evaluation using synthetic and real traffic data  
- 📊 Quantitative analysis under challenging conditions (night, occlusion, viewpoint variation)

---

## Experiments & Evaluation

- Trained ReID models on **Synthehicle (synthetic)** and **CityFlow (real-world)** datasets  
- Compared tracking performance across domains using standard MTMCT metrics  
- Observed significant performance degradation when transferring from synthetic to real data

---

## Results Summary

- Synthetic data enables stable ReID training with high identity consistency  
- Real-world MCMT remains challenging due to appearance variation and environmental noise  
- **IDF1** is the most reliable metric for evaluating global identity consistency across cameras

---

## Report

📄 Full technical details, model formulation, and experimental analysis are provided in **`report.pdf`**.
