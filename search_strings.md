# PRISMA Search Strings

This document records the exact database queries used for the systematic
review, so the search can be reproduced.

- **Databases:** Web of Science, Scopus, Google Scholar
- **Date range:** 2000–2026
- **Language:** English only
- **Search concepts (combined with Boolean AND / OR):**
  - Methods: "reinforcement learning" OR "graph theory" OR "graph neural networks"
  - Domain: "marine ecology"

> Note: adjust the exact strings below to match what was actually run in each
> database. The templates reflect the field settings described in the
> Methodology section. Record the run date and the number of hits returned by
> each query for a complete audit trail.

---

## Web of Science
Field tag: `ALL =` (topic search — covers titles, abstracts, author keywords, and Keywords Plus).

```
ALL=(("reinforcement learning" OR "graph theory" OR "graph neural networks") AND "marine ecology")
```

Filters applied: Publication years 2000–2026; Language = English.

- Records returned: **56**
- Date run: __________

---

## Scopus
Field-restricted search across title, abstract, and keywords (`TITLE-ABS-KEY`).

```
TITLE-ABS-KEY(("reinforcement learning" OR "graph theory" OR "graph neural networks") AND "marine ecology")
AND PUBYEAR > 1999 AND PUBYEAR < 2027
AND (LIMIT-TO(LANGUAGE, "English"))
```

- Records returned: **782**
- Date run: __________

---

## Google Scholar
Google Scholar does not support field-restricted queries, so equivalent
keyword combinations were entered through the full-text search interface.

```
("reinforcement learning" OR "graph theory" OR "graph neural networks") "marine ecology"
```

Custom year range: 2000–2026.

- Records returned: **994**
- Date run: __________

---

## Note on the keyword revision
An initial search omitted "graph neural networks (GNNs)" from the keyword set,
which missed papers combining RL and GT. The term was subsequently added and
the searches re-run. New GNN records were cross-checked against the existing
set to avoid duplicates before inclusion.

---

## Deduplication and screening totals (see PRISMA flow diagram, Figure 5)

| Stage | Count |
|---|---|
| Identified (WoS 56 + Scopus 782 + Google Scholar 994) | 1832 |
| Duplicates removed before screening | 368 |
| Records screened (title & abstract) | 1464 |
| Excluded after title/abstract screening | 1254 |
| Full-text assessed for eligibility | 210 |
| Excluded: missing full text | 28 |
| Excluded: outside scope | 39 |
| Excluded: other methodological reasons | 21 |
| **Included in review** | **122** |
