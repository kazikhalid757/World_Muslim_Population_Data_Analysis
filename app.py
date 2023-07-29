import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Replace this with your actual dataset
data = pd.read_csv('your_data.csv')

# Function to create the line chart for a selected country
def plot_population(country_name):
    country_data = data[data['Country Name'] == country_name].values[0]
    years = data.columns[2:-1]
    population = country_data[2:-1]  # Exclude 'Growth_Rate' from population values
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, population, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(f'Population for {country_name}')
    plt.xticks(rotation=45)

    # Annotate each data point with its population value
    for x, y in zip(years, population):
        plt.annotate(f'{y:,}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    st.pyplot(plt)

# Main Streamlit app
def main():
    st.title('Country Population Visualization')
    
    # Dropdown to select the country
    country_list = data['Country Name'].unique().tolist()
    selected_country = st.selectbox('Select a country', country_list)
    
    # Display the line chart for the selected country
    plot_population(selected_country)

if __name__ == '__main__':
    main()
