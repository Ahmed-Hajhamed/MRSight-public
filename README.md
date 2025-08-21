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
  <img width="1919" height="995" alt="fig  1" src="https://github.com/user-attachments/assets/5ed1f33b-e361-4f91-b9cc-22fb1422be4b" />

### Network Analysis View
- Complete Metabolite Graph
  <img width="1488" height="631" alt="fig 2" src="https://github.com/user-attachments/assets/eaae82b7-36f2-4be8-b604-51a4d104cda7" />
  
- Natural Visibility Graph
  <img width="1488" height="631" alt="fig  3" src="https://github.com/user-attachments/assets/f5c4a82e-5945-414a-9139-0fe2207c7ebd" />

- Horizontal Visibility Graph
  <img width="1501" height="634" alt="fig  4" src="https://github.com/user-attachments/assets/bf12604c-25d6-47b4-bf22-dcb18ca6bf74" />

### Comparative Analysis
  <img width="1919" height="990" alt="fig  5" src="https://github.com/user-attachments/assets/2ea8c638-6497-4e21-8685-fd4b4a31f26a" />


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
