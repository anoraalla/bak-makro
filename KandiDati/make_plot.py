import pandas as pd
import matplotlib.pyplot as plt

# List of filenames and corresponding years
files = ["12withgender_updated.csv", "13withgender_updated.csv", "14withgender_updated.csv"]
years = [12, 13, 14]
custom_labels = ["2014", "2018", "2022"]

actual_years = [2014, 2018, 2022]

# Lists to store the calculated percentages
percent_females = []
percent_females_elected = []
percent_females_big_party = []
percent_females_top25 = []

# Process each file
for file in files:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file)
    
    # Calculate the percentage of female candidates
    total_candidates = df.shape[0]
    female_candidates = df[df['Gender'] == 'Female'].shape[0]
    percent_females.append((female_candidates / total_candidates) * 100)
    
    # Calculate the percentage of female elected candidates
    elected_df = df[df['Ievelets'] == True]
    
    
    total_elected_candidates = elected_df.shape[0]
    if total_elected_candidates > 0:
        female_elected_candidates = elected_df[elected_df['Gender'] == 'Female'].shape[0]
        percent_females_elected.append((female_elected_candidates / total_elected_candidates) * 100)
    else:
        percent_females_elected.append(0)  # No elected candidates in this case
    
    
    big_party_list = []
    
    if file == "12withgender_updated.csv": 
    	big_party_list = ["Partija \"VIENOTĪBA\"", "Nacionālā apvienība \"Visu Latvijai!\"-\"Tēvzemei un Brīvībai/LNNK\"", "Latvijas Reģionu Apvienība", 
    	"\"Saskaņa\" sociāldemokrātiskā partija", "Zaļo un Zemnieku savienība", "No sirds Latvijai"]
    elif file == "13withgender_updated.csv": 
    	big_party_list = ["Jaunā konservatīvā partija", "Nacionālā apvienība \"Visu Latvijai!\"-\"Tēvzemei un Brīvībai/LNNK\"", "\"Saskaņa\" sociāldemokrātiskā partija",
    	"Attīstībai/Par!", "Jaunā VIENOTĪBA", "Politiskā partija \"KPV LV\"", "Zaļo un Zemnieku savienība"]
    else: 
        big_party_list = ["Jaunā VIENOTĪBA", "Zaļo un Zemnieku savienība", "Politiskā partija \"Stabilitātei!\"", "Nacionālā apvienība \"Visu Latvijai!\"-\"Tēvzemei un Brīvībai/LNNK\"", "LATVIJA PIRMAJĀ VIETĀ",
        "\"PROGRESĪVIE\"", "\"APVIENOTAIS SARAKSTS - Latvijas Zaļā partija, Latvijas Reģionu Apvienība, Liepājas partija\""]
    
        
    big_party_df = df[df['Partija'].isin(big_party_list)]
    total_big_party_candidates = big_party_df.shape[0]
    if total_big_party_candidates > 0:
        female_big_party_candidates = big_party_df[big_party_df['Gender'] == 'Female'].shape[0]
        percent_females_big_party.append((female_big_party_candidates / total_big_party_candidates) * 100)
    else:
        percent_females_big_party.append(0)  # No elected candidates in this case
    
    
    top25_df = big_party_df[big_party_df['Numurs'] <= 5]
    total_top25_candidates = top25_df.shape[0]
    if total_top25_candidates > 0:
        female_top25_candidates = top25_df[top25_df['Gender'] == 'Female'].shape[0]
        percent_females_top25.append((female_top25_candidates / total_top25_candidates) * 100)
    else:
        percent_females_top25.append(0)  # No elected candidates in this case
    
    
    
        

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the percentage of female candidates
plt.plot(years, percent_females, 'ko-', label='Percentage of Female Candidates')

# Plot the percentage of female elected candidates
plt.plot(years, percent_females_elected, 'bo-', label='Percentage of Female Elected Candidates')

# Plot the percentage of female elected candidates
plt.plot(years, percent_females_big_party, 'go-', label='Percentage of Female >5% Party Candidates')


# Plot the percentage of female elected candidates
plt.plot(years, percent_females_top25, 'ro-', label='Percentage of Female Top 25 Candidates')


# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Percentage (%)')
plt.title('Percentage of Female Candidates and Elected Candidates')
plt.legend(loc='best')

# Set the x-ticks and corresponding labels
plt.xticks(ticks=years, labels=custom_labels)


# Add gridlines only for these specific years
plt.grid(which='both', axis='x')



# Show the plot
plt.grid(True)
plt.show()


