import csv

input_file = 'kandidatiKurzeme2.csv'
output_file = 'melted_kandidatiKurzeme.csv'

def melt_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    header_party = rows[0]
    header_name = rows[1]
    header_number = rows[2]
    header_plus_minus = rows[3]

    # Prepare the header for the new CSV
    new_header = ["Apgabals", "Struktūrvienība", "Party", "Name", "Number", "Pluses", "Minuses"]

    # Create the output data
    melted_data = []
    for row in rows[4:]:  # Start from the fifth line
        struktura_value = row[0]  # The first column value
        
        for i in range(1, len(row), 2):  # Step through the columns in pairs
            if i < len(header_party) and header_party[i].strip() and i+1 < len(row):
                print(f"lengths = {len(header_party)}, {len(header_name)}, {len(header_number)}, {len(header_plus_minus)}")
                party = header_party[i]
                name = header_name[i]
                number = header_number[i]
                pluses = row[i]
                minuses = row[i + 1]
                
                # Append the new row to the melted data
                melted_data.append(["Kurzeme", struktura_value, party, name, number, pluses, minuses])

    # Write the melted data to the new CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_header)
        writer.writerows(melted_data)

# Run the function
melt_csv(input_file, output_file)
