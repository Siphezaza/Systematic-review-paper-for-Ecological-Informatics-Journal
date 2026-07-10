"""
inter_rater_reliability.py

Computes inter-rater reliability for the six-dimension theoretical rigour
scoring framework used in the systematic review.

Two raters independently scored all 122 studies across six dimensions
(0-3 scale). This script reports, per dimension and overall:
    - Cohen's kappa (unweighted and quadratic-weighted)
    - raw percent agreement
    - mean absolute difference
    - Spearman's rank correlation
and produces the score-concordance matrix (Figure 12) and a per-dimension
agreement bar chart.

Requirements:
    pip install numpy pandas scikit-learn scipy matplotlib

Input:
    paired_scores.csv  - one row per study, with both raters' six scores.
    Columns:
        Study,
        Zaza_Eco, Zaza_The, Zaza_Unc, Zaza_Sca, Zaza_Sta, Zaza_Int,
        Nicole_Eco, Nicole_The, Nicole_Unc, Nicole_Sca, Nicole_Sta, Nicole_Int
"""

import numpy as np
import pandas as pd
from sklearn.metrics import cohen_kappa_score
from scipy.stats import spearmanr

# ------------------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------------------
CSV_PATH = "paired_scores.csv"

DIMENSION_NAMES = [
    "Ecological Relevance",
    "Theoretical Foundations",
    "Uncertainty Quantification",
    "Scalability",
    "Stakeholder Utility",
    "Interpretability"
]

ZAZA_COLS = ['Zaza_Eco', 'Zaza_The', 'Zaza_Unc', 'Zaza_Sca', 'Zaza_Sta', 'Zaza_Int']
NICOLE_COLS = ['Nicole_Eco', 'Nicole_The', 'Nicole_Unc', 'Nicole_Sca', 'Nicole_Sta', 'Nicole_Int']


# ------------------------------------------------------------------------------
# STEP 1: LOAD PAIRED DATA FROM CSV
# ------------------------------------------------------------------------------
def load_paired_data(csv_path):
    """
    Load paired scores from CSV.

    The CSV has one row per study with BOTH raters' scores, which guarantees
    paper-to-paper correspondence: study [8] in rater 1's data is the exact
    same paper as study [8] in rater 2's data.
    """
    df = pd.read_csv(csv_path)

    zaza_matrix = df[ZAZA_COLS].values
    nicole_matrix = df[NICOLE_COLS].values
    study_ids = df['Study'].values

    print(f"  Loaded {len(df)} studies from {csv_path}")
    print(f"  Each study has 6 dimension scores for both raters")
    print(f"  Total ratings: {len(df) * 6} = {len(df)} studies x 6 dimensions")

    print(f"\n  --- Verification sample ---")
    for i in range(min(3, len(df))):
        sid = int(study_ids[i])
        z = zaza_matrix[i].tolist()
        n = nicole_matrix[i].tolist()
        print(f"  Study [{sid}]: Rater1={z} (sum={sum(z)}), Rater2={n} (sum={sum(n)})")

    return zaza_matrix, nicole_matrix, study_ids


# ------------------------------------------------------------------------------
# STEP 2: COMPUTE COHEN'S KAPPA
# ------------------------------------------------------------------------------
def interpret_kappa(k):
    """Landis & Koch (1977) interpretation."""
    if k < 0:      return "Poor"
    elif k < 0.21: return "Slight"
    elif k < 0.41: return "Fair"
    elif k < 0.61: return "Moderate"
    elif k < 0.81: return "Substantial"
    else:          return "Almost Perfect"


