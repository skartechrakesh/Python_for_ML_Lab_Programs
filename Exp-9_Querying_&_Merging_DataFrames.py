import pandas as pd

# Accept CSV file names
sales_file = input("Enter sales data CSV file name: ")
customer_file = input("Enter customer data CSV file name: ")

# Read CSV files
sales_df = pd.read_csv(sales_file)
customer_df = pd.read_csv(customer_file)

print("\nSales Data")
print("----------")
print(sales_df)

print("\nCustomer Data")
print("-------------")
print(customer_df)

# Inner Join
inner_join = pd.merge(sales_df, customer_df, on="Customer_ID", how="inner")
print("\nInner Join Result")
print("-----------------")
print(inner_join)

# Left Join
left_join = pd.merge(sales_df, customer_df, on="Customer_ID", how="left")
print("\nLeft Join Result")
print("----------------")
print(left_join)

# Outer Join
outer_join = pd.merge(sales_df, customer_df, on="Customer_ID", how="outer")
print("\nOuter Join Result")
print("-----------------")
print(outer_join)
