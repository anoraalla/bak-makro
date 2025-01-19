import pandas as pd

def main():
    df = pd.read_csv('kandidatiZemgaleFinal.csv')
    unique_values = df['Struktūrvienība'].unique()
    filtered_values = [value for value in unique_values if not value[0].isdigit()]
    print(filtered_values)

    novads = {
        'Rīga': ['Rīga', 'Ārzemes'],
        'Vidzeme': ['Jūrmala', 
                    'Alūksnes novads', 
                    'Ādažu novads', 
                    'Cēsu novads', 
                    'Gulbenes novads', 
                    'Ķekavas novads', 
                    'Limbažu novads', 
                    'Madonas novads', 
                    'Mārupes novads', 
                    'Ogres novads', 
                    'Olaines novads', 
                    'Ropažu novads', 
                    'Salaspils novads', 
                    'Saulkrastu novads', 
                    'Siguldas novads', 
                    'Smiltenes novads', 
                    'Valkas novads', 
                    'Valmieras novads', 
                    'Varakļānu novads'],
        'Latgale': ['Daugavpils', 
                    'Rēzekne', 
                    'Augšdaugavas novads', 
                    'Balvu novads',
                    'Krāslavas novads', 
                    'Līvānu novads', 
                    'Ludzas novads', 
                    'Preiļu novads', 
                    'Rēzeknes novads'], 
        'Kurzeme': ['Liepāja', 
                    'Ventspils', 
                    'Dienvidkurzemes novads', 
                    'Kuldīgas novads', 
                    'Saldus novads', 
                    'Talsu novads', 
                    'Ventspils novads'], 
        'Zemgale': ['Jelgava', 
                    'Aizkraukles novads', 
                    'Bauskas novads', 
                    'Dobeles novads', 
                    'Jelgavas novads', 
                    'Jēkabpils novads', 
                    'Tukuma novads']
    }


if __name__ == '__main__':
    main()
