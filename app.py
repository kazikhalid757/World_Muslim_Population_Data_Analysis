import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate the 5-year differences
def calculate_5_year_differences(row):
    return [row[i+5] - row[i] if i+5 < len(row) else None for i in range(len(row))]

# Function to create the line chart for a selected country
def plot_growth_rate(country_name):
    country_data = data[data['Country Name'] == country_name].values[0]
    years = data.columns[2:-1]
    growth_rate = country_data[2:-1]
    five_year_diff = calculate_5_year_differences(growth_rate)
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, growth_rate, marker='o', label='Growth Rate')
    plt.plot(years[4:], five_year_diff[4:], marker='o', label='5-Year Difference')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate')
    plt.title(f'Growth Rate for {country_name}')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)

# Main Streamlit app
def main():
    st.title('Country Growth Rate Visualization')
    
    # Dropdown to select the country
    country_list = data['Country Name'].unique().tolist()
    selected_country = st.selectbox('Select a country', country_list)
    
    # Display the line chart for the selected country
    plot_growth_rate(selected_country)

if __name__ == '__main__':
    main()
