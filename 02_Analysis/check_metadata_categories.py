
import csv
from collections import Counter

file_path = "01_Data/hmp2_metadata_2018-08-20.csv"

data_types = Counter()
diagnoses = Counter()
combinations = Counter()

with open(file_path, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data_type = row.get("data_type", "").strip()
        diagnosis = row.get("diagnosis", "").strip()

        data_types[data_type] += 1
        diagnoses[diagnosis] += 1
        combinations[(data_type, diagnosis)] += 1

print("\n1. SAMPLE TYPES")
for name, count in data_types.most_common():
    print(name, ":", count)

print("\n2. DISEASE GROUPS")
for name, count in diagnoses.most_common():
    print(name if name else "Blank", ":", count)

print("\n3. SAMPLE TYPE AND DIAGNOSIS")
for (data_type, diagnosis), count in combinations.most_common():
    print(data_type, "|", diagnosis, ":", count)