def compute_kappa(zaza_matrix, nicole_matrix):
    """Compute Cohen's Kappa for each dimension and overall."""
    n_studies = len(zaza_matrix)
    results = []
    all_zaza = []
    all_nicole = []

    print("\n" + "=" * 72)
    print("  COHEN'S KAPPA INTER-RATER RELIABILITY ANALYSIS")
    print("  Theoretical Rigour Scoring Framework")
    print(f"  N = {n_studies} studies  |  {n_studies * 6} individual ratings")
    print("=" * 72)

    for dim_idx, dim_name in enumerate(DIMENSION_NAMES):
        z_dim = zaza_matrix[:, dim_idx].tolist()
        n_dim = nicole_matrix[:, dim_idx].tolist()

        all_zaza.extend(z_dim)
        all_nicole.extend(n_dim)

        kappa_unw = cohen_kappa_score(z_dim, n_dim)
        kappa_w = cohen_kappa_score(z_dim, n_dim, weights='quadratic')

        agreements = sum(1 for z, n in zip(z_dim, n_dim) if z == n)
        pct_agree = (agreements / len(z_dim)) * 100
        mad = np.mean([abs(z - n) for z, n in zip(z_dim, n_dim)])
        rho, pval = spearmanr(z_dim, n_dim)
        pval_str = f"{pval:.2e}" if pval < 0.001 else str(round(pval, 3))

        results.append({
            'Dimension': dim_name,
            'Kappa (weighted)': round(kappa_w, 3),
            'Kappa (unweighted)': round(kappa_unw, 3),
            'Agreement (%)': round(pct_agree, 1),
            'Mean Abs. Diff': round(mad, 2),
            'Spearman r': round(rho, 3),
            'p-value': pval_str,
            'Interpretation': interpret_kappa(kappa_w)
        })

        print(f"\n  {dim_name}:")
        print(f"    Weighted Kappa:    {kappa_w:.3f}  ({interpret_kappa(kappa_w)})")
        print(f"    Unweighted Kappa:  {kappa_unw:.3f}")
        print(f"    Agreement:         {pct_agree:.1f}%")
        print(f"    Mean Abs. Diff:    {mad:.2f}")
        print(f"    Spearman r:        {rho:.3f}  (p = {pval_str})")

    print("\n" + "=" * 72)
    print("  OVERALL (all 6 dimensions combined)")
    print("=" * 72)

    kappa_all_w = cohen_kappa_score(all_zaza, all_nicole, weights='quadratic')
    kappa_all_u = cohen_kappa_score(all_zaza, all_nicole)
    overall_agree = sum(1 for z, n in zip(all_zaza, all_nicole) if z == n)
    overall_pct = (overall_agree / len(all_zaza)) * 100
    overall_mad = np.mean([abs(z - n) for z, n in zip(all_zaza, all_nicole)])
    rho_all, pval_all = spearmanr(all_zaza, all_nicole)

    print(f"    Weighted Kappa:    {kappa_all_w:.3f}  ({interpret_kappa(kappa_all_w)})")
    print(f"    Unweighted Kappa:  {kappa_all_u:.3f}")
    print(f"    Agreement:         {overall_pct:.1f}%")
    print(f"    Mean Abs. Diff:    {overall_mad:.2f}")
    print(f"    Spearman r:        {rho_all:.3f}  (p = {pval_all:.2e})")

    print("\n" + "=" * 72)
    print("  SUMMARY TABLE")
    print("=" * 72)
    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))

    overall = {
        'n_studies': n_studies,
        'n_ratings': len(all_zaza),
        'weighted_kappa': kappa_all_w,
        'unweighted_kappa': kappa_all_u,
        'percent_agreement': overall_pct,
        'mean_abs_diff': overall_mad,
        'spearman_r': rho_all,
        'interpretation': interpret_kappa(kappa_all_w)
    }

    return df_results, overall, all_zaza, all_nicole


