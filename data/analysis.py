import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/sample_data.csv')

print(df.head())

sales_by_category = df.groupby('category')['sales'].sum()

print(sales_by_category)

sales_by_category.plot(kind='bar')
plt.title('Sales by Category')
plt.show()
