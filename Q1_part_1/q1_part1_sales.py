"""
Part 1: Sales and Profitability Analysis
- Merge List of Orders and Order Details on Order ID
- Calculate total sales, avg profit per order, profit margin by category
- Sub-category level profitability analysis
"""
import pandas as pd
import matplotlib.pyplot as plt


orders = pd.read_excel("data/List of Orders.xlsx")

details = pd.read_excel("data/Order Details.xlsx")

# order data exploring 


# detail data exploring 

# Merging the two dataframes on Order ID

merged_data = pd.merge(orders, details, on='Order ID', how='inner')

print("---------------- total sales amount in each category --------------")

sales_by_category = merged_data.groupby('Category')['Amount'].sum()

print(sales_by_category)

print("----------------  The average profit per order by category --------------")

profit_per_order = merged_data.groupby(['Category', 'Order ID'])['Profit'].sum().reset_index()
avg_profit_per_order = profit_per_order.groupby('Category')['Profit'].mean()

print("AVERAGE PROFIT PER ORDER:")
print(avg_profit_per_order.round(2))

print("----------------  Total profit margin --------------"  )

total_profit_margin = merged_data.groupby('Category')[['Profit', 'Amount']].sum().reset_index()
total_profit_margin["Margin_profit%"] = (total_profit_margin["Profit"] / total_profit_margin["Amount"]) * 100
print(total_profit_margin.round(2))

# Data visualization

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# total sales bar chart 

axes[0].bar(sales_by_category.index, sales_by_category.values, color='skyblue')
axes[0].set_title('Total Sales Amount', fontweight='bold')
axes[0].set_xlabel('Category')
axes[0].set_ylabel('Amount')

# avg profit per order bar chart

axes[1].bar(avg_profit_per_order.index, avg_profit_per_order.values, color='lightgreen')
axes[1].set_title('Average Profit per Order',  fontweight='bold')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Profit')

# total profit margin bar chart

axes[2].bar(total_profit_margin['Category'], total_profit_margin['Margin_profit%'], color='salmon')
axes[2].set_title('Profit Margin (%)', fontweight='bold')
axes[2].set_xlabel('Category')
axes[2].set_ylabel('Percentage (%)')

plt.savefig('Q1_part_1/Q1_Part1_Charts.png', dpi=150, bbox_inches='tight')
plt.show()

# analysis of sub category 

sub = merged_data.groupby(['Category','Sub-Category']).agg(
    Sales=('Amount','sum'), Profit=('Profit','sum')).reset_index()
sub['Margin%'] = (sub.Profit/sub.Sales*100).round(2)
sub = sub.sort_values('Margin%')
plt.figure(figsize=(8,6))
plt.barh(sub['Sub-Category'], sub['Margin%'],
         color=['red' if x<0 else 'green' for x in sub['Margin%']])
plt.axvline(0, color='black')
plt.title('Profit Margin by Sub-Category')
plt.tight_layout(); plt.savefig('Q1_part_1/Q1_Part1_SubCategory.png', dpi=150, bbox_inches='tight')
plt.show()