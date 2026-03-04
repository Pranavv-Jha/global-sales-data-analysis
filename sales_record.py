import pandas as pd

df = pd.read_csv("Sales_records.csv", encoding="latin1")

print(df.shape)
print(df.head())

# PROJECT: Global Sales Performance Analysis

# OBJECTIVE:
# Analyze large-scale global sales data to understand revenue trends,
# regional performance, product profitability, and sales channel impact
# to support strategic business decisions.

df["Order Date"] = pd.to_datetime(df["Order Date"])

region_revenue = df.groupby("Region")["Total Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Region:\n", region_revenue)

product_profit = df.groupby("Item Type")["Total Profit"].sum().sort_values(ascending=False)

print("\nProfit by Product:\n", product_profit)

channel_revenue = df.groupby("Sales Channel")["Total Revenue"].sum()

print("\nRevenue by Channel:\n", channel_revenue)

# REGIONAL REVENUE INSIGHT:
# Sub-Saharan Africa and Europe generate the highest revenue globally.
# This suggests strong market demand and business penetration in these regions.
# North America contributes significantly less, indicating a potential growth opportunity.


# Product Profitability INSIGHT:
# Cosmetics and Household items drive the highest profits globally.
# These categories likely have strong margins and customer demand.
# Fruits generate the lowest profit, suggesting lower pricing power or higher costs.


# Sales Channel INSIGHT:
# Offline sales marginally outperform online sales in total revenue.
# This indicates physical distribution channels still dominate in this business model.
# However, online revenue is nearly equal, suggesting strong digital growth potential.


# ---------- KPI CALCULATIONS ----------

total_revenue = df["Total Revenue"].sum()
total_profit = df["Total Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = total_revenue / total_orders
profit_margin = (total_profit / total_revenue) * 100

print("\n--- KPI SUMMARY ---")
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)
print("Profit Margin %:", profit_margin)

# INSIGHT:
# The business generated strong revenue with a healthy profit margin.
# Average order value helps estimate customer spending behaviour.
# These KPIs are core performance indicators tracked by analysts.

# ---------- TIME ANALYSIS ----------

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["YearMonth"] = df["Order Date"].dt.to_period("M")

monthly_revenue = df.groupby("YearMonth")["Total Revenue"].sum()

print("\nMonthly Revenue Trend:\n", monthly_revenue.tail())

# INSIGHT:
# Monthly revenue trend helps detect seasonality, peak demand periods,
# and potential decline patterns useful for forecasting and planning.

best_month = monthly_revenue.idxmax()
worst_month = monthly_revenue.idxmin()

print("\nBest Revenue Month:", best_month)
print("Worst Revenue Month:", worst_month)

# INSIGHT:
# Identifying peak and low months helps businesses plan marketing,
# staffing, and inventory decisions.

#From my analysis, I found that the business maintains a profit margin of around 29.5%,
# which indicates strong pricing control and efficient cost management.
#This suggests the company is able to generate substantial profit from its revenue and has a sustainable business model.
loss_products = df.groupby("Item Type")["Total Profit"].sum().sort_values()

print("\nProducts ranked by profit:\n", loss_products)

# INSIGHT:
# Ranking products by profit helps identify high performers
# and detect low-margin or loss-making products that may need pricing revision.



import matplotlib.pyplot as plt

monthly_revenue.plot(figsize=(10,5))
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.show()

product_profit.plot(kind="bar", figsize=(10,5))
plt.title("Profit by Product Type")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.show()


region_revenue.plot(kind="bar", figsize=(10,5))
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.show()

