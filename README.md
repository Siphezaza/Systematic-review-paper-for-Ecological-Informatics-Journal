> 📋 Code and data accompanying a systematic review paper

# Graph Theory, Graph Neural Networks, and Reinforcement Learning in Marine Ecology

This repository is the official supplementary material for *Graph Theory, Graph Neural
Networks, and Reinforcement Learning in marine ecology: A systematic review of
methodologies, theoretical rigour, and future directions*.

The purpose of this repository is not only to release code, but to guide readers
step-by-step through the complete workflow of a systematic review: how the literature
was searched, how studies were screened, how their theoretical rigour was scored, and
how the quantitative results and figures in the paper were produced.

This README is intentionally written as an extended tutorial so that users can
reproduce, understand, and adapt the methodology to their own reviews.

## 1. What Does This Repository Provide?

Systematic reviews are expected to be reproducible: another researcher should be able to
repeat the search, see why each study was kept or dropped, and check how conclusions were
reached. To support this, the repository provides:

- The exact **PRISMA search strings** used in each database
- The **inclusion/exclusion criteria** and a per-record **decision log**
- The six-dimension **theoretical rigour scoring rubric**, with per-study justifications
  in the supplementary PDF
- The **analysis code** that reproduces the inter-rater reliability statistics and the
  bibliometric figures reported in the paper

Rather than releasing raw scripts alone, each component is documented and linked back to
the specific table or figure it supports.

## 2. Overview of the Workflow

The review followed the PRISMA framework across four stages:

- Search three databases (Web of Science, Scopus, Google Scholar), 2000–2026
- Remove duplicates and screen records by title and abstract
- Assess full texts against inclusion/exclusion criteria (1832 → 122 studies)
- Extract data and score each study for theoretical rigour across six dimensions

Each stage is documented explicitly in the folders described below.

Quick Start
-----------
For users who want to reproduce the main quantitative results with minimal setup:

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Reproduce the inter-rater reliability results** (Table 5 and Figure 12)
   Place the paired scores in `scoring/paired_scores.csv` (see `scoring/README.md` for
   the exact column format), then run:
   ```
   cd scoring
   python ../code/inter_rater_reliability.py
   ```
   This reproduces the weighted Cohen's kappa of **0.753** (substantial agreement) and
   **81.1%** exact agreement across all 732 individual ratings, and saves both figures.

3. **Reproduce the bibliometric figures** (Figures 9 and 10b)
   ```
   python code/bibliometric_analysis.py
   ```
   The keyword word cloud runs directly. The affiliation map additionally requires
   `studies_affiliation.xlsx` with columns `AffiliationLon`, `AffiliationLat`, `Method`.

Each script is commented and explicitly linked to the corresponding sections of the
paper, enabling both reproducibility and methodological transparency.

## Repository Structure

The repository is organised to support both full reproducibility of the paper's results
and easy adaptation to new systematic reviews.

```
.
├── README.md                                  Extended tutorial-style documentation
├── requirements.txt                           Python dependencies
├── LICENSE
│
├── prisma/
│   ├── search_strings.md                      Exact database queries + PRISMA funnel counts (Fig 5)
│   ├── inclusion_exclusion_criteria.md        Criteria and how to read the decision log
│   └── inclusion_exclusion_decisions.csv      Per-record screening decisions (1832 → 122)
│
├── scoring/
│   ├── README.md                              Scoring rubric + inter-rater instructions
│   └── paired_scores_TEMPLATE.csv             Column template for the kappa script
│
├── code/
│   ├── inter_rater_reliability.py             Cohen's kappa + concordance matrix (Table 5, Fig 12)
│   ├── bibliometric_analysis.py               Word cloud (Fig 10b) + affiliation map (Fig 9)
│   └── full_analysis_notebook.py              Full project notebook (all figures, reference)
│
└── supplementary/
    ├── README.md
    └── supplementary_materials.pdf            ← add: per-study scores + justifications
```

## 3. Requirements

This code was developed in a Google Colab environment with Python 3. Key libraries include:

