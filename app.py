import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Replace this with your actual dataset
data = pd.read_csv("World_Muslim_Population _Dataset.csv")

# Function to create the line chart for a selected country
def plot_growth_rate(country_name):
    country_data = data[data['Country Name'] == country_name].values[0]
    years = data.columns[2:-1]
    growth_rate = country_data[2:-1]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, growth_rate, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate')
    plt.title(f'Growth Rate for {country_name}')
    plt.xticks(rotation=45)

    # Annotate each data point with its growth rate value
    for x, y in zip(years, growth_rate):
        plt.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

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
