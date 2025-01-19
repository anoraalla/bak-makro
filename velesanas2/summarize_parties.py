import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys


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

def get_voters(district): 
    big_parties_by_district = dict()
    big_parties_by_district['R'] = [(1, "Vienotība", 61137), (3, "ZZS", 16371), (8, "Stabilitātei!", 27172), 
        (11, "NA", 21200), (12, "LPV", 25518), (15, "Progresīvie", 26881), (18, "AS", 20513)]
    big_parties_by_district['V'] = [(1, "Vienotība", 61485), (3, "ZZS", 31711), (8, "Stabilitātei!", 7978), 
        (11, "NA", 29861), (12, "LPV", 13473), (15, "Progresīvie", 15591), (18, "AS", 33078)]
    big_parties_by_district['L'] = [(1, "Vienotība", 7747), (3, "ZZS", 16157), (8, "Stabilitātei!", 20634), 
        (11, "NA", 6428), (12, "LPV", 7259), (15, "Progresīvie", 2735), (18, "AS", 5693)]
    big_parties_by_district['K'] = [(1, "Vienotība", 18879), (3, "ZZS", 24230), (8, "Stabilitātei!", 2487), 
        (11, "NA", 11768), (12, "LPV", 4907), (15, "Progresīvie", 5512), (18, "AS", 25329)]
    big_parties_by_district['Z'] = [(1, "Vienotība", 24177), (3, "ZZS", 25207), (8, "Stabilitātei!", 3897), 
        (11, "NA", 15682), (12, "LPV", 5876), (15, "Progresīvie", 5608), (18, "AS", 16018)]    
    return big_parties_by_district[district]


# Not really needed
def get_total_voters(District, PartyNum): 
    big_parties_by_district = dict()
    big_parties_by_district['Rīga'] = [(1, "Vienotība", 61137), (3, "ZZS", 16371), (8, "Stabilitātei!", 27172), 
        (11, "NA", 21200), (12, "LPV", 25518), (15, "Progresīvie", 26881), (18, "AS", 20513)]
    big_parties_by_district['Vidzeme'] = [(1, "Vienotība", 61485), (3, "ZZS", 31711), (8, "Stabilitātei!", 7978), 
        (11, "NA", 29861), (12, "LPV", 13473), (15, "Progresīvie", 15591), (18, "AS", 33078)]
    big_parties_by_district['Latgale'] = [(1, "Vienotība", 7747), (3, "ZZS", 16157), (8, "Stabilitātei!", 20634), 
        (11, "NA", 6428), (12, "LPV", 7259), (15, "Progresīvie", 2735), (18, "AS", 5693)]
    big_parties_by_district['Kurzeme'] = [(1, "Vienotība", 18879), (3, "ZZS", 24230), (8, "Stabilitātei!", 2487), 
        (11, "NA", 11768), (12, "LPV", 4907), (15, "Progresīvie", 5512), (18, "AS", 25329)]
    big_parties_by_district['Zemgale'] = [(1, "Vienotība", 24177), (3, "ZZS", 25207), (8, "Stabilitātei!", 3897), 
        (11, "NA", 15682), (12, "LPV", 5876), (15, "Progresīvie", 5608), (18, "AS", 16018)]  
    
    sublist = big_parties_by_district[District]
    result = 1000
    for triple in sublist:
        if triple[0] == PartyNum:
            result = triple[2]
    return result
    


def filter(data, district_name):
    # Filter rows where 'Struktūrvienība' equals to the given district_name (Rīga, Vidzeme etc.)
    filtered_data = data[data['Struktūrvienība'] == district_name]
    
    # Save the filtered data to a CSV file
    # filtered_data.to_csv('temp.csv', index=False)
    
    return filtered_data

def filter_large_parties(data):
    filtered_data = data[data['PartyNumber'].isin([1,3,8,11,12,15,18])]
    return filtered_data



def get_party_number(party_name): 
    items = party_name.split('.')
    return int(items[0])


def summarize_party_data(data, district_name):
    # Initialize a list to store summary rows
    summary_rows = []
    
    # Get list of unique parties
    unique_parties = data['Party'].unique()
    
    # Iterate over each party to calculate statistics
    for party in unique_parties:
        # Filter data for the current party
        party_data = data[data['Party'] == party]
        
        # Calculate number of males and females
        num_males = party_data[party_data['Gender'] == 'Male'].shape[0]
        num_females = party_data[party_data['Gender'] == 'Female'].shape[0]
        
        # Calculate sums for males
        sum_pluses_males = party_data[party_data['Gender'] == 'Male']['Pluses'].sum()
        sum_minuses_males = party_data[party_data['Gender'] == 'Male']['Minuses'].sum()
        
        # Calculate sums for females
        sum_pluses_females = party_data[party_data['Gender'] == 'Female']['Pluses'].sum()
        sum_minuses_females = party_data[party_data['Gender'] == 'Female']['Minuses'].sum()
        
        party_num = get_party_number(party)
        
        # Create a dictionary summarizing the current party's data
        summary_row = {
            'District': district_name,
            'PartyName': party,
            'PartyNumber': party_num,
            'numMales': num_males,
            'numFemales': num_females,
            'sumPlusesMales': sum_pluses_males,
            'sumMinusesMales': sum_minuses_males,
            'sumPlusesFemales': sum_pluses_females,
            'sumMinusesFemales': sum_minuses_females
        }
        
        # Append the dictionary to the list of summary rows
        summary_rows.append(summary_row)
        
    # Convert the summary rows list into a DataFrame
    summary_df = pd.DataFrame(summary_rows)
    
    return summary_df


