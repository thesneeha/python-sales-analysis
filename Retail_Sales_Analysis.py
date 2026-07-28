import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Region':['North','South','East','West','North','South'],
    'Category':['Clothing','Electronics','Clothing','Groceries','Electronics','Clothing'],
    'Sales':[5000,3000,2000,7000,4000,3500]

    }

df = pd.DataFrame(data)

print("SALES DATA:\n")
print(df)

category_sales = df.groupby('Category')['Sales'].sum()

print("\nCATEGORY-WISE SALES:\n")
print(category_sales)

best_category = category_sales.idxmax()
best_value = category_sales.max()

print(f"\nBEST CATEGORY: {best_category} ({best_value})")

category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

input("Press Enter to Exit")
