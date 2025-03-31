import csv

with open("liens.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    for i, row in enumerate(reader):
        print(f"Ligne {i+1} ({len(row)} colonnes) : {row}")