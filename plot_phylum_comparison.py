
import os
import pandas as pd
import matplotlib.pyplot as plt

# Create graph folder if it does not exist
os.makedirs("04_Graphs", exist_ok=True)

# Load participant-level abundance data
data = pd.read_csv(
    "03_Results/participant_level_phylum_abundance.csv"
)

# Calculate average abundance for each disease group
summary = (
    data.groupby(["diagnosis", "Phylum"])["Relative_Abundance_Percent"]
    .mean()
    .reset_index()
)

# Select the 10 most abundant phyla overall
top_phyla = (
    summary.groupby("Phylum")["Relative_Abundance_Percent"]
    .mean()
    .nlargest(10)
    .index
)

plot_data = summary[summary["Phylum"].isin(top_phyla)]

# Arrange data for grouped bar chart
pivot = plot_data.pivot(
    index="Phylum",
    columns="diagnosis",
    values="Relative_Abundance_Percent"
).fillna(0)

# Order phyla by overall abundance
pivot["overall_mean"] = pivot.mean(axis=1)
pivot = pivot.sort_values("overall_mean", ascending=False)
pivot = pivot.drop(columns="overall_mean")

# Generate grouped bar chart
ax = pivot.plot(
    kind="bar",
    figsize=(13, 7),
    width=0.8
)

ax.set_title(
    "Comparison of Top 10 Bacterial Phyla Across Disease Groups"
)
ax.set_xlabel("Bacterial Phylum")
ax.set_ylabel("Mean Relative Abundance (%)")
ax.legend(title="Disease Group")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    "04_Graphs/top_10_phylum_comparison.png",
    dpi=300
)

plt.show()

# Print top 10 phyla for each disease group
print("\nTOP 10 PHYLA IN EACH DISEASE GROUP:")

for group in ["CD", "UC", "nonIBD"]:
    print(f"\n{group}:")
    group_data = summary[summary["diagnosis"] == group]

    print(
        group_data.sort_values(
            "Relative_Abundance_Percent",
            ascending=False
        ).head(10).to_string(index=False)
    )

print("\nGraph saved in 04_Graphs/")