- numpy, pandas, scipy
- scikit-learn (for Cohen's kappa)
- matplotlib, seaborn (for figures)
- wordcloud (for the keyword word cloud, Figure 10b)
- geopandas (for the affiliation map, Figure 9)
- graphviz, openpyxl

To install, run:
```
pip install -r requirements.txt
```

**Tested environment:**

- Google Colab (recommended, handles all dependencies out of the box)
- Also runs locally on Windows/Linux with Python 3.10+

## 4. Step-by-Step Guide

### Step 1: Literature Search

The exact queries for each database are in `prisma/search_strings.md`, together with the
field settings used (Web of Science `ALL`; Scopus `TITLE-ABS-KEY`; Google Scholar
full-text), the year range (2000–2026), and the number of records each database returned.
The same file records the full PRISMA funnel that produced Figure 5:

| Stage | Count |
|---|---|
| Identified (WoS 56 + Scopus 782 + Google Scholar 994) | 1832 |
| Duplicates removed | 368 |
| Screened (title & abstract) | 1464 |
| Full-text assessed | 210 |
| **Included in review** | **122** |

### Step 2: Screening Decisions

`prisma/inclusion_exclusion_criteria.md` lists the rules used to keep or drop a study.
`prisma/inclusion_exclusion_decisions.csv` is a per-record log: one row per screened
record, with the stage, the decision, the assigned method (GT / GNN / RL / Hybrid), and,
for excluded records, the exclusion reason.

### Step 3: Theoretical Rigour Scoring

Each of the 122 included studies was scored on six dimensions (ecological relevance,
theoretical foundations, uncertainty quantification, scalability, stakeholder utility,
interpretability), each on a 0–3 scale. The generic rubric is in `scoring/README.md`
(and Table 4 of the paper); the **per-study scores and written justifications** are in
`supplementary/supplementary_materials.pdf`.

### Step 4: Inter-Rater Reliability

Two raters independently scored all 122 studies. `code/inter_rater_reliability.py`
computes, per dimension and overall: weighted and unweighted Cohen's kappa, percent
agreement, mean absolute difference, and Spearman's correlation, and produces the score
concordance matrix (Figure 12).

**Example (loading paired scores):**
```python
import pandas as pd
from sklearn.metrics import cohen_kappa_score

df = pd.read_csv("paired_scores.csv")
kappa_w = cohen_kappa_score(df["Zaza_Eco"], df["Nicole_Eco"], weights="quadratic")
print(f"Ecological Relevance weighted kappa: {kappa_w:.3f}")
```

### Step 5: Bibliometric Analysis

`code/bibliometric_analysis.py` reproduces the keyword word cloud (Figure 10b) from the
author keywords of the included studies, and the geographic distribution of first-author
affiliations by method (Figure 9).

## Results (Inter-Rater Reliability)

The table below reports the agreement between the two raters across the six scoring
dimensions, as computed by `code/inter_rater_reliability.py` and reported in Table 5.

| Dimension | Weighted κ | Agreement (%) | Level |
|---|---|---|---|
| Ecological Relevance | 0.665 | 83.6 | Substantial |
| Theoretical Foundations | 0.539 | 84.4 | Moderate |
| Uncertainty Quantification | 0.642 | 77.0 | Substantial |
| Scalability | 0.735 | 85.2 | Substantial |
| Stakeholder Utility | 0.636 | 78.7 | Substantial |
| Interpretability | 0.442 | 77.9 | Moderate |
| **Overall** | **0.753** | **81.1** | **Substantial** |

## Adapting the Code to Other Reviews

Although demonstrated for a review of GT, GNNs, and RL in marine ecology, this workflow
is transferable to other systematic reviews. Users may need to adjust:

- The search strings and databases
- The inclusion/exclusion criteria
- The scoring dimensions and rubric

The overall pipeline (search → screen → score → check agreement → visualise) remains
unchanged.

## Data Availability

The full PRISMA search strings, inclusion/exclusion decisions, scoring rubric with
per-study justifications, and bibliometric analysis code are provided in this repository.
The list of the 122 included studies is given in the reference list of the paper. This
ensures full reproducibility of the search, screening, and scoring processes.

## Citation

If you use this code or the scoring framework, please cite:
```
@article{yourkey2026marine,
  title={Graph Theory, Graph Neural Networks, and Reinforcement Learning in marine ecology:
         A systematic review of methodologies, theoretical rigour, and future directions},
  author={<Your Name and Co-authors>},
  journal={<Journal / preprint>},
  year={2026}
}
```
