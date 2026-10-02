import matplotlib.pyplot as plt

import pandas as pd


orders = pd.read_excel("data/List of Orders.xlsx")
details = pd.read_excel("data/Order Details.xlsx")

merged_data = pd.merge(orders, details, on='Order ID', how='inner')



state_analysis = merged_data.groupby('State').agg(
    Order_Count=('Order ID', 'nunique'),
    total_sales=('Amount', 'sum'),
    total_profit=('Profit', 'sum'),
).reset_index()


state_analysis['avg_profit'] = (state_analysis['total_profit'] / state_analysis['Order_Count']).round(2)


top_5_states = state_analysis.sort_values(by='Order_Count', ascending=False).head(5)

print("\n--- TOP 5 STATES WITH HIGHEST NUMBER OF ORDERS ---")
print(top_5_states.head(5))

# vizualization of top 5 states with highest number of orders

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot 1: Total Sales as a Bar Chart (Left Y-Axis)

ax1.bar(top_5_states['State'], top_5_states['total_sales'], color='skyblue', alpha=0.8)
ax1.set_xlabel('State', fontweight='bold')
ax1.set_ylabel('Total Sales Amount', color='tab:blue', fontweight='bold')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plot 2: Average Profit as a Line Chart (Right Y-Axis)

ax2 = ax1.twinx()  
ax2.plot(top_5_states['State'], top_5_states['avg_profit'], color='red', marker='o', linewidth=2.5, markersize=8)
ax2.set_ylabel('Average Profit per Order(%)', color='red', fontweight='bold')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Top 5 States: Total Sales vs. Average Profit', fontsize=14, fontweight='bold')
ax1.grid(axis='y', linestyle='--', alpha=0.4)


for i, val in enumerate(top_5_states['total_sales']):
    ax1.text(i, val + 1000, f'{int(val)}', ha='center', fontweight='bold', color='blue', fontsize=9)


for i, val in enumerate(top_5_states['avg_profit']):
    ax2.text(i, val + 3, f'{val:.2f}', ha='center', fontweight='bold', color='red', fontsize=9)

fig.tight_layout()

plt.show()

# Detail analysis of punjab 


punjab_data = merged_data[merged_data['State'] == 'Punjab']

print ("\n--- PUNJAB DATA INFO ---")
print(punjab_data.to_string())
print(punjab_data.shape)
print(punjab_data.columns.tolist())
print(punjab_data.isnull().sum())
print("------------------------")

city_breakdown = punjab_data.groupby('City').agg(
    Total_Sales=('Amount', 'sum'),
    Total_Profit=('Profit', 'sum')
).reset_index().sort_values('Total_Profit')

print("\n--- CITY BREAKDOWN FOR PUNJAB ---")
print(city_breakdown)

# Punjab City Analysis - Double Bar Chart
city_stats = punjab_data.groupby('City').agg(
    Total_Sales=('Amount', 'sum'),
    Avg_Profit=('Profit', 'mean')
).reset_index().sort_values('Total_Sales', ascending=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Bar 1: Total Sales
ax1.bar(city_stats['City'], city_stats['Total_Sales'], color='skyblue')
ax1.set_title('Total Sales by City', fontweight='bold')
ax1.set_xlabel('City')
ax1.set_ylabel('Total Sales')
ax1.tick_params(axis='x', rotation=45)

# Bar 2: Average Profit
colors = ['red' if x < 0 else 'green' for x in city_stats['Avg_Profit']]
ax2.bar(city_stats['City'], city_stats['Avg_Profit'], color=colors)
ax2.set_title('Avg Profit by City', fontweight='bold')
ax2.set_xlabel('City')
ax2.set_ylabel('Avg Profit')
ax2.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
ax2.tick_params(axis='x', rotation=45)

fig.suptitle('Punjab: City-wise Breakdown', fontsize=14, fontweight='bold')
fig.tight_layout()

plt.show()

# detailed analysis of chandigarh city


chandigarh_data = merged_data[merged_data['City'] == 'Chandigarh']
category_split = chandigarh_data.groupby('Category').agg(
    Total_Sales=('Amount', 'sum'),
    Total_Profit=('Profit', 'sum')
).reset_index()

print("\n--- CHANDIGARH: SALES & PROFIT BY CATEGORY ---")
print(category_split)