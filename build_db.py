import pandas as pd
import sqlite3

orders_df = pd.read_csv("orders_clean.csv")
regions_df = pd.read_csv("regions_master.csv")

print("Orders loaded:", len(orders_df))
print("Regions loaded:", len(regions_df))

connect = sqlite3.connect("pharmeasy.db")


orders_df.to_sql(
    "orders_clean",
    connect,
    if_exists="replace",
    index=False
)

regions_df.to_sql(
    "regions_master",
    connect,
    if_exists="replace",
    index=False
)

orders_count = pd.read_sql_query(
    "SELECT COUNT(*) AS count FROM orders_clean",
    connect
)

regions_count = pd.read_sql_query(
    "SELECT COUNT(*) AS count FROM regions_master",
    connect
)

print("\nOrders table:")
print(orders_count)

print("\nRegions table:")
print(regions_count)

connect.close()

print("\nDatabase created successfully: pharmeasy.db")