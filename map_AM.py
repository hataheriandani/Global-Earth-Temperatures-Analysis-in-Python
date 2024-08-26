import pandas as pd
import lightningchart as lc
from lightningchart import Color, Themes

# Set the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'country-level-monthly-temperature-anomalies.csv'
data = pd.read_csv(file_path)

# List of North American country codes (ISO A3)
north_american_countries = [
    'ATG', 'BHS', 'BRB', 'BLZ', 'CAN', 'CUB', 'DMA', 'SLV', 'GTM', 'GRD','DOM','PRI',
    'HND', 'JAM', 'MEX', 'NIC', 'PAN', 'KNA', 'LCA', 'VCT', 'TTO','USA','GRL','HTI'
]

# List of South American country codes (ISO A3)
south_american_countries = [
    'ARG', 'BOL', 'BRA', 'CHL', 'COL', 'ECU', 'GUY', 'PRY', 'PER', 'SUR','NIC','PAN',
    'URY', 'VEN','CRI','HND','SLV','TTO','GTM'
]

# Function to create a map chart for North America
def create_north_america_map_chart(data, year):
    # Filter data for the given year and only for North American countries
    data_year = data[(data['Year'] == year) & (data['Code'].isin(north_american_countries))]
    data_year = data_year[['Code', 'March']].rename(columns={'Code': 'ISO_A3', 'March': 'value'})

    # Create the MapChart for North America
    chart = lc.MapChart(map_type='NorthAmerica', theme=lc.Themes.White)

    # Set temperature anomaly data
    chart.invalidate_region_values(data_year.to_dict(orient='records'))

    # Set title with year
    chart.set_title(f"Temperature Anomalies - March {year} - North America")

    # Set a detailed color palette with 10 colors
    chart.set_palette_colors(
        steps=[
            {'value': -2, 'color': Color('#00008B')},
            {'value': -1, 'color': Color('#0000FF')},
            {'value': 0, 'color': Color('#4169E1')},
            {'value':  0.5, 'color': Color('#87CEEB')},
            {'value': 1, 'color': Color('#ADD8E6')},
            {'value': 1.5, 'color': Color('#B0E0E6')},
            {'value': 2, 'color': Color('#FFDAB9')},
            {'value': 2.5, 'color': Color('#FFA07A')},
            {'value': 3, 'color': Color('#FF4500')},
            {'value': 3.5, 'color': Color('#FF0000')},
            {'value': 4, 'color': Color('#8B0000')}
        ],
        look_up_property='value',
        percentage_values=False
    )

    # Enable hover highlighting
    chart.set_highlight_on_hover(enabled=True)

    # Add legend
    legend = chart.add_legend(horizontal=True, title=f"March Temperature Anomaly - Year: {year}", data=chart)
    legend.set_font_size(10)  # Adjust font size as needed

    # Open the chart in live mode
    chart.open(live=True)

    return chart

# Function to create a map chart for South America
def create_south_america_map_chart(data, year):
    # Filter data for the given year and only for South American countries
    data_year = data[(data['Year'] == year) & (data['Code'].isin(south_american_countries))]
    data_year = data_year[['Code', 'March']].rename(columns={'Code': 'ISO_A3', 'March': 'value'})

    # Create the MapChart for South America
    chart = lc.MapChart(map_type='SouthAmerica', theme=lc.Themes.White)

    # Set temperature anomaly data
    chart.invalidate_region_values(data_year.to_dict(orient='records'))

    # Set title with year
    chart.set_title(f"Temperature Anomalies - March {year} - South America")

    # Set a detailed color palette with 10 colors
    chart.set_palette_colors(
        steps=[
            {'value': -2, 'color': Color('#00008B')},
            {'value': -1, 'color': Color('#0000FF')},
            {'value': 0, 'color': Color('#4169E1')},
            {'value':  0.5, 'color': Color('#87CEEB')},
            {'value': 1, 'color': Color('#ADD8E6')},
            {'value': 1.5, 'color': Color('#B0E0E6')},
            {'value': 2, 'color': Color('#FFDAB9')},
            {'value': 2.5, 'color': Color('#FFA07A')},
            {'value': 3, 'color': Color('#FF4500')},
            {'value': 3.5, 'color': Color('#FF0000')},
            {'value': 4, 'color': Color('#8B0000')}
        ],
        look_up_property='value',
        percentage_values=False
    )

    # Enable hover highlighting
    chart.set_highlight_on_hover(enabled=True)

    # Add legend
    legend = chart.add_legend(horizontal=True, title=f"March Temperature Anomaly - Year: {year}", data=chart)
    legend.set_font_size(10)  # Adjust font size as needed

    # Open the chart in live mode
    chart.open(live=True)

    return chart

# Create and display the map charts for the year 1990
create_north_america_map_chart(data, 2024)
create_south_america_map_chart(data, 2024)
