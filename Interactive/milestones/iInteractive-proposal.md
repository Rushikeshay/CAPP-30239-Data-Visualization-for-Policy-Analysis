# Rushikesh Jadhav

## Description

Democratic values around the world are being challenged. Freedom of speech and protest are under threat in many places. I want to create a visualization exploring protests around the world and their motivations and triggers. I also want this visualization to show whether these protests led to policy changes or achieved their intended political or policy goals.

## Technical Plan re: Option A/B/C/D

### Option A
Create one large visualization with dropdown menus for geographic regions (countries/continents), motivators, and triggers. The user can explore the data to see descriptions of these protests such as their size, duration, and policy or political outcomes. This information can be presented using various visualizations, such as charts (for example, a bubble chart to show protest size).
d3-scale, d3-axis, d3-selection, d3-format, d3-array, d3-transition 

Motivations: 

1. https://carnegieendowment.org/features/global-protest-tracker?lang=en. this is also the data source. While they use a map, I don’t think it’s used effectively. I would rather keep only the dropdown menu and create more informative boxes and charts that go beyond simply summarizing protests.
2. https://acleddata.com/platform/conflict-index-dashboard. this tool helps visualize a few aspects of conflicts around the world by country. I like how it focuses on one specific aspect of the information. For me, that aspect could be the size of protests and whether there was an outcome or not.

OR

### Option C

A world map displaying protest information for each country. I can include hover or tooltip boxes with country details. I would like to take this further by showing country profiles below the map in separate boxes. I can also create a slider showing democracy index rankings or scores, allowing users to select countries based on their democratic standing and view policy or political outcomes at different stages. 
Libraries: MapLibreGL, Plotly or D3 + TopoJSON 

Motivatios: 

1. https://digitaldevelopmentcompass.undp.org/. I am currently interning here and our team created this tool. I like it because it really allows you to explore all the data at hand. 
2. https://www.undp.org/acceleratorlabs/peoplepowered/dataviz/SatoshiGaneko A similar country level tool. 


## Mockup
Here are two potential exmaples of my interactive tool. I believe my final tool will be a combination of both examples. 



## Data Sources

{
include 1-3 data sources with the following,
you may re-use data sources from before or switch topics
}

### Data Source 1: {Name}

URL: https://carnegieendowment.org/features/global-protest-tracker?lang=en 

Size: 930 rows, 20 columns

This dataset lists all recorded protests around the world reported by major English-language news sources. It categorizes them into four motivation categories and provides key information such as the number of protesters, duration, the nature of the police response, and, most importantly, the outcome.

URL: https://ourworldindata.org/grapher/democracy-index-eiu?time=2017..latest

Size: 3183 rows, 4 columns

This is the Global Democracy Index compiled by The Economist Intelligence Unit (EIU). It is one of the most widely used indicators for assessing the state of democracy across countries. The index evaluates nations based on criteria such as electoral processes, civil liberties, government functioning, political participation, and political culture. 

## Questions

{Numbered list of questions for course staff, if any.}

1. The Carnegie data, while very good on their website, has an issue when downloaded, the start_date column does not show the year of the protests. It only displays the day and month. On their website, however, the year is available. I need to find a way to include the year as well. Do you have any suggestions on how I could do that?
