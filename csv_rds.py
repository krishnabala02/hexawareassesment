from pathlib import Path
import csv

input_dir = Path.home().joinpath("Desktop", "csv_files")
print(input_dir)
# glob = specific folder
# rglob = including subfolder
files = list(input_dir.rglob("*.csv"))
for each_file in files:
    with open(each_file, 'r') as csv_file:
        csv_reader = csv.DictReader(each_file)