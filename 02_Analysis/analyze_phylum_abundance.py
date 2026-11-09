
import pandas as pd

# 1. Load MGnify phylum abundance data
taxonomy = pd.read_csv(
    "01_Data/phylum_taxonomy_abundances_SSU_v4.1.tsv",
    sep="\t"
)

# 2. Load sequencing runs with disease information
metadata = pd.read_csv(
    "03_Results/runs_with_disease_groups.csv"
)

# 3. Select bacterial phyla only
kingdom_column = taxonomy.columns[0]
phylum_column = taxonomy.columns[1]

bacterial_mask = (
    taxonomy[kingdom_column].astype(str).str.strip().str.lower()
    == "bacteria"
)

bacterial = taxonomy.loc[bacterial_mask].copy()

# 4. Convert abundance values into numeric format
abundance = bacterial.iloc[:, 2:].apply(
    pd.to_numeric, errors="coerce"
).fillna(0)

abundance.index = bacterial[phylum_column].astype(str)

# 5. Calculate relative abundance for each sequencing run
sample_totals = abundance.sum(axis=0).replace(0, pd.NA)

relative_abundance = (
    abundance.div(sample_totals, axis=1) * 100
)

# Convert table into one row per sequencing run
relative_abundance = relative_abundance.T
relative_abundance.index.name = "Run"
relative_abundance = relative_abundance.reset_index()

# 6. Attach participant and disease information
metadata["Run"] = metadata["Run"].astype(str)
relative_abundance["Run"] = relative_abundance["Run"].astype(str)

analysis_data = relative_abundance.merge(
    metadata[["Run", "Participant ID", "diagnosis"]],
    on="Run",
    how="inner"
)

# Remove records without participant or diagnosis information
analysis_data = analysis_data.dropna(
    subset=["Participant ID", "diagnosis"]
)

# Save sample-level results
analysis_data.to_csv(
    "03_Results/sample_level_phylum_relative_abundance.csv",
    index=False
)

# 7. Reshape data for participant-level analysis
phylum_columns = [
    col for col in relative_abundance.columns if col != "Run"
]

long_data = analysis_data.melt(
    id_vars=["Run", "Participant ID", "diagnosis"],
    value_vars=phylum_columns,
    var_name="Phylum",
    value_name="Relative_Abundance_Percent"
)

# Average repeated samples within each participant
participant_data = (
    long_data.groupby(
        ["Participant ID", "diagnosis", "Phylum"],
        as_index=False
    )["Relative_Abundance_Percent"].mean()
)

participant_data.to_csv(
    "03_Results/participant_level_phylum_abundance.csv",
    index=False
)

# 8. Calculate average abundance across participants in each group
group_summary = (
    participant_data.groupby(
        ["diagnosis", "Phylum"],
        as_index=False
    )["Relative_Abundance_Percent"].mean()
)

group_summary.to_csv(
    "03_Results/disease_group_phylum_summary.csv",
    index=False
)

# 9. Display summary
print("\nANALYSIS COMPLETED SUCCESSFULLY")

print("\nTOTAL SAMPLES ANALYSED:", len(analysis_data))

print(
    "UNIQUE PARTICIPANTS:",
    analysis_data["Participant ID"].nunique()
)

print("\nSAMPLES PER DISEASE GROUP:")
print(analysis_data["diagnosis"].value_counts())

print("\nUNIQUE PARTICIPANTS PER DISEASE GROUP:")
print(
    participant_data[
        ["Participant ID", "diagnosis"]
    ].drop_duplicates()["diagnosis"].value_counts()
)

print("\nPHYLUM-LEVEL GROUP SUMMARY:")
print(group_summary.head(15).to_string(index=False))

print("\nRESULT FILES SAVED IN 03_Results/")
