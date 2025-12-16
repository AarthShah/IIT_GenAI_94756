import pandas as pd
df=pd.read_csv('C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment01\\products.csv')

print(df.head(5))

print("Total number of rows:", len(df))

count = (df['price'] >= 500).sum()

print("Number of products with price >= 500:", count)

avg=df['price'].mean()
print("Average price of products:", avg)

category=input("Enter the category to filter products: ")
category_f=df[df['category'] == category]
print(f"Products in category '{category}':")
print(category_f)

total=df['quantity'].sum()
print("Total quantity of all products:", total)