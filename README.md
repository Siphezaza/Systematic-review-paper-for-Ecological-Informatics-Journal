# Supplementary Code and Data — Systematic Review of GT, GNNs, and RL in Marine Ecology

This repository supports reproducibility for the systematic review
*"Graph Theory, Graph Neural Networks, and Reinforcement Learning in marine
ecology: A systematic review of methodologies, theoretical rigour, and future
directions."*

It contains the PRISMA search strings, the inclusion/exclusion decision log,
the theoretical-rigour scoring rubric with per-study justifications, and the
analysis code used to produce the review's quantitative results and figures.

## Repository structure

```
.
├── README.md
├── requirements.txt
├── prisma/
│   ├── search_strings.md                    # Exact database queries (WoS, Scopus, Google Scholar)
│   ├── inclusion_exclusion_criteria.md      # Criteria + how to read the decision log
│   └── inclusion_exclusion_decisions.csv    # Per-record screening decisions (1832 -> 122)
├── scoring/
│   ├── README.md                            # Rubric + inter-rater reliability instructions
│   └── paired_scores_TEMPLATE.csv           # Column template for the kappa script
├── code/
│   ├── inter_rater_reliability.py           # Cohen's kappa + concordance matrix (Table 5, Fig 12)
│   ├── bibliometric_analysis.py             # Word cloud (Fig 10b) + affiliation map (Fig 9)
│   └── full_analysis_notebook.py            # Full project notebook (all figures, reference)
└── supplementary/
    ├── README.md
    └── supplementary_materials.pdf          # <- add: per-study scores + justifications
```

## Reproducing the main results

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. **Inter-rater reliability (Table 5, Figure 12).**
   Put the real paired scores in `scoring/paired_scores.csv` (see
   `scoring/README.md` for the format), then:
   ```
   cd scoring
   python ../code/inter_rater_reliability.py
   ```
   Expected: overall weighted kappa = 0.753, 81.1% exact agreement over 732
   ratings.

3. **Bibliometric figures (Figures 9 and 10b).**
   ```
   python code/bibliometric_analysis.py
   ```
   The affiliation map needs `studies_affiliation.xlsx` with columns
   `AffiliationLon`, `AffiliationLat`, `Method`.

## What maps to what in the paper

| Paper element | File |
|---|---|
| Search strings / databases | `prisma/search_strings.md` |
| PRISMA flow counts (Figure 5) | `prisma/search_strings.md` (totals table) |
| Inclusion/exclusion criteria | `prisma/inclusion_exclusion_criteria.md` |
| Screening decisions | `prisma/inclusion_exclusion_decisions.csv` |
| Scoring rubric (Table 4) | `scoring/README.md` + supplementary PDF |
| Per-study scores + justifications | `supplementary/supplementary_materials.pdf` |
| Inter-rater stats (Table 5) | `code/inter_rater_reliability.py` |
| Score concordance matrix (Figure 12) | `code/inter_rater_reliability.py` |
| Word cloud (Figure 10b) | `code/bibliometric_analysis.py` |
| Affiliation map (Figure 9) | `code/bibliometric_analysis.py` |

## Citation
If you use this material, please cite the associated paper. See `LICENSE` for
reuse terms.
