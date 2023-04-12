import csv

csv_file_name = "N:\\Professional\\Office\\DevOps\\visa\\changes.csv"

with open(csv_file_name, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames + ['line_number']
    rows = list(reader)
    for row in rows:
        file_name = row['file_name']
        with open(file_name, 'r') as f:
            x = f.readlines()
            x = [i.rstrip('\n') for i in x]
        line_to_find = row['lines']
        line_number = x.index(line_to_find)
        row['line_number'] = line_number+1

with open(csv_file_name, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
