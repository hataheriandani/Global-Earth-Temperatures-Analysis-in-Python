import pandas as pd
import lightningchart as lc
from lightningchart import Color, Themes

# Set the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'country-level-monthly-temperature-anomalies.csv'
data = pd.read_csv(file_path)

# List of Asian country codes (ISO A3)
asian_countries = [
    'AFG', 'ARM', 'AZE', 'BHR', 'BGD', 'BRN', 'KHM', 'CHN', 'CYP', 'DEU','UGA',
    'DJI', 'EGY', 'ERI', 'ETH', 'GEO', 'HKG', 'IND', 'IRL', 'ISR', 'JPN','GNQ','KEN','PNG',
    'JOR', 'KOR', 'KWT', 'LAO', 'LBN', 'MAC', 'MDV', 'MNG', 'MMR', 'MYS','KGZ','SOM','BTN',
    'NPL', 'OMN', 'PAK', 'PHL', 'QAT', 'SAU', 'SGP', 'SRI', 'SYR', 'TJK','PRK','ARE','LKA',
    'TKM', 'TLS', 'TUR', 'TWN', 'UZB', 'VNM', 'YEM', 'IRN', 'IRQ', 'KAZ','IDN','THA','RUS'
]

# Function to create a map chart for a given year and month for Asia
def create_asia_map_chart(data, year):
    # Filter data for the given year and only for Asian countries
    data_year = data[(data['Year'] == year) & (data['Code'].isin(asian_countries))]
    data_year = data_year[['Code', 'March']].rename(columns={'Code': 'ISO_A3', 'March': 'value'})

    # Create the MapChart for Asia
    chart = lc.MapChart(map_type='Asia', theme=lc.Themes.White)

    # Set temperature anomaly data
    chart.invalidate_region_values(data_year.to_dict(orient='records'))

    # Set title with year
    chart.set_title(f"Temperature Anomalies - March {year}")

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

# Create and display the map chart for the year 1990
create_asia_map_chart(data, 2024)
