
import csv
import os

folder = "01_Data"

files = [
    "phylum_taxonomy_abundances_SSU_v4.1.tsv",
    "taxonomy_abundances_SSU_v4.1.tsv"
]

for filename in files:

    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        rows = list(reader)

    header = rows[0]

    print("\n" + "=" * 55)
    print("FILE:", filename)
    print("=" * 55)

    print("Total rows:", len(rows) - 1)
    print("Total columns:", len(header))
    print("First 8 sample IDs:", header[-8:])

    print("\nFirst 5 data entries:")

    for row in rows[1:6]:
        print(row[:2] + row[2:6] if len(row) > 2 else row[:6])
