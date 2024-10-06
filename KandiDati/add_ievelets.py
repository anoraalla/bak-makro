import pandas as pd

# Load the CSV files into DataFrames
withgender_df = pd.read_csv('14withgender.csv')
ieveleti_df = pd.read_csv('14Ieveleti.csv')

# Strip any leading/trailing spaces or quotes from relevant columns
ieveleti_df['Partija'] = ieveleti_df['Partija'].str.strip()
ieveleti_df['Vards'] = ieveleti_df['Vards'].str.strip()



# Create a column in withgender_df to indicate whether a candidate is elected
withgender_df['Ievelets'] = withgender_df.apply(
    lambda row: 'true' if any(
        (row['Vards'] == elected_name) and (row['Partija'].strip() == elected_party)
        for elected_name, elected_party in zip(ieveleti_df['Vards'], ieveleti_df['Partija'])
    ) else 'false',
    axis=1
)

# Reorder columns to insert the 'Ievelets' column right after 'Vards'
columns = list(withgender_df.columns)
new_column_order = columns[:3] + ['Ievelets'] + columns[3:]
withgender_df = withgender_df[new_column_order]

# Save the updated DataFrame to a new CSV file
withgender_df.to_csv('14withgender_updated.csv', index=False)

