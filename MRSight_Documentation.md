# MRSight Documentation

## Overview

MRSight is a powerful MRS (Magnetic Resonance Spectroscopy) data visualization and analysis tool developed as a submission to the BioVis+ 2025 challenge at IEEE Vis 2025. The tool employs innovative graph network analysis techniques to provide researchers and clinicians with intuitive ways to explore metabolite relationships and compare subject data.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Subject Selection](#subject-selection)
4. [Graph Types](#graph-types)
5. [Metabolite Selection](#metabolite-selection)
6. [Metadata Display](#metadata-display)
7. [Graph Features](#graph-features)
8. [Network Graph Interaction](#network-graph-interaction)
9. [Focus Mode](#focus-mode)
10. [Comparison Mode](#comparison-mode)
11. [Spectrum Visualization](#spectrum-visualization)
12. [Team Members and Supervision](#team-members-and-supervision)
13. [Contact & Support](#contact--support)

## Getting Started

1. Get the latest release from the [MRSight GitHub repository](https://github.com/Ahmed-Hajhamed/MRSight-public)
2. Run MRSight.py
3. Select a primary subject to begin analysis
4. Choose which metabolites to visualize
5. Select a graph type for visualization

## Interface Overview

The MRSight interface consists of two primary sections:
1. **Controls Panel** (left side) - Contains all configuration options
2. **Visualization Area** (right side) - Displays the network graph and spectrum

### Controls Panel

The Controls Panel provides options for:
- Subject selection
- Graph type selection
- Metabolite selection
- Metadata display options
- Graph features display

### Visualization Area

The Visualization Area consists of:
- Network Graph (top) - Interactive graph visualization
- Spectrum View (bottom) - Traditional MRS spectrum display

## Subject Selection

Located at the top of the Controls Panel:

1. **Primary Subject Selection**
   - Use the dropdown combobox to select the main subject for analysis
   - Data for this subject will be displayed in the primary color scheme

2. **Comparison Subject Selection**
   - Check the "Enable Comparison" checkbox to activate this feature
   - Use the dropdown to select a second subject
   - Comparison subject data will be displayed in a contrasting color scheme (white)

## Graph Types

MRSight supports three different graph visualization methods, selectable via the dropdown combobox:

1. **Complete Metabolite Graph**
   - Every metabolite node connects to all other metabolite nodes
   - Each node has 13 edges (connections to other metabolites)
   - Edge properties represent relationships between metabolites

2. **Natural Visibility Graph**
   - Connects two nodes if there's a direct line of sight between them.
   - Provides a more selective view of metabolite relationships

3. **Horizontal Visibility Graph**
   - Connects two nodes if there's a horizontal line of sight between them, starting from higher shift metabolites to lower ones.
   - Shows different relationship patterns compared to other graph types

## Metabolite Selection

- The metabolite selection area contains two columns of 14 checkboxes
- Each checkbox corresponds to a specific metabolite (e.g., PCr, NAD+, Pi)
- Check/uncheck boxes to show/hide specific metabolites in the graph visualization
- The legend on the top right of the graph updates dynamically to reflect selected metabolites

## Metadata Display

Enable the "Show Metadata on Hover" checkbox to display detailed information when hovering over nodes:

### Node Metadata Includes:
- Intensity value
- Ratio to PCr
- Graph local features:
  - Strength
  - Betweenness centrality
  - Clustering coefficient
  - Node efficiency
  - Assortativity coefficient

## Graph Features

The text display at the bottom of the Controls Panel shows global graph metrics:

### Global Features Displayed:
- Global efficiency
- Path length
- Transitivity
- Average local efficiency
- Average betweenness centrality

When comparison mode is enabled, these metrics are shown for both the primary and comparison subjects.

## Network Graph Interaction

The network graph at the top right of the interface offers several interactive features:

### Edge Interactions:
- **Hover over edge**: Displays direction (e.g., PCr → PE) and ratio value
- **Double-click edge**: Toggles transparency to hide/show the edge
- **Single-click edge**: Flips the direction and ratio of the edge

### Visual Elements:
- **Nodes**: Represent individual metabolites
- **Edges**: 
  - Connect metabolites
  - Thickness and transparency represents ratio magnitude
  - Arrows point to the denominator in the ratio

## Focus Mode

Focus mode allows detailed examination of a single metabolite's relationships:

1. **Activation**: Double-click on any node in the network graph
2. **Display**: Only edges connected to the selected node are shown
3. **Deactivation**: Double-click on the selected node again

## Comparison Mode

When comparison mode is enabled:

1. Both primary and comparison subject data are visualized
2. Primary subject nodes use the standard color scheme
3. Comparison subject nodes appear in white
4. Focus mode enables direct comparison between the same metabolite across subjects
5. Global graph features for both subjects are displayed in the text panel

## Spectrum Visualization

The bottom right area displays the traditional MRS spectrum:

- X-axis: Chemical shift (ppm)
- Y-axis: Signal intensity
- The spectrum updates based on the selected primary subject
- When comparison mode is active, both spectra are overlaid with different colors

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

## Contact & Support

For questions, feature requests, or bug reports:

- **GitHub Repository**: [github.com/Ahmed-Hajhamed/MRSight](https://github.com/Ahmed-Hajhamed/MRSight-public)
- **Email Support**: ahmed.hajhamed03@eng-st.cu.edu.eg

---

*MRSight was developed as a submission to the BioVis+ 2025 challenge at IEEE Vis 2025.*