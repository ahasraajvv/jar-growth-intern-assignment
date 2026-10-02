# Jar Growth Intern Assignment — Sales Analysis

## About
This project analyses sales data for a retail company across three dimensions:
1. **Sales & Profitability** — Category and sub-category level performance
2. **Target Achievement** — Furniture category target vs actual analysis
3. **Regional Performance** — State and city level insights

## Dataset
Three Excel files in the `data/` folder:
- `List of Orders.xlsx` — Order metadata (Order ID, date, state, city)
- `Order Details.xlsx` — Transaction details (category, sub-category, amount, profit, quantity)
- `Sales target.xlsx` — Monthly sales targets by category

## Project Structure
```
JAR-assignment/
├── data/                          # Raw datasets
│   ├── List of Orders.xlsx
│   ├── Order Details.xlsx
│   └── Sales target.xlsx
├── Q1_part_1/                     # Part 1: Sales & Profitability
│   ├── q1_part1_sales.py          # Analysis script
│   ├── Q1_Part1_Charts.png        # Category-level charts
│   ├── Q1_Part1_SubCategory.png   # Sub-category margin chart
│   └── Report_part_1.txt          # Written analysis
├── Q1_part_2/                     # Part 2: Target Achievement
│   ├── q1_part2_target.py         # Analysis script
│   ├── Q1_Part2_Charts.png        # Target vs Actual chart
│   └── Report_part2.txt           # Written analysis
├── Q1_part_3/                     # Part 3: Regional Performance
│   ├── q1_part_3.py               # Analysis script
│   ├── Q1_Part3_Charts.png        # State-level chart
│   ├── Punjab_City_Breakdown.png  # City drill-down chart
│   └── Report_part_3.txt          # Written analysis
└── README.md
```

## How to Run
```bash
# Install dependencies
pip install pandas matplotlib seaborn openpyxl

# Run each part (from the project root directory)
python Q1_part_1/q1_part1_sales.py
python Q1_part_2/q1_part2_target.py
python Q1_part_3/q1_part_3.py
```

## Key Findings
- **Electronics** leads in total sales; **Clothing** has the best profit margin; **Furniture** underperforms at 1.81% margin
- Furniture **actual sales are highly volatile** (3,600–15,600) while targets increase linearly (10,400–11,800)
- **Punjab** is the only loss-making state among the top 5, driven by Electronics losses in Chandigarh

## Tools Used
- Python 3.x
- pandas, matplotlib, seaborn, openpyxl
