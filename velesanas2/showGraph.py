import pandas as pd
import matplotlib.pyplot as plt


def get_party_dictionary():
    csv_data = """
    Apgabals,Nr.,Party,Votes,Percentage,Seats
    Riga,1,"1. Jaunā VIENOTĪBA ",61137,"20,59%",11
    Riga,2,"2. Latvijas Krievu savienība ",14106,"4,75%",0
    Riga,3,"3. Zaļo un Zemnieku savienība ",16371,"5,51%",3
    Riga,4,"4. TAUTAS KALPI LATVIJAI ",2572,"0,87%",0
    Riga,5,"5. SUVERĒNĀ VARA ",14918,"5,02%",0
    Riga,6,"6. Kristīgi Progresīvā Partija ",462,"0,16%",0
    Riga,7,"7. ""Saskaņa"" sociāldemokrātiskā partija ",19713,"6,64%",0
    Riga,8,"8. Politiskā partija ""Stabilitātei!"" ",27172,"9,15%",5
    Riga,9,"9. Politiskā partija ""Tautas varas spēks"" ",4412,"1,49%",0
    Riga,10,"10. Partija ""Vienoti Latvijai"" ",399,"0,13%",0
    Riga,11,"11. Nacionālā apvienība ""Visu Latvijai!""-""Tēvzemei un Brīvībai/LNNK"" ",21200,"7,14%",4
    Riga,12,"12. LATVIJA PIRMAJĀ VIETĀ ",25518,"8,59%",4
    Riga,13,"13. Konservatīvie ",8067,"2,72%",0
    Riga,14,"14. Politiskā partija ""KATRAM UN KATRAI"" ",13737,"4,63%",0
    Riga,15,"15. ""PROGRESĪVIE"" ",26881,"9,05%",5
    Riga,16,"16. Attīstībai/Par! ",11564,"3,89%",0
    Riga,17,"17. ""Apvienība Latvijai"" ",906,"0,31%",0
    Riga,18,"18. ""APVIENOTAIS SARAKSTS - Latvijas Zaļā partija, Latvijas Reģionu Apvienība, Liepājas partija"" ",20513,"6,91%",4
    Riga,19,"19. Politiskā partija ""Republika"" ",4447,"1,50%",0
    """
    
    # Load the CSV data into a DataFrame
    from io import StringIO
    data = pd.read_csv(StringIO(csv_data))
    
    # Create the dictionary
    votes_dict = {row['Party'].strip(): row['Votes'] for index, row in data.iterrows()}
    # print(votes_dict)
    return votes_dict

# Read the CSV file
data = pd.read_csv('kandidatiRigaFinal.csv')

pdict = get_party_dictionary()

# Regex pattern to match strings that start with a number followed by a dot and a space
pattern = r'^\d+\. .+'

# Filter the DataFrame
data = data[data['Struktūrvienība'].str.match(pattern, na=False)]

# Calculate the difference between Pluses and Minuses
data['Difference'] = (data['Pluses'] - data['Minuses'])

print(data['Difference'])


# Group by Party and Gender and calculate the mean difference
avg_diff_female = data[data['Gender'] == 'Female'].groupby('Party')['Difference'].mean()
avg_diff_male = data[data['Gender'] == 'Male'].groupby('Party')['Difference'].mean()
avg_diff_overall = data.groupby('Party')['Difference'].mean()

# Combine into a single DataFrame
result = pd.DataFrame({
    'Female': avg_diff_female,
    'Male': avg_diff_male,
    'Overall': avg_diff_overall
}).reset_index()

# Plotting the results
labels = result['Party']
female_means = result['Female']
male_means = result['Male']
overall_means = result['Overall']

x = range(len(labels))  # X axis positions for each group
width = 0.25  # Width of the bars

fig, ax = plt.subplots()

# Create bar charts for each category
bars_female = ax.barh([x - width for x in x], female_means, width, label='Female')
bars_male = ax.barh(x, male_means, width, label='Male')
bars_overall = ax.barh([x + width for x in x], overall_means, width, label='Overall', color='gray')

# Add some text for labels, title, and axes ticks
ax.set_xlabel('Average Difference (Pluses - Minuses)')
ax.set_ylabel('Party')
ax.set_title('Average Difference between Pluses and Minuses by Gender and Party')
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()