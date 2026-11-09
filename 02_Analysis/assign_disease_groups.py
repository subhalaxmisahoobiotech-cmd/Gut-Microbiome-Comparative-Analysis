import pandas as pd

# Read matched sequencing runs
sra = pd.read_csv("03_Results/matched_sequencing_runs.csv")

# Read clinical metadata
clinical = pd.read_csv(
    "01_Data/hmp2_metadata_2018-08-20.csv",
    low_memory=False
)

# Keep only metagenomics records
clinical = clinical[
    clinical["data_type"] == "metagenomics"
].copy()

# Clean participant IDs
clinical["Participant ID"] = (
    clinical["Participant ID"].astype(str).str.strip()
)

# Extract participant IDs from NCBI metadata
sra["extracted_participant"] = (
    sra["host_subject_id"]
    .astype(str)
    .str.extract(r"^([A-Za-z]\d+)", expand=False)
)

# Create one diagnosis record per participant
diagnosis_map = (
    clinical.groupby("Participant ID")["diagnosis"]
    .agg(lambda x: sorted(set(x.dropna().astype(str).str.strip())))
    .reset_index()
)

# Check for participants with multiple diagnoses
diagnosis_map["diagnosis_count"] = (
    diagnosis_map["diagnosis"].apply(len)
)

print("TOTAL CLINICAL PARTICIPANTS:", len(diagnosis_map))

print("\nPARTICIPANTS WITH MULTIPLE DIAGNOSES:")
print(
    diagnosis_map[
        diagnosis_map["diagnosis_count"] > 1
    ].to_string(index=False)
)

# Keep only participants with one clear diagnosis
diagnosis_map = diagnosis_map[
    diagnosis_map["diagnosis_count"] == 1
].copy()

diagnosis_map["diagnosis"] = diagnosis_map["diagnosis"].apply(
    lambda x: x[0]
)

# Match sequencing runs with diagnosis
result = sra.merge(
    diagnosis_map[["Participant ID", "diagnosis"]],
    left_on="extracted_participant",
    right_on="Participant ID",
    how="left"
)

# Display results
print("\nDISEASE GROUPS (SEQUENCING RUNS):")
print(result["diagnosis"].value_counts(dropna=False))

print("\nDISEASE GROUPS (UNIQUE PARTICIPANTS):")
print(
    result.drop_duplicates("extracted_participant")[
        "diagnosis"
    ].value_counts(dropna=False)
)

# Save results
result.to_csv(
    "03_Results/runs_with_disease_groups.csv",
    index=False
)

print("\nSaved: 03_Results/runs_with_disease_groups.csv")