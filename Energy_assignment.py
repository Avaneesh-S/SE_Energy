import pandas as pd

# Read data from CSV file
df = pd.read_csv('energy_data.csv')

# Define a function to calculate the total energy consumption per month
def calculate_total_energy_consumption_per_month():
    # Convert date column to datetime object
    df['date'] = pd.to_datetime(df['date'])

    # Add columns for year and month
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    # Group the data by year and month and calculate the total energy consumption
    monthly_energy_consumption = df.groupby(['year', 'month'])['energy_consumption'].sum()

    return monthly_energy_consumption

# Calculate the average energy consumption per day
df['energy_consumption_per_day'] = df['energy_consumption'] / 24
average_energy_consumption_per_day = df['energy_consumption_per_day'].mean()
print(f"Average energy consumption per day: {average_energy_consumption_per_day}")

# Calculate the total energy consumption per month
monthly_energy_consumption = calculate_total_energy_consumption_per_month()
print(monthly_energy_consumption)




