import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Online Retail.xlsx")

original_size = data.shape

data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

clean_data = data.copy()

clean_data = clean_data.drop_duplicates()

clean_data = clean_data[
    ~clean_data['InvoiceNo'].astype(str).str.startswith('C')
]

clean_data = clean_data[
    (clean_data['Quantity'] > 0) &
    (clean_data['UnitPrice'] > 0)
]

clean_data = clean_data.dropna(subset=['Description']).copy()

cleaned_size = clean_data.shape

clean_data['Revenue'] = (
    clean_data['Quantity'] * clean_data['UnitPrice']
)

mean_quantity = clean_data['Quantity'].mean()
median_quantity = clean_data['Quantity'].median()

mean_price = clean_data['UnitPrice'].mean()
median_price = clean_data['UnitPrice'].median()

total_revenue = clean_data['Revenue'].sum()
mean_revenue = clean_data['Revenue'].mean()
median_revenue = clean_data['Revenue'].median()

correlation = clean_data[
    ['Quantity', 'UnitPrice', 'Revenue']
].corr()

clean_data['Month'] = (
    clean_data['InvoiceDate']
    .dt.to_period('M')
)

monthly_revenue = (
    clean_data.groupby('Month')['Revenue']
    .sum()
)

monthly_revenue.index = (
    monthly_revenue.index.to_timestamp()
)

country_revenue = (
    clean_data.groupby('Country')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("Original dataset size:", original_size)
print("Cleaned dataset size:", cleaned_size)

print("\nSales Analysis:")
print("Mean Quantity:", mean_quantity)
print("Median Quantity:", median_quantity)
print("Mean Unit Price:", mean_price)
print("Median Unit Price:", median_price)
print("Total Revenue:", total_revenue)
print("Mean Revenue:", mean_revenue)
print("Median Revenue:", median_revenue)

print("\nCorrelation:")
print(correlation)

print("\nTop 10 Countries by Revenue:")
print(country_revenue)

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker='o'
)

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Online Retail Revenue")
plt.xticks(rotation=45)
plt.grid()

plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()

plt.figure(figsize=(10, 6))

country_revenue.plot(kind='bar')

plt.xlabel("Country")
plt.ylabel("Revenue")
plt.title("Top 10 Countries by Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("country_revenue.png")
plt.show()