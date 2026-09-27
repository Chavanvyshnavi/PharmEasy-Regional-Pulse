import sqlite3
import pandas as pd

connect = sqlite3.connect("pharmeasy.db")

print("\n========== TASK 2.2 ==========")

left_join_query = """
SELECT COUNT(*) AS row_count
FROM regions_master r
LEFT JOIN orders_clean o
ON r.region = o.region;
"""

left_count = pd.read_sql_query(left_join_query, connect)

print("\nLEFT JOIN row count:")
print(left_count)

inner_join_query = """
SELECT COUNT(*) AS row_count
FROM regions_master r
INNER JOIN orders_clean o
ON r.region = o.region;
"""

inner_count = pd.read_sql_query(inner_join_query, connect)

print("\nINNER JOIN row count:")
print(inner_count)

duplicate_query = """
SELECT order_id, COUNT(*) AS count
FROM orders_clean
GROUP BY order_id
HAVING COUNT(*) > 1;
"""

duplicates = pd.read_sql_query(duplicate_query, connect)

print("\nDuplicate order IDs:")
print(duplicates)

if duplicates.empty:
    print("No duplicate order IDs found.")

count_comparison_query = """
SELECT
    r.region,
    COUNT(*) AS count_star,
    COUNT(o.order_id) AS count_order_id
FROM regions_master r
LEFT JOIN orders_clean o
ON r.region = o.region
GROUP BY r.region
ORDER BY r.region;
"""

count_comparison = pd.read_sql_query(
    count_comparison_query,
    connect
)

print("\nCOUNT(*) vs COUNT(order_id):")
print(count_comparison)

disagreement = count_comparison[
    count_comparison["count_star"]
    != count_comparison["count_order_id"]
]

print("\nRegions where COUNT(*) and COUNT(order_id) disagree:")
print(disagreement)

region_orders_query = """
SELECT
    r.region,
    COUNT(o.order_id) AS order_count
FROM regions_master r
LEFT JOIN orders_clean o
ON r.region = o.region
GROUP BY r.region
ORDER BY order_count ASC;
"""

region_orders = pd.read_sql_query(
    region_orders_query,
    connect
)

print("\nPer-region order counts:")
print(region_orders)

print("\n========== TASK 2.3 ==========")


monthly_sales_query = """
SELECT
    region,
    substr(order_date, 1, 7) AS month,
    ROUND(SUM(sales_inr), 2) AS total_sales
FROM orders_clean
GROUP BY region, substr(order_date, 1, 7)
ORDER BY region, month;
"""

monthly_sales = pd.read_sql_query(
    monthly_sales_query,
    connect
)

print("\nRegion × Month sales:")
print(monthly_sales)

monthly_sales.to_csv(
    "region_month_sales.csv",
    index=False
)

print("\nSaved: region_month_sales.csv")

connect.close()