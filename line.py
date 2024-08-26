import lightningchart as lc
import pandas as pd

# Read the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'Land Ocean Temperature Index.xlsx'
data = pd.read_excel(file_path)

# Extract values
x_values = data['Year'].tolist()
y_values_no_smoothing = data['No_Smoothing'].tolist()
y_values_lowess = data['Lowess(5)'].tolist()

# Create the chart
chart = lc.ChartXY(
    theme=lc.Themes.Dark,
    title='GLOBAL LAND-OCEAN TEMPERATURE INDEX'
)

# Add No_Smoothing series
no_smoothing_series = chart.add_line_series()
no_smoothing_series.add(x_values, y_values_no_smoothing)
no_smoothing_series.set_name('No Smoothing')
no_smoothing_series.set_line_color(lc.Color(0, 128, 255))
no_smoothing_series.set_line_thickness(2) 

no_smoothing_points = chart.add_point_series()
no_smoothing_points.add(x_values, y_values_no_smoothing)
no_smoothing_points.set_name('No Smoothing Points')
no_smoothing_points.set_point_shape('circle')
no_smoothing_points.set_point_color(lc.Color(0, 255, 255))
no_smoothing_points.set_point_size(6)

# Add Lowess(5) series
lowess_series = chart.add_line_series()
lowess_series.add(x_values, y_values_lowess)
lowess_series.set_name('Lowess(5)')
lowess_series.set_line_color(lc.Color(255, 255, 0))
lowess_series.set_line_thickness(2)

lowess_points = chart.add_point_series()
lowess_points.add(x_values, y_values_lowess)
lowess_points.set_name('Lowess(5) Points')
lowess_points.set_point_shape('circle')
lowess_points.set_point_color(lc.Color(255, 225, 0))
lowess_points.set_point_size(6)

# Customize x-axis
x_axis = chart.get_default_x_axis()
x_axis.set_title('Year')

# Customize y-axis
y_axis = chart.get_default_y_axis()
y_axis.set_title('Temperature Anomaly (C)')

# Customize chart appearance
legend = chart.add_legend()
legend.add(no_smoothing_series)
legend.add(lowess_series)
legend.add(no_smoothing_points)
legend.add(lowess_points)

# Open the chart
chart.open()
