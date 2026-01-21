import pandas as pd

# Read all CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine into one dataframe
data = pd.concat([df1, df2, df3])
#only pink morsel
data = data[data["product"] == "pink morsel"]
#clean price
data["price"] = data["price"].str.replace("$", "", regex=False)
data["price"] = pd.to_numeric(data["price"])
# ensure quantity is number
data["quantity"] = pd.to_numeric(data["quantity"])
#create sales column
data["sales"] = data["quantity"] * data["price"]
# keep only required column
final_data = data[["sales", "date", "region"]]
#save final output
final_data.to_csv("formatted_sales_data.csv", index=False)



