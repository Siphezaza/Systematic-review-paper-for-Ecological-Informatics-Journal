# Inclusion and Exclusion Criteria

## Inclusion
A study was included if it:
- was published between 2000 and 2026, **and**
- discussed Graph Theory (GT), Graph Neural Networks (GNNs), Reinforcement
  Learning (RL), or a hybrid combination of these, **in a marine ecology
  context**.

## Exclusion
A study was excluded if it:
- focused only on terrestrial or freshwater systems without marine relevance,
- did not discuss GT, GNNs, or RL in a marine context,
- was written in a language other than English, or
- was a shortened or earlier version of another retrieved publication.

## Quality assessment (full-text stage)
Each full-text study was additionally checked for:
- clearly defined objectives,
- appropriate application of the GT / GNN / RL method,
- reproducibility of results.

Studies lacking methodological transparency or ecological validation were
excluded.

---

## How to use `inclusion_exclusion_decisions.csv`
The CSV is a per-record decision log. One row per screened record.

- **Stage** — `TitleAbstract` or `FullText`
- **Decision** — `Include` or `Exclude`
- **Method** — GT / GNN / RL / Hybrid (for included studies)
- **ExclusionReason** — required when Decision = `Exclude`; use one of the
  reasons listed above (e.g. "Outside scope", "Missing full text",
  "Other methodological reasons", "Non-English", "Duplicate/earlier version").

Populate this file from your Web of Science / Scopus / Google Scholar
screening spreadsheets so the 1832 → 122 funnel in Figure 5 can be traced
record by record.
