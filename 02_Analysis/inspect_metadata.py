
import csv

file_path = "01_Data/hmp2_metadata_2018-08-20.csv"

key_columns = [
    "Project",
    "External ID",
    "Participant ID",
    "site_sub_coll",
    "data_type",
    "week_num",
    "visit_num",
    "GSSR IDs",
    "ProjectSpecificID",
    "diagnosis",
    "stool_id"
]

with open(file_path, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    rows = list(reader)

print("TOTAL METADATA RECORDS:", len(rows))

print("\nFIRST 10 RECORDS:")
for i, row in enumerate(rows[:10]):
    print("\nRecord", i + 1)
    for col in key_columns:
        if col in row:
            print(col, ":", row[col])

print("\nRECORDS CONTAINING SRR IDENTIFIERS:")

count = 0

for row in rows:
    for col, value in row.items():
        if value and "SRR" in value.upper():
            print({
                "column": col,
                "value": value,
                "participant": row.get("Participant ID"),
                "diagnosis": row.get("diagnosis")
            })
            count += 1

            if count >= 20:
                break

    if count >= 20:
        break

print("\nSRR MATCHES DISPLAYED:", count)
