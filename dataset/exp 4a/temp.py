import pandas as pd

print("\n----- EX. NO: 4 (a) - Temperature Analysis -----")

data_a = {
    'City': ['Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi', 'Chennai'],
    'Date': pd.to_datetime(['2024-06-10', '2024-06-15', '2024-06-20', 
                            '2024-07-05', '2024-07-10', '2024-07-15', 
                            '2024-08-01', '2024-08-05', '2024-08-10']),
    'Temperature': [34, 38, 35, 33, 39, 36, 32, 40, 34]
}

df_a = pd.DataFrame(data_a)
df_a['Month'] = df_a['Date'].dt.strftime('%B')
monthly_temp_sum = df_a.groupby(['City', 'Month'])['Temperature'].sum().reset_index()
pivot_a = monthly_temp_sum.pivot(index='City', columns='Month', values='Temperature').fillna(0)

print("\nMonth-wise Temperature Summary:")
print(pivot_a)

summer_months = ['June', 'July', 'August']
pivot_a['Summer Total'] = pivot_a[summer_months].sum(axis=1)
highest_city = pivot_a['Summer Total'].idxmax()
print(f"\nCity with highest total summer temperature: {highest_city}")

