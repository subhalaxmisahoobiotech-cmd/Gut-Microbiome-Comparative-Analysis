# NGS-Based Gut Microbiome Comparative Analysis

## Project Overview

This project focuses on the comparative analysis of gut microbial composition among individuals with Crohn's Disease (CD), Ulcerative Colitis (UC), and Non-Inflammatory Bowel Disease (Non-IBD) controls using publicly available metagenomic data from the Human Microbiome Project 2 (HMP2/iHMP).

The study investigates differences in gut microbial composition at the phylum level and evaluates whether microbial abundance varies significantly among the three participant groups.

## Objectives

- To obtain and organize publicly available gut metagenomic data.
- To identify and match metagenomic sequencing runs with participant metadata.
- To organize participants into CD, UC, and Non-IBD groups.
- To compare gut microbial abundance at the phylum level.
- To perform statistical analysis using the Kruskal-Wallis test.
- To apply False Discovery Rate (FDR) correction for multiple comparisons.
- To visualize microbial abundance patterns across the study groups.

## Dataset Information

The data used in this project were obtained from the Human Microbiome Project 2 (HMP2/iHMP).

**Data sources:**
- Project: Human Microbiome Project 2 (HMP2/iHMP)
- MGnify Study Accession: MGYS00002301
- SRA Study Accession: SRP115812
- BioProject Accession: PRJNA389280

**Study population:**

A total of 362 matched metagenomic sequencing runs representing 117 participants were included.

| Clinical group | Number of participants |
|---|---:|
| Crohn's Disease (CD) | 59 |
| Ulcerative Colitis (UC) | 34 |
| Non-IBD controls | 24 |
| **Total** | **117** |

## Methodology

### 1. Data Collection

Publicly available metagenomic data and associated participant metadata were obtained from the HMP2/iHMP project.

### 2. Data Organization and Participant Matching

Sequencing run information was organized and matched with participant metadata to establish the relationship between metagenomic samples and their corresponding clinical groups.

A total of 362 matched sequencing runs were retained for the analysis.

### 3. Group Classification

Participants were categorized into three groups:

- Crohn's Disease (CD)
- Ulcerative Colitis (UC)
- Non-IBD controls

### 4. Microbial Abundance Analysis

Microbial abundance was examined at the phylum level. Participant-level abundance data were used to compare the distribution of major bacterial phyla across the three clinical groups.

### 5. Statistical Analysis

The Kruskal-Wallis test was performed to evaluate differences in phylum-level microbial abundance among the three groups.

False Discovery Rate (FDR) correction was applied to account for multiple statistical comparisons.

A significance threshold of adjusted p-value < 0.05 was used.

### 6. Data Visualization

Graphs were generated using Python to visualize phylum-level microbial abundance patterns and facilitate comparisons among the clinical groups.

## Tools and Technologies

- **Python:** Data processing and statistical analysis
- **Pandas:** Data manipulation and organization
- **NumPy:** Numerical operations
- **SciPy:** Kruskal-Wallis statistical testing
- **Statsmodels:** FDR correction
- **Matplotlib:** Data visualization
- **Jupyter / Python scripts:** Analysis workflow

## Results

- A total of 362 matched metagenomic sequencing runs were analyzed.
- The dataset represented 117 participants across three clinical groups.
- Phylum-level microbial abundance was compared among CD, UC, and Non-IBD groups.
- The Kruskal-Wallis test was performed with FDR correction.
- No statistically significant phylum-level differences were identified after FDR correction at the 0.05 significance threshold.

## Conclusion

This project demonstrates a computational workflow for comparative gut microbiome analysis using publicly available metagenomic data.

The analysis provided an overview of phylum-level microbial abundance patterns among Crohn's Disease, Ulcerative Colitis, and Non-IBD participants.

Although differences in microbial abundance were observed, none of the tested phylum-level comparisons remained statistically significant after FDR correction.

The project provided practical experience in metagenomic data organization, participant metadata matching, statistical analysis, and biological data visualization.

## Repository Structure

```text
Gut-Microbiome-Comparative-Analysis/
│
├── 01_Data/
│
├── 02_Analysis/
│
├── 03_Results/
│
├── 04_Graphs/
│
├── Gut_Microbiome_Comparative_Analysis_Project_Report.docx
│
├── plot_phylum_comparison.py
│
└── README.md
```

## Project Type

Independent Bioinformatics Mini-Project

**Field:** NGS, Metagenomics, Gut Microbiome, Comparative Analysis, Statistical Bioinformatics

## Author

**Subhalaxmi Sahoo**

M.Sc. Bioinformatics

