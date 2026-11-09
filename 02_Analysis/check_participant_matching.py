import pandas as pd

# Read matched NCBI sequencing run information
sra = pd.read_csv("03_Results/matched_sequencing_runs.csv")

# Read clinical metadata
clinical = pd.read_csv("01_Data/hmp2_metadata_2018-08-20.csv")

# Keep only metagenomics records
clinical = clinical[
    clinical["data_type"] == "metagenomics"
].copy()

# Extract participant ID from host_subject_id
# Example: C3037C2_MGX becomes C3037
sra["extracted_participant"] = (
    sra["host_subject_id"]
    .astype(str)
    .str.extract(r"^([A-Za-z]\d+)", expand=False)
)

# Convert participant IDs to strings
clinical["Participant ID"] = (
    clinical["Participant ID"].astype(str).str.strip()
)

# Find matching participant IDs
clinical_participants = set(clinical["Participant ID"].dropna())

matched_participants = sra[
    sra["extracted_participant"].isin(clinical_participants)
].copy()

unmatched_participants = sra[
    ~sra["extracted_participant"].isin(clinical_participants)
].copy()

print("TOTAL MATCHED SEQUENCING RUNS:", len(sra))

print(
    "RUNS MATCHED TO CLINICAL PARTICIPANTS:",
    len(matched_participants)
)

print(
    "RUNS NOT MATCHED TO CLINICAL PARTICIPANTS:",
    len(unmatched_participants)
)

print("\nFIRST 15 PARTICIPANT MATCHES:")

print(
    matched_participants[
        ["Run", "host_subject_id", "extracted_participant"]
    ].head(15).to_string(index=False)
)

print("\nFIRST 10 UNMATCHED IDENTIFIERS:")

print(
    unmatched_participants[
        ["Run", "host_subject_id", "extracted_participant"]
    ].head(10).to_string(index=False)
)
print("\nALL COLUMN NAMES IN THE FINAL FILE:")
print(pd.read_csv("03_Results/runs_with_disease_groups.csv", nrows=0).columns.tolist())