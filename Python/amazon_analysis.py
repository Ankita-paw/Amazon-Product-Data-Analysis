import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/amazon.csv")

# Clean price columns
df['discounted_price'] = df['discounted_price'].replace('[₹,]', '', regex=True).astype(float)
df['actual_price'] = df['actual_price'].replace('[₹,]', '', regex=True).astype(float)

# Clean rating count
df['rating_count'] = df['rating_count'].replace(',', '', regex=True)
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

# Create discount column
df['discount_amount'] = df['actual_price'] - df['discounted_price']

# Basic analysis
print("Total Products:", df.shape[0])
print("Average Rating:", df['rating'].mean())

# Top rated products
top_rated = df[['product_name','rating']].sort_values(by='rating',ascending=False).head(10)
print(top_rated)

# Plot rating distribution
plt.figure(figsize=(8,5))
sns.histplot(df['rating'], bins=20)
plt.title("Product Rating Distribution")
plt.show()
