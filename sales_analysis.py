import matplotlib.pyplot as plt
import pandas as pd
# Read the CSV file
sales = pd.read_csv("sales_data.csv")

# Display the data
print("Sales Data:")
print(sales) 

# Create Total colunmn
sales["Total"] = sales["Quantity"] * sales["Price"]

print("\nSales with Total:")
print(sales)

#Overall Sales
total_sales = sales ["Total"].sum()

print("\nOverall Sales Amount: $", total_sales)

# Best-selling product based on quantity
best_product = ( 
    sales.groupby("Product")
["Quantity"].sum()
)
print("\nBest Selling Products:")
print(best_product)

# Top selling product
top_product = best_product. idxmax()
top_quantity = best_product . max()

print("\nTop Selling Product:", top_product)
print("Quantity Sold:", top_quantity) 

#Sales by category
category_sales =(
    sales.groupby("Category")
["Total"].sum()
)
print("\nSales by Category:")
print(category_sales)

category_sales.plot(kind="bar")
plt.title("Sales by category")
plt.xlabel("Category")
plt.ylabel("Sales Amount")

plt.show()

# Sales by region
region_sales =(
    sales.groupby("Region")
["Total"].sum()
)

plt.figure(figsize=(6,6))
plt.pie(region_sales,
        labels=region_sales.index,
        autopct="%1,1f%%")
plt.title("Sales by Region")
plt.show()

#Convert  Order Date to datetime
sales["Order Date"],format="d%-m%-y%"
#Monthly Sales
monthly_sales = sales.groupby(sales["Order Date"].dt.date)["Total"].sum()
# Line Chart
plt.figure(figsize=(8,5))
plt.ploy(monthly_sales.index,
    monthly_sales.values,marker="o")
plt.title("Sales Trend")
plt.xlabel("Order Date")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Save report 
sales.to_csv("sales_report.csv", index=False)
print("\nReport saved successfully")