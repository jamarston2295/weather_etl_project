import csv

def load_to_csv(data, filepath="output.csv"):
    keys = data.keys()
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerow(data)
