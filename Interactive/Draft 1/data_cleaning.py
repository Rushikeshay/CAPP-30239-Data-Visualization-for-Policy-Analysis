import pandas as pd 
# data 
index_df = pd.read_csv('democracy-index-eiu/democracy-index-eiu.csv')
protest_df = pd.read_excel('Global Protest Tracker.xlsx')

protest_df['Country'].nunique()
index_df['Entity'].nunique()

index_df.columns
protest_df.columns

# rename entity to country 
index_df.rename(columns={'Entity': 'Country'}, inplace=True)

# rename map 
rename_map = {
    "Czech Republic": "Czechia",
    "Democratic Republic of the Congo": "Democratic Republic of Congo",
    "Gaza Strip": "Palestine",
    "Indian Kashmit": "India",  
    "Republic of Ireland": "Ireland",
    "The Gambia": "Gambia",
    "Türkiye": "Turkey",
    "West Bank": "Palestine",
    "Cote d'Ivoire": "Ivory Coast",
    "Indian Kashmir": "India",
    "Transnistria": "Moldova", 
}

# apply renames to both
index_df['Country'] = index_df['Country'].replace(rename_map)
protest_df['Country'] = protest_df['Country'].replace(rename_map)

# recompute missing
missing_countries = set(protest_df['Country'].unique()) - set(index_df['Country'].unique())
missing_countries

# keep only countries also in protest_df
index_df = index_df[index_df['Country'].isin(protest_df['Country'])]

# check again
index_df['Country'].nunique()
protest_df['Country'].nunique()


import re

def extract_year(val):
    match = re.search(r"\d+", str(val))
    return match.group(0) if match else None

def extract_month(val):
    match = re.search(r"[A-Za-z]{3}", str(val))
    return match.group(0).title() if match else None

def year2_to_year4(y):
    if pd.isna(y):
        return None
    y = int(y)
    return 2000 + y if y <= 29 else 1900 + y

protest_df['Year_2digit'] = protest_df['Start Date'].apply(extract_year)
protest_df['Year_4digit'] = protest_df['Year_2digit'].apply(year2_to_year4)
protest_df['Month'] = protest_df['Start Date'].apply(extract_month)
protest_df['MonthYear'] = protest_df['Month'] + "-" + protest_df['Year_2digit']

protest_df.head()
protest_df.columns

# save copies of both cleaned datasets as csv in local folder 
index_df.to_csv('cleaned_democracy_index.csv', index=False)
protest_df.to_csv('cleaned_global_protest_tracker.csv', index=False)

protest = pd.read_csv('cleaned_global_protest_tracker.csv')

# Aligning with the map data 

protest.loc[protest['Country'] == 'United States', 'Country'] = 'United States of America'
protest.loc[protest['Country'] == 'Central African Republic', 'Country'] = 'Central African Rep.'
protest.loc[protest['Country'] == 'South Sudan', 'Country'] = 'S. Sudan'
protest.loc[protest['Country'] == 'Democratic Republic of Congo', 'Country'] = 'Dem. Rep. Congo'

protest.to_csv('protest.csv', index=False)