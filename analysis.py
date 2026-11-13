from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "ecommerce_orders.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(DATA_FILE)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df.dropna(subset=["order_id", "customer_id", "product_name", "order_date"])

    df["gross_sales"] = df["quantity"] * df["unit_price"]
    df["discount_amount"] = df["gross_sales"] * df["discount_percent"]
    df["revenue"] = df["gross_sales"] - df["discount_amount"]

    total_revenue = df["revenue"].sum()
    total_orders = df["order_id"].nunique()
    customer_orders = df.groupby("customer_id")["order_id"].nunique()
    repeat_customers = int((customer_orders > 1).sum())
    avg_order_value = total_revenue / total_orders if total_orders else 0

    print("\\n=== E-COMMERCE CUSTOMER ANALYTICS ===")
    print(f"Total revenue:       ₹{total_revenue:,.2f}")
    print(f"Total orders:        {total_orders:,}")
    print(f"Unique customers:    {df['customer_id'].nunique():,}")
    print(f"Repeat customers:    {repeat_customers:,}")
    print(f"Average order value: ₹{avg_order_value:,.2f}")
    print(f"Discount amount:     ₹{df['discount_amount'].sum():,.2f}")

    top_products = df.groupby("product_name", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    category_sales = df.groupby("category", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    repeat_summary = pd.DataFrame({
        "customer_type": ["Repeat customers", "One-time customers"],
        "customer_count": [repeat_customers, int((customer_orders == 1).sum())]
    })
    monthly_sales = df.set_index("order_date").resample("MS")["revenue"].sum().reset_index()

    top_products.to_csv(OUTPUT_DIR / "top_products.csv", index=False)
    category_sales.to_csv(OUTPUT_DIR / "category_sales.csv", index=False)
    repeat_summary.to_csv(OUTPUT_DIR / "repeat_customers.csv", index=False)
    monthly_sales.to_csv(OUTPUT_DIR / "monthly_revenue.csv", index=False)

    plt.figure(figsize=(10, 5))
    plt.bar(top_products["product_name"].head(8), top_products["revenue"].head(8))
    plt.title("Top Products by Revenue")
    plt.xlabel("Product")
    plt.ylabel("Revenue (INR)")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_products.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(category_sales["category"], category_sales["revenue"])
    plt.title("Category-wise Revenue")
    plt.xlabel("Category")
    plt.ylabel("Revenue (INR)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "category_sales.png", dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(monthly_sales["order_date"], monthly_sales["revenue"], marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue (INR)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
    plt.close()

    print("\\nAnalysis complete. Check the outputs/ folder for reports and charts.")
    print("\\nTop 5 products:")
    print(top_products.head().to_string(index=False))
    print("\\nCategory-wise sales:")
    print(category_sales.to_string(index=False))

if __name__ == "__main__":
    main()
