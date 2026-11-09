
import pandas as pd

# Read NCBI RunInfo metadata
sra = pd.read_csv("01_Data/SraRunTable.csv")

# Read MGnify phylum abundance table
taxonomy = pd.read_csv(
    "01_Data/phylum_taxonomy_abundances_SSU_v4.1.tsv",
    sep="\t"
)

# Extract sequencing run IDs from MGnify columns
mgnify_runs = set(taxonomy.columns[2:])

# Extract sequencing run IDs from NCBI
ncbi_runs = set(sra["Run"].dropna().astype(str))

# Find common and unmatched runs
matched = mgnify_runs.intersection(ncbi_runs)
missing_ncbi = mgnify_runs - ncbi_runs
missing_mgnify = ncbi_runs - mgnify_runs

print("MGNIFY RUNS:", len(mgnify_runs))
print("NCBI RUNS:", len(ncbi_runs))
print("MATCHED RUNS:", len(matched))
print("MGNIFY RUNS NOT FOUND IN NCBI:", len(missing_ncbi))
print("NCBI RUNS NOT FOUND IN MGNIFY:", len(missing_mgnify))

# Save matched run information
matched_df = sra[sra["Run"].astype(str).isin(matched)].copy()

matched_df.to_csv(
    "03_Results/matched_sequencing_runs.csv",
    index=False
)

print("\nFIRST 10 MATCHED RUNS:")
columns = [
    col for col in [
        "Run",
        "BioSample",
        "Experiment",
        "Sample Name",
        "host_subject_id",
        "Collection_Date"
    ]
    if col in matched_df.columns
]

print(matched_df[columns].head(10).to_string(index=False))

print("\nMatched run information saved successfully.")
