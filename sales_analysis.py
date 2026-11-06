import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate E-Commerce Dataset
np.random.seed(42)
n = 1500

categories = ['Electronics', 'Home & Kitchen', 'Apparel', 'Books', 'Fitness']
payments = ['UPI', 'Credit Card', 'Debit Card', 'Net Banking', 'Cash on Delivery']
statuses = ['Delivered', 'Cancelled', 'Returned']

df = pd.DataFrame({
    'order_id': [f"ORD-{10000+i}" for i in range(n)],
    'customer_id': [f"CUST-{np.random.randint(1001, 1250)}" for _ in range(n)],
    'order_date': np.random.choice(pd.date_range('2026-01-01', '2026-10-31'), n),
    'product_category': np.random.choice(categories, n),
    'quantity': np.random.choice([1, 2, 3, 4], n, p=[0.5, 0.3, 0.15, 0.05]),
    'order_amount_inr': np.round(np.random.uniform(300, 5000, n), 2),
    'payment_method': np.random.choice(payments, n),
    'delivery_status': np.random.choice(statuses, n, p=[0.85, 0.10, 0.05])
})

# Save dataset
df.to_csv('data/ecommerce_orders.csv', index=False)
print("Saved: data/ecommerce_orders.csv")

# 2. Simple RFM Calculation
delivered = df[df['delivery_status'] == 'Delivered']
rfm = delivered.groupby('customer_id').agg(
    total_orders=('order_id', 'count'),
    total_spend=('order_amount_inr', 'sum')
).reset_index()

# 3. Create & Save Visualizations
sns.set_theme(style="whitegrid")

# Chart 1: Revenue by Category
plt.figure(figsize=(7, 4))
delivered.groupby('product_category')['order_amount_inr'].sum().plot(kind='bar', color='steelblue')
plt.title('Total Revenue by Category (Delivered)')
plt.ylabel('Revenue (INR)')
plt.xlabel('Category')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('visualizations/category_revenue.png')
plt.close()

# Chart 2: Order Count vs Spend
plt.figure(figsize=(7, 4))
sns.scatterplot(data=rfm, x='total_orders', y='total_spend', color='coral')
plt.title('Customer Order Count vs. Total Spend')
plt.xlabel('Total Orders')
plt.ylabel('Total Spend (INR)')
plt.tight_layout()
plt.savefig('visualizations/rfm_spend_distribution.png')
plt.close()

print("Saved: visualizations/category_revenue.png")
print("Saved: visualizations/rfm_spend_distribution.png")
print("Execution Complete!")