import lightningchart as lc
import pandas as pd

# Set the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'global-temperature-anomalies-by-month.csv'
data = pd.read_csv(file_path)

# Filter data for years 1991 to 2023
data = data[(data['Year'] >= 1991) & (data['Year'] <= 2023)]

# Prepare the dashboard
dashboard = lc.Dashboard(
    columns=4,
    rows=3,
    theme=lc.Themes.Dark
)

# Define the months
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# Loop through each month and create a bar chart
for i, month in enumerate(months):
    month_data = data[data['Entity'] == month]

    # Sort the data by Year to ensure 1991 is on the left and 2023 is on the right
    month_data = month_data.sort_values(by='Year')

    # Prepare the bar chart data
    bar_data = [
        {'category': str(int(row['Year'])), 'value': float(row['Temperature anomaly'])}
        for _, row in month_data.iterrows()
    ]

    # Create a bar chart
    chart = dashboard.BarChart(
        column_index=i % 4,
        row_index=i // 4,
        row_span=1,
        column_span=1
    )
    chart.set_sorting('disabled')
    chart.set_title(f'{month} Temperature Anomalies (1991-2023)')
    chart.set_data(bar_data)
    

# Open the dashboard
dashboard.open()