
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kruskal

# Create output folder
os.makedirs("04_Graphs", exist_ok=True)
os.makedirs("03_Results", exist_ok=True)

# Load participant-level data
data = pd.read_csv(
    "03_Results/participant_level_phylum_abundance.csv"
)

groups = ["CD", "UC", "nonIBD"]

# Select top 8 phyla by overall mean abundance
top_phyla = (
    data.groupby("Phylum")["Relative_Abundance_Percent"]
    .mean()
    .nlargest(8)
    .index.tolist()
)

results = []

# Perform Kruskal-Wallis test for each phylum
for phylum in top_phyla:
    values = []

    for group in groups:
        group_values = data.loc[
            (data["Phylum"] == phylum) &
            (data["diagnosis"] == group),
            "Relative_Abundance_Percent"
        ].dropna().values

        values.append(group_values)

    if all(len(v) > 0 for v in values):
        statistic, p_value = kruskal(*values)

        results.append({
            "Phylum": phylum,
            "Kruskal_Wallis_H": statistic,
            "P_value": p_value
        })

# Apply Benjamini-Hochberg FDR correction
results_df = pd.DataFrame(results)

if not results_df.empty:
    p_values = results_df["P_value"].values
    n = len(p_values)

    order = np.argsort(p_values)
    sorted_p = p_values[order]

    adjusted = sorted_p * n / np.arange(1, n + 1)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    adjusted = np.minimum(adjusted, 1)

    fdr = np.empty(n)
    fdr[order] = adjusted

    results_df["FDR_adjusted_p"] = fdr
    results_df["Significant_FDR_0.05"] = fdr < 0.05

    results_df.to_csv(
        "03_Results/phylum_statistical_tests.csv",
        index=False
    )

# Create boxplot figure
fig, axes = plt.subplots(2, 4, figsize=(16, 9))
axes = axes.flatten()

for i, phylum in enumerate(top_phyla):
    ax = axes[i]

    plot_values = [
        data.loc[
            (data["Phylum"] == phylum) &
            (data["diagnosis"] == group),
            "Relative_Abundance_Percent"
        ].dropna().values
        for group in groups
    ]

    ax.boxplot(
        plot_values,
        tick_labels=groups,
        showfliers=False
    )

    ax.set_title(phylum, fontsize=10)
    ax.set_ylabel("Relative abundance (%)")
    ax.tick_params(axis="x", rotation=20)

    row = results_df[results_df["Phylum"] == phylum]

    if not row.empty:
        p = row.iloc[0]["FDR_adjusted_p"]
        ax.text(
            0.5, 0.95,
            f"FDR-adjusted p = {p:.3g}",
            transform=ax.transAxes,
            ha="center",
            va="top",
            fontsize=8
        )

fig.suptitle(
    "Participant-level Phylum Abundance Across Disease Groups",
    fontsize=14
)

plt.tight_layout()

plt.savefig(
    "04_Graphs/statistical_phylum_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSTATISTICAL ANALYSIS COMPLETED")
print("\nKruskal-Wallis test with FDR correction:")
print(results_df.to_string(index=False))

print("\nSaved:")
print("03_Results/phylum_statistical_tests.csv")
print("04_Graphs/statistical_phylum_comparison.png")