# ------------------------------------------------------------------------------
# STEP 3: VISUALISATION
# ------------------------------------------------------------------------------
def create_figure(results_df, overall, all_zaza, all_nicole):
    """Create and save both figures as separate PNG files."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n[Note: matplotlib not installed. Skipping figures.]")
        print("Install: pip install matplotlib")
        return

    # --- FIGURE 1: Inter-Rater Agreement by Dimension ---
    fig1, ax1 = plt.subplots(figsize=(10, 6))

    dims_short = ['Eco. Rel.', 'Theor. Found.', 'Uncert. Quant.',
                  'Scalability', 'Stakehold. Util.', 'Interpret.']
    kappa_unw = results_df['Kappa (unweighted)'].values
    kappa_w = results_df['Kappa (weighted)'].values

    x = np.arange(len(dims_short))
    width = 0.35

    bars1 = ax1.bar(x - width/2, kappa_unw, width, label='Unweighted',
                    color='#4472C4', alpha=0.85, edgecolor='white', linewidth=0.5)
    bars2 = ax1.bar(x + width/2, kappa_w, width, label='Weighted (quadratic)',
                    color='#ED7D31', alpha=0.85, edgecolor='white', linewidth=0.5)

    ax1.axhspan(0.00, 0.20, alpha=0.06, color='red')
    ax1.axhspan(0.21, 0.40, alpha=0.06, color='orange')
    ax1.axhspan(0.41, 0.60, alpha=0.06, color='gold')
    ax1.axhspan(0.61, 0.80, alpha=0.08, color='green')
    ax1.axhspan(0.81, 1.00, alpha=0.10, color='darkgreen')

    ax1.text(5.4, 0.10, 'Slight', fontsize=8, ha='right', color='gray', style='italic')
    ax1.text(5.4, 0.30, 'Fair', fontsize=8, ha='right', color='gray', style='italic')
    ax1.text(5.4, 0.50, 'Moderate', fontsize=8, ha='right', color='gray', style='italic')
    ax1.text(5.4, 0.70, 'Substantial', fontsize=8, ha='right', color='gray', style='italic')
    ax1.text(5.4, 0.90, 'Almost Perfect', fontsize=8, ha='right', color='gray', style='italic')

    ax1.set_ylabel("Cohen's Kappa", fontsize=12)
    ax1.set_title(f"Inter-Rater Agreement by Dimension\n(N = {overall['n_studies']} studies)",
                  fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(dims_short, rotation=30, ha='right', fontsize=10)
    ax1.set_ylim(0, 1)
    ax1.legend(loc='lower right', fontsize=10, framealpha=0.9)
    ax1.grid(axis='y', alpha=0.2)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    for bar in list(bars1) + list(bars2):
        h = bar.get_height()
        ax1.annotate(f'{h:.3f}', xy=(bar.get_x() + bar.get_width()/2, h),
                     xytext=(0, 3), textcoords="offset points", ha='center',
                     va='bottom', fontsize=8)

    plt.tight_layout()
    plt.savefig('cohens_kappa_by_dimension.png', dpi=300, bbox_inches='tight')
    plt.close(fig1)
    print("\n  Figure 1 saved: cohens_kappa_by_dimension.png")

    # --- FIGURE 2: Score Concordance Matrix ---
    fig2, ax2 = plt.subplots(figsize=(8, 6.5))

    agree_matrix = np.zeros((4, 4))
    for z, n in zip(all_zaza, all_nicole):
        agree_matrix[z, n] += 1
    agree_pct = agree_matrix / agree_matrix.sum() * 100

    im = ax2.imshow(agree_pct, cmap='Blues', aspect='auto')
    ax2.set_xticks([0, 1, 2, 3])
    ax2.set_yticks([0, 1, 2, 3])
    ax2.set_xticklabels(['0', '1', '2', '3'], fontsize=11)
    ax2.set_yticklabels(['0', '1', '2', '3'], fontsize=11)
    ax2.set_xlabel("Rater 2 Score", fontsize=12)
    ax2.set_ylabel("Rater 1 Score", fontsize=12)
    ax2.set_title(f"Score Concordance Matrix\n(% of all {overall['n_ratings']} ratings)",
                  fontsize=13, fontweight='bold')

    for i in range(4):
        for j in range(4):
            count = int(agree_matrix[i, j])
            pct = agree_pct[i, j]
            if count > 0:
                color = 'white' if pct > 15 else 'black'
                ax2.text(j, i, f'{count}\n({pct:.1f}%)', ha='center', va='center',
                         fontsize=11, fontweight='bold', color=color)

    for i in range(4):
        ax2.add_patch(plt.Rectangle((i-0.5, i-0.5), 1, 1, fill=False,
                                    edgecolor='red', linewidth=2.5))

    cbar = plt.colorbar(im, ax=ax2)
    cbar.set_label('Percentage (%)', fontsize=11)

    plt.tight_layout()
    plt.savefig('cohens_kappa_concordance_matrix.png', dpi=300, bbox_inches='tight')
    plt.close(fig2)
    print("  Figure 2 saved: cohens_kappa_concordance_matrix.png")


# ------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------
def main():
    print("\n  [1/3] Loading paired scores from CSV...")
    zaza_matrix, nicole_matrix, study_ids = load_paired_data(CSV_PATH)

    print(f"\n  [2/3] Computing Cohen's Kappa...")
    df, overall, all_z, all_n = compute_kappa(zaza_matrix, nicole_matrix)

    print(f"\n  [3/3] Creating visualizations (2 separate figures)...")
    create_figure(df, overall, all_z, all_n)


if __name__ == "__main__":
    main()
