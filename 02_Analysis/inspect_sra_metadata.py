
import pandas as pd

file_path = "01_Data/SraRunTable.csv"

df = pd.read_csv(file_path)

print("TOTAL RUNS:", len(df))
print("TOTAL COLUMNS:", len(df.columns))

print("\nCOLUMN NAMES:")
print(df.columns.tolist())

print("\nFIRST 5 RECORDS:")

columns_to_show = [
    col for col in [
        "Run",
        "BioSample",
        "Sample",
        "Experiment",
        "LibraryName",
        "ScientificName",
        "Platform",
        "spots",
        "bases"
    ]
    if col in df.columns
]

print(df[columns_to_show].head().to_string(index=False))

print("\nFIRST 10 RUN ACCESSIONS:")
print(df["Run"].head(10).tolist())
