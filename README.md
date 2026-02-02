Multi-Camera Vehicle Tracking

This repository presents a technical study and implementation of Multi-Camera Multi-Target (MCMT) vehicle tracking based on the ELECTRICITY framework, with a primary focus on Vehicle Re-Identification (ReID) and cross-camera identity association.

The project evaluates tracking performance across synthetic and real-world environments and analyzes the domain gap between simulation and real traffic scenes.


What I Learned

✅ Designed a full MCMT tracking pipeline including single-camera tracking and cross-camera association
✅ Implemented graph-based tracklet association using energy minimization
✅ Fine-tuned a ResNet-101–based ReID model with Triplet Loss and Cross-Entropy Loss
✅ Built ReID training datasets by preprocessing large-scale tracking benchmarks
✅ Evaluated system robustness using IDF1, ID Precision (IDP), and ID Recall (IDR)