def plot_party_districts(data, party_number):
    plt.rcParams['font.family'] = 'Times New Roman'
    # Filter the data for the given PartyNumber
    filtered_data = data[data['PartyNumber'] == party_number]
    
    # Calculate the expressions for each district
    filtered_data['expression_1'] = (
        (filtered_data['sumPlusesMales'] - filtered_data['sumMinusesMales']) / (filtered_data['numMales']*filtered_data['totalVoters'] ) - 
        (filtered_data['sumPlusesFemales'] - filtered_data['sumMinusesFemales']) / (filtered_data['numFemales']*filtered_data['totalVoters'])
    )
    
    filtered_data['expression_2'] = (
        filtered_data['sumMinusesFemales'] / (filtered_data['numFemales']*filtered_data['totalVoters']) - 
        filtered_data['sumMinusesMales'] / (filtered_data['numMales']*filtered_data['totalVoters'])
    )
    
    districts = filtered_data['District']
    expression_1_values = filtered_data['expression_1']
    expression_2_values = filtered_data['expression_2']
    
    # Define pastel colors for the districts
    pastel_colors = ['lightcoral', 'lightblue', 'lightgreen', 'khaki', 'mediumaquamarine', 'thistle', 'lavender']
    

    num_bars = len(districts)
    bar_height = 0.5  # Each bar should be 0.25 inches tall
    space_between_bars = 0.2  # Each space should be 0.375 inches
    total_height_in_inches = num_bars * (bar_height + space_between_bars)

    # Set up the subplots
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, total_height_in_inches), sharey=True)

    short_names = {1:'Vienotība', 3:'ZZS', 8:'Stabilitātei!', 11: 'NA', 12:'LPV', 15:'Progresīvie', 18: 'AS'}

    # Plot the first expression as a horizontal bar chart
    axes.barh(districts, expression_1_values, 
              # color=pastel_colors[:len(districts)],
              color = '#9BBB59',
              edgecolor='black', height=bar_height)
    axes.set_title(f'Male-Female Candiate Support Difference for Party {short_names[party_number]}',
                   fontname='Times New Roman', fontsize=14, fontweight='bold')
    axes.set_xlabel('Support for an Average Male Minus Support for an Average Female',
                    fontname='Times New Roman', fontsize=12, fontweight='normal')
    axes.set_ylabel('Electoral District', 
                    fontname='Times New Roman', fontsize=12, fontweight='normal')
    
    # Plot the second expression as a horizontal bar chart
    # axes[1].barh(districts, expression_2_values, color=pastel_colors[:len(districts)], edgecolor='black', height=0.8)
    # axes[1].set_title('Average FemaleMinuses-MaleMinuses')
    # axes[1].set_xlabel('Value')


    # Set custom font size for tick labels
    axes.xaxis.set_tick_params(labelsize=10)  # 10pt font for x-axis tick labels
    axes.yaxis.set_tick_params(labelsize=12)  # 12pt font for y-axis tick labels


    # Set major and minor ticks
    axes.xaxis.set_major_locator(ticker.MultipleLocator(0.01))
    axes.xaxis.set_minor_locator(ticker.MultipleLocator(0.002))

    # Enable grid
    axes.grid(True, which='major', linestyle='--', linewidth=1.0)
    axes.grid(True, which='minor', linestyle='--', linewidth=0.5)

    axes.set_xlim(-0.046, 0.052)
    
    # Adjust the layout to prevent overlap
    plt.tight_layout()
        
    plt.savefig(f'chart_{short_names[party_number]}.png')
    
    # Display the plots
    plt.show()

def add_total_voters_column(data):
    # Define the new column by applying the get_total_voters function
    data['totalVoters'] = data.apply(lambda row: get_total_voters(row['District'], row['PartyNumber']), axis=1)
    return data



def main():
    data_files = [('R', 'kandidatiRigaFinalShort.csv'), ('V', 'kandidatiVidzemeFinal.csv'), ('L', 'kandidatiLatgaleFinal.csv'), ('K', 'kandidatiKurzemeFinal.csv'), ('Z', 'kandidatiZemgaleFinal.csv')]
    
    district_names = {'R': "Rīga", "V": "Vidzeme", "L": "Latgale", "K": "Kurzeme", "Z": "Zemgale"}
    

    big_summary = []
    for (key, file_name) in data_files:
        data = pd.read_csv(file_name)
        print(f'data rows for {key} is {len(data)}')
    
        pdict = get_party_dictionary()
        
        # Only read those lines, which represent the entire "Kurzeme", "Rīga" and so on. Ignore individual polling stations and cities.
        filtered_data = filter(data, district_names[key])
        print(f'filtered_data rows for {key} is {len(data)}')
        
        summary_data = summarize_party_data(filtered_data, district_names[key])
        
        large_party_summaries = filter_large_parties(summary_data)
        
        print(f'large_party_summaries = ') 
        print(f'{large_party_summaries}')
        
        big_summary.append(large_party_summaries)
        
    df_combined = pd.concat(big_summary, ignore_index=True)
        
    df_combined = add_total_voters_column(df_combined)
    df_combined.to_csv(f'big_summary.csv', index=False)

    plot_party_districts(df_combined, 1)
    plot_party_districts(df_combined, 3)
    plot_party_districts(df_combined, 8)
    plot_party_districts(df_combined, 11)
    plot_party_districts(df_combined, 12)
    plot_party_districts(df_combined, 15)
    plot_party_districts(df_combined, 18)
    
    
    
if __name__ == '__main__':
    main()