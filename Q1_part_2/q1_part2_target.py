"""
Part 2: Target Achievement Analysis
- Month-over-month % change in Furniture sales targets
- Identify months with significant target fluctuations
- Compare target vs actual sales with gap analysis
"""
import pandas as pd 
import matplotlib.pyplot as plt

# 1. Load All Data (Need orders to get actual sales)
orders = pd.read_excel("data/List of Orders.xlsx")
details = pd.read_excel("data/Order Details.xlsx")
merged_data = pd.merge(orders, details, on='Order ID', how='inner')
target_data = pd.read_excel("data/Sales target.xlsx")



target_furniture = target_data[target_data['Category'] == 'Furniture'].copy()

# --- THE DATE FIX ---
# Excel converted the 18/19 years into days. We extract them back into years.
true_year = 2000 + target_furniture['Month of Order Date'].dt.day
true_month = target_furniture['Month of Order Date'].dt.month
target_furniture['Month of Order Date'] = pd.to_datetime({'year': true_year, 'month': true_month, 'day': 1})

# arrange them in chronological order in each month 
target_furniture = target_furniture.sort_values('Month of Order Date')

# mathematical calculation of percentage change in target sales month over month
target_furniture['Target_Pct_Change'] = (target_furniture['Target'].pct_change() * 100).round(2)

print("\n--- FURNITURE TARGET PERCENTAGE CHANGE (MONTH-OVER-MONTH) ---")
print(target_furniture[['Month of Order Date', 'Target', 'Target_Pct_Change']])

# Identify months with significant target fluctuations
print("\n--- MONTHS WITH SIGNIFICANT TARGET FLUCTUATIONS ---")
significant = target_furniture[target_furniture['Target_Pct_Change'].abs() > 1.5]
print(significant[['Month of Order Date', 'Target', 'Target_Pct_Change']])


# --- GET ACTUAL SALES ---
actual_furn = merged_data[merged_data['Category'] == 'Furniture'].copy()
actual_furn['Order Date'] = pd.to_datetime(actual_furn['Order Date'])
# Force actual dates to the 1st of the month so they match target dates perfectly
actual_furn['Month of Order Date'] = actual_furn['Order Date'].dt.to_period('M').dt.to_timestamp()
actual_sales = actual_furn.groupby('Month of Order Date')['Amount'].sum().reset_index()

# Merge Targets and Actuals
comparison = pd.merge(target_furniture, actual_sales, on='Month of Order Date', how='inner')

# Gap Analysis: Target vs Actual
comparison['Gap'] = comparison['Amount'] - comparison['Target']
comparison['Achievement_%'] = ((comparison['Amount'] / comparison['Target']) * 100).round(2)

print("\n--- TARGET vs ACTUAL GAP ANALYSIS ---")
print(comparison[['Month of Order Date', 'Target', 'Amount', 'Gap', 'Achievement_%']].to_string(index=False))

print(f"\nMonths where actual exceeded target: {(comparison['Gap'] > 0).sum()} out of {len(comparison)}")
print(f"Average achievement: {comparison['Achievement_%'].mean():.1f}%")


# --- DATA VISUALIZATION ---
plt.figure(figsize=(12, 6))

# Plot Target Line (Solid Purple)
plt.plot(comparison['Month of Order Date'], comparison['Target'], marker='o', color='purple', label='Target Sales', linewidth=2)
# Plot Actual Line (Dashed Green)
plt.plot(comparison['Month of Order Date'], comparison['Amount'], marker='x', color='green', label='Actual Sales', linewidth=2, linestyle='--')

plt.title("Furniture: Smooth Targets vs Volatile Actual Sales", fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Sales Amount")

# Labels for Target Line (Pushed UP)
for i, row in comparison.iterrows():
    label = f"{row['Month of Order Date'].strftime('%b-%y')}\n{int(row['Target'])}"
    plt.text(row['Month of Order Date'], row['Target'] + 200, 
             label, ha='center', fontsize=8, fontweight='bold', color='purple')

# Labels for Actual Line (Pushed DOWN)
for i, row in comparison.iterrows():
    plt.text(row['Month of Order Date'], row['Amount'] - 400, 
             f"{int(row['Amount'])}", ha='center', fontsize=8, fontweight='bold', color='green')
    
plt.legend()
plt.grid(True) 
plt.tight_layout()

plt.savefig("Q1_part_2/Q1_Part2_Charts.png", dpi=150, bbox_inches='tight') 
plt.show()