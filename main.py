import sys
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Load data from file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data.split('\n')

# Parse data into a list of dictionaries
def parse_data(data):
    currencyRates = []
    for line in data:
        if line.startswith('<Obs'):
            line = line.split('\"')
            currencyRates.append({'date': line[1], 'rate': line[3]})
    return currencyRates

# Convert data to DataFrame
def create_dataframe(currencyRates):
    df = pd.DataFrame(currencyRates)
    df['date'] = pd.to_datetime(df['date'])
    df['rate'] = pd.to_numeric(df['rate'])
    return df

# Calculate expected rate using Taylor approximation
def expected_rate(df, N, starting_value):
    average_gradient = (df['rate'][starting_value-1] - df['rate'][starting_value-1-N]) / float(N)
    average_curvature = (average_gradient - (df['rate'][starting_value - 4*N] - df['rate'][starting_value - 3*N]) / float(N)) / 3.0
    expected = df['rate'][starting_value-1] + average_gradient + average_curvature / 2.0
    return expected

# Calculate deltas for different values of N
def calculate_deltas(df):
    delta_pair = {}
    for N in range(1, 11):
        delta_list = []
        for k in range(4*N, 181):
            delta_list.append(df['rate'][k] - expected_rate(df, N, k))
        average_delta = sum(delta_list) / len(delta_list)
        delta_pair[N] = average_delta
    return delta_pair

# Calculate naive average delta
def calculate_naive_delta(df, best_N):
    delta_list = []
    for k in range(4*best_N, 181):
        delta_list.append(df['rate'][k] - df['rate'][k-1])
    average_delta = sum(delta_list) / len(delta_list)
    return average_delta

# Main function to run the analysis
def main(file_path):
    data = load_data(file_path)
    currencyRates = parse_data(data)
    df = create_dataframe(currencyRates)

    delta_pair = calculate_deltas(df)
    for N in range(1, 11):
        print(f"N: {N} Delta: {delta_pair[N]}")
    
    best_N = min(delta_pair, key=delta_pair.get)
    print(f"The best N is: {best_N}")
    
    naive_delta = calculate_naive_delta(df, best_N)
    print(f"The naive average delta is: {naive_delta}")

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['rate'], label='Rate')
    plt.title('Currency Rate Over Time')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main('usd')
