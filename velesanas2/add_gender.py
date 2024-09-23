import csv
import re
import sys

def get_gender(name):
    sex = "Other"
    # Extract first name (if there are multiple names)
    first_name = re.sub(r"(^[^ ]+)( ([^ ]+))+", r"\1", name)
    # print(f"{first_name}")
    if first_name in ["Adam", "Alexander", "Aliaksandr", "Andrey", "Anton", "Artem", "Bruno",
                      "Čiro", "Dmitry", "Dmytro", "Gvido", "Hugo", "Ivo", "Nikita", "Ņikita", "Nikolay",
                      "Oleksandr", "Oto", "Raivo", "Renē", "Udo", "Uko", "Vladimir"]:
        sex = "Male"
    elif first_name in ["Naomi", "Nelli", "Fani", "Romi"]:
        sex = "Female"
    elif re.search(r"[sš]$", first_name):
        sex = "Male"
    elif re.search(r"[ae]$", first_name):
        sex = "Female"
    else:
        print(f"Undefined sex for name = {name}") 

    return sex

# Function to process the CSV and add the Gender column
def add_gender_column(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    # Get the header and insert "Gender" after "Name"
    header = rows[0]
    index_name = header.index("Name")
    header.insert(index_name + 1, "Gender")
    
    # Process each row and add the gender information
    new_rows = [header]
    for row in rows[1:]:
        name = row[index_name]
        gender = get_gender(name)
        row.insert(index_name + 1, gender)
        new_rows.append(row)

    # Write the output to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(new_rows)

# Run the function
      
if __name__ == '__main__': 
    if len(sys.argv) != 3: 
        print("Usage: add_gender.py infile.csv outfile.csv")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    add_gender_column(input_file, output_file)