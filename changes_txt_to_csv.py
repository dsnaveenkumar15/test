import csv

# specify the file name which has changed files and lines
file_name = "N:\\Professional\\Office\\DevOps\\visa\\changes.txt"

# mention the csv file name
csv_file_name = "N:\\Professional\\Office\\DevOps\\visa\\changes.csv"


# create a variable to store the current file name
temp_file_name = ""

# create a new CSV file to store the data
with open(csv_file_name, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # write the column names
    writer.writerow(['file_name', 'lines'])
    # open the text file
    with open(file_name, 'r') as f:
        for line in f:
            # check if the line starts with "file"
            if line.startswith("file"):
                temp_file_name = line.split("%>")[1].strip()
            # check if the line starts with "line"
            elif line.startswith("line"):
                # write the current file name and the line in the CSV file
                writer.writerow([temp_file_name, line.split("%>")[1].strip()])

