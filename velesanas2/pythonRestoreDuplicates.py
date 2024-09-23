import csv

input_file = 'kandidatiKurzeme.csv'
output_file = 'kandidatiKurzeme2.csv'

def restore_omitted_values(lst, repeat=True):
    result = []
    last_value = ''
    for val in lst:
        if val.strip() != '':
            last_value = val
        result.append(last_value if repeat else val)
    return result

def repeat_each_value(lst):
    result = []
    for val in lst:
        if val.strip() != '':
            result.extend([val, val])
    return result

def process_file(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    # Process the first three rows
    rows[0] = restore_omitted_values(rows[0])
    rows[1] = repeat_each_value(rows[1])
    rows[2] = repeat_each_value(rows[2])

    # Write the output
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

# Run the function
process_file(input_file, output_file)
