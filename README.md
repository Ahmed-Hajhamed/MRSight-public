# MRSight - Magnetic Resonance Spectroscopy Visualization Tool

<p align="center">
  <img width="300" height="300" alt="MRSight_Logo" src="https://github.com/user-attachments/assets/f0eeea66-be89-497b-8651-4515e405dd93" />
</p>

## Overview
MRSight is a specialized visualization and analysis tool for Magnetic Resonance Spectroscopy (MRS) data, developed as a submission for the Bio+MedVis Challenge @ IEEE VIS 2025. The tool leverages graph network analysis to provide researchers and clinicians with novel ways to visualize and analyze complex MRS data relationships.

## Key Features

### Interactive Subject Comparison
- Select primary subjects for analysis
- Optional comparative analysis with secondary subjects
- Side-by-side visualization for immediate comparison

### Advanced Graph Network Visualization
- Multiple graph type options:
    - Complete Metabolite Graph
    - Natural Visibility Graph
    - Horizontal Visibility Graph
- Customizable metabolite selection (14 metabolites available)
- Interactive node and edge manipulation
- Focus mode for targeted analysis

### Comprehensive Metabolite Analysis
- Detailed metabolite metadata on hover:
    - Intensity values
    - PCr ratios
    - Graph network metrics
- Local node features:
    - Strength
    - Betweenness centrality
    - Clustering coefficient
    - Node efficiency
    - Assortativity coefficient

### Global Network Analysis
- Quantitative comparison of network properties:
    - Global efficiency
    - Path length
    - Transitivity
    - Average local efficiency
    - Average betweenness centrality

### Dual Visualization Interface
- Network graph representation (top)
- Traditional spectrum visualization (bottom)
- Interactive legend with dynamic updates

## Screenshots
### Main Interface
<img width="1920" height="991" alt="Python 3 11 8_17_2025 6_33_31 PM" src="https://github.com/user-attachments/assets/10ef1e43-c696-4d0e-aa81-669f2122c5ea" />

### Network Analysis View
<img width="1920" height="991" alt="Python 3 11 8_17_2025 6_34_28 PM" src="https://github.com/user-attachments/assets/986517c0-5546-4aac-8030-b134513b1981" />

### Comparative Analysis
<img width="1920" height="991" alt="Python 3 11 8_18_2025 3_05_27 PM" src="https://github.com/user-attachments/assets/07d496f2-b90b-45ac-a36a-ab3a58c3eef3" />

## Installation
```bash
git clone https://github.com/Ahmed-Hajhamed/MRSight-public.git
cd MRSight-public
```

## Usage
```bash
# Launch MRSight
python MRSight.py
```

## BioVis+ Challenge Submission
This tool was developed as a submission for the Bio+MedVis Challenge @ IEEE VIS 2025, focusing on novel approaches to biomedical data visualization through network analysis.

## Team Members and Supervision

### Team Members
- Ahmed Hajhamed
- Ammar Yassir
- Ziad Wael
- Muhamed Ahmed

### Supervision
- Prof. Muhammad Rushdi - Supervisor
   Department of Biomedical Engineering and Systems 
   Faculty of Engineering, Cairo University

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or support, please contact us at Ahmed.Hajhamed03@eng-st.cu.edu.eg, connect on [LinkedIn](https://www.linkedin.com/in/ahmed-hajhamed/), or create an [issue](https://github.com/Ahmed-Hajhamed/MRSight-public/issues).
