import pandas as pd
import hashlib

data = pd.read_csv("cafe_sales.csv")
#print(data.head())

#create a copy of 'data' dataframe
cleaned_data = data.copy()
#print(cleaned_data.head())

#Remove column 'Card Number'
cleaned_data= cleaned_data.drop(columns=["Card Number"])
#print(cleaned_data.head())

#Anonymise 'Customer Name' column
cleaned_data["Customer Name"] = cleaned_data["Customer Name"].apply(lambda x: "Cust_"+ hashlib.sha256(x.encode()).hexdigest()[:3])
#print(cleaned_data.head())

#create a new columns 'Sales' and 'Profit' which equal to 'Price'*0.33
cleaned_data["Sales"] = cleaned_data["Price"]
cleaned_data["Profit"] = cleaned_data["Sales"]* 0.33
#print(cleaned_data.head())

#convert the modified dataframe 'cleaned_data' to a csv file
cleaned_data.to_csv("cafe_sales_cleaned.csv",index = False)
print(pd.read_csv("cafe_sales_cleaned.csv"))