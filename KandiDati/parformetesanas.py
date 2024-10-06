import pandas as pd

# Read the CSV file into a DataFrame
input_file = '12.csv'
df = pd.read_csv(input_file)

# Define the list of region columns
regions = ['Riga', 'Vidzeme', 'Latgale', 'Kurzeme', 'Zemgale']

# Create empty lists to store the new data
apgabals_list = []
rangs_list = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Find the region column with a non-null value
    for region in regions:
        if pd.notnull(row[region]):
            apgabals_list.append(region)
            rangs_list.append(row[region])
            break

rangs_list_int = [int(x) for x in rangs_list]

# Add the new columns to the DataFrame
df['Apgabals'] = apgabals_list
df['Rangs'] = rangs_list_int

# Select the columns for the output CSV
output_columns = ['Saraksts', 'Partija', 'Numurs', 'Vards', 'Apgabals', 'Rangs']

# Write the transformed data to a new CSV file
output_file = 'output.csv'
df.to_csv(output_file, columns=output_columns, index=False)

