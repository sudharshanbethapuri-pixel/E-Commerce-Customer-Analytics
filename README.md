# E-Commerce Customer Analytics

A beginner-friendly portfolio project using **Python, Pandas, NumPy and Matplotlib** to analyze e-commerce orders and customer purchasing patterns.

## Project objectives
- Identify top products by revenue.
- Analyze repeat and one-time customers.
- Calculate total revenue, category-wise sales and discount impact.
- Review monthly revenue trends through visualizations.

## Technologies
Python 3.9+, Pandas, NumPy and Matplotlib.

## Project structure
```text
ecommerce_customer_analytics/
├── data/
│   └── ecommerce_orders.csv
├── outputs/
│   └── Generated reports and charts
├── analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset
The CSV contains 1,200 sample order records with order date, customer ID, product, category, quantity, unit price and discount percentage. **This is synthetic sample data**, not real customer information.

## Run the project
1. Install Python 3.9 or later.
2. Open a terminal in this project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python analysis.py
   ```
5. View generated CSV summaries and PNG charts in `outputs/`.

## Main calculations
- Gross sales = quantity × unit price
- Discount amount = gross sales × discount percentage
- Revenue = gross sales − discount amount
- Average order value = total revenue ÷ unique order count
- Repeat customer = customer with more than one order

## Upload to GitHub
Create a repository named `ecommerce-customer-analytics`, extract this ZIP file, then upload the project folder contents to the repository. Keep the `data/` folder so the script can run.

## Resume project description
**E-Commerce Customer Analytics | Python, Pandas, NumPy, Matplotlib**
- Developed a Python-based data analysis project to explore e-commerce order and customer data.
- Analyzed purchasing patterns to identify top products and repeat customers.
- Calculated total revenue, category-wise sales and discount impact.
- Generated visualizations and summary reports to communicate business insights.
