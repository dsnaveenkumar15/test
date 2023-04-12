import pandas as pd

reports_file_name = "N:\\Professional\\Office\\DevOps\\visa\\report.csv"

# read the reports.csv file
df = pd.read_csv(reports_file_name)

# iterate through each row of the dataframe
for index, row in df.iterrows():
    file_name = row['SrcFileName']
    line_number = row['Line']
    # open the file mentioned in the file_name column
    with open(file_name, 'r') as f:
        lines = f.readlines()
        # read the line number from the file
        code = lines[line_number - 1]
        # add the line to the "line" column of the dataframe
        df.at[index, 'Code'] = code

# save the updated dataframe to the reports.csv file
df.to_csv(reports_file_name, index=False)

