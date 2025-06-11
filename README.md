# Functional Connectome in Obsessive-Compulsive Disorder

Code repository for the ENIGMA-OCD consortium study on resting-state functional connectivity analysis and machine learning classification.

## 📄 Publication

**"The functional connectome in obsessive-compulsive disorder: resting-state mega-analysis and machine learning classification for the ENIGMA-OCD consortium study"**

*Molecular Psychiatry* (2023) 28:4307-4319  
DOI: [10.1038/s41380-023-02077-0](https://doi.org/10.1038/s41380-023-02077-0)  
PubMed: [37131072](https://pubmed.ncbi.nlm.nih.gov/37131072/)

## 🔧 Requirements

### Software
- Python 3.9.5
- R (for linear mixed-effects models)

### Python Packages
- `pymer4` (v0.8.1) - Python to R interface for linear mixed-effects models
- `scikit-learn` (v1.0.20) - Machine learning framework
- Standard scientific Python stack (numpy, pandas, matplotlib, etc.)

### R Packages
- `lme4` (v1.1.21) - Linear mixed-effects models
- `lmerTest` (v3.1.3) - Statistical tests for mixed-effects models

## 📋 Installation

1. Clone this repository:
```bash
git clone https://github.com/WillemB2104/Bruin-2023-MP.git
cd Bruin-2023-MP
```

2. Install Python dependencies (separate environments for univariate and multivariate analyses):
```bash
pip install -r requirements_univariate.txt
pip install -r requirements_multivariate.txt
```

3. Install pymer4 following the [official installation guide](https://eshinjolly.com/pymer4/pages/installation.html)

4. Install R packages:
```r
install.packages(c("lme4", "lmerTest"))
```

## 📊 Analysis Pipeline

The analysis consists of three main notebooks that should be run in sequence:

### 1. Data Preprocessing (`1_parse_halfpipe_outputs.ipynb`)
- Parses HALFPIPE rs-fMRI preprocessing outputs
- Performs quality control checks
- Extracts functional connectivity features

### 2. Univariate Analysis (`2_run_univariate_analyses_with_lme4.ipynb`)
- Implements linear mixed-effects models with random effects
- Tests group differences in resting-state fMRI features
- Generates statistical summaries and effect size visualizations (brain maps for voxel-wise features)
- Produces circular connectome plots for effect sizes on functional connectivity

### 3. Multivariate Classification (`3_run_multivariate_classifications.ipynb`)
- Performs machine learning classification using scikit-learn
- Includes case-control and within-patient comparisons
- Evaluates the influence of ComBat harmonization on site effects

## 🗂️ Accessing ENIGMA-OCD Data

We are happy to welcome new cohorts at any time! If you would like to receive more information and/or are willing to participate in this initiative by sharing your data, please contact:

- **Prof. dr. Odile van den Heuvel**: oa.vandenheuvel@amsterdamumc.nl
- **Prof. dr. Dan Stein**: dan.stein@uct.ac.za

For more information, visit: https://enigma.ini.usc.edu/ongoing/enigma-ocd-working-group/

## 🤝 Contributing

If you use this code in your research, please cite our paper:

```bibtex
@article{ocd_connectome_2023,
  title={The functional connectome in obsessive-compulsive disorder: resting-state mega-analysis and machine learning classification for the ENIGMA-OCD consortium study},
  journal={Molecular Psychiatry},
  volume={28},
  pages={4307--4319},
  year={2023},
  doi={10.1038/s41380-023-02077-0}
}
```
