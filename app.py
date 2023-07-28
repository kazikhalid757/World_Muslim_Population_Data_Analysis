import pandas as pd
import bar_chart_race as bcr


start_year = '1960'
end_year = '2021'

# Step 2: Read the CSV data
df = pd.read_csv("World_Muslim_Population _Dataset.csv")

# Step 3: Calculate the growth rate for each country
def calculate_growth_rate(row):
    initial_value = row[start_year]
    final_value = row[end_year]
    return ((final_value - initial_value) / initial_value) * 100

# Step 4: Apply the function to create a new column for the growth rate
df['Growth_Rate'] = df.apply(calculate_growth_rate, axis=1)

# Step 5: Sort the DataFrame by 'Growth_Rate' in descending order and select the top 20 countries
top_20_growth_countries = df.nlargest(20, 'Growth_Rate')

# Step 6: Create the bar chart race
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
