import pandas as pd
import bar_chart_race as bcr
df=pd.read_csv("World_Muslim_Population _Dataset.csv")
# Assuming your DataFrame is named 'df' and contains the necessary columns, including 'Growth_Rate' and 'Country Name'.

# Step 1: Sort the DataFrame by 'Growth_Rate' in descending order and select the top 20 countries
top_20_growth_countries = df.nlargest(20, 'Growth_Rate')

# Step 2: Create the bar chart race
bcr.bar_chart_race(
    df=top_20_growth_countries,
    filename='bar_chart_race.mp4',  # Output filename (change as needed)
    orientation='h',               # Horizontal orientation for bars
    sort='desc',                   # Sort bars in descending order
    n_bars=10,                     # Number of bars to display at a time
    title='Top 20 Countries with Highest Growth Rates',  # Title for the chart
    label_bars=True,               # Show labels for bars
    steps_per_period=10            # Number of steps (frames) for each period
)
