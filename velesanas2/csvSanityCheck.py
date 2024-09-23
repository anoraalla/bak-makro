import csv

input_file = 'kandidatiKurzeme.csv'

def print_first_column(input_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Ensuring the row is not empty
                # print(row[0])
                print(len(row))

# Run the function
print_first_column(input_file)