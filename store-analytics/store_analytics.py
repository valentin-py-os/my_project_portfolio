import codecademylib3
import pandas as pd

# Load the datasets into DataFrames
visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

# Display the first few rows of each DataFrame to understand their structure
print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))

# Merge visits and cart DataFrames using a left merge
v_c = pd.merge(visits, cart, how='left')

# Print the length of the merged DataFrame and its contents
print(len(v_c))
print(v_c)

# Find and print rows where cart_time is null
null = v_c[v_c.cart_time.isnull()]
print(null)

# Calculate and print the percentage of users who visited but did not add to cart
calculation = float(1652/2000) * 100
print('Percentage unvisited cart: ' + str(calculation))

# Merge cart and checkout DataFrames using a left merge
c_c = pd.merge(cart, checkout, how='left')

# Print the length of the merged DataFrame and its contents
print(len(c_c))
print(c_c)

# Find and print rows where checkout_time is null
null2 = c_c[c_c.checkout_time.isnull()]
print(null2)

# Merge all four steps of the funnel using a series of left merges
all_data = visits.merge(cart, how='left')\
    .merge(checkout, how='left')\
    .merge(purchase, how='left')

# Display the first few rows of the merged DataFrame
print(all_data.head(5))

# Calculate the percentage of users who proceeded to checkout but did not purchase
checkout_nopurchase = (all_data['checkout_time'].notnull().sum() - all_data['purchase_time'].notnull().sum()) / (all_data['checkout_time'].notnull().sum()) * 100
print(str(checkout_nopurchase) + '%')

# Calculate total users at each step of the funnel
total_visits = len(all_data)
total_cart = all_data['cart_time'].notnull().sum()
total_checkout = all_data['checkout_time'].notnull().sum()
total_purchase = all_data['purchase_time'].notnull().sum()

# Calculate drop-off rates at each step
visit_to_cart_dropoff = ((total_visits - total_cart) / total_visits) * 100
cart_to_checkout_dropoff = ((total_cart - total_checkout) / total_cart) * 100
checkout_to_purchase_dropoff = ((total_checkout - total_purchase) / total_checkout) * 100

# Print drop-off rates
print(f"Visit to Cart Drop-off: {visit_to_cart_dropoff:.2f}%")
print(f"Cart to Checkout Drop-off: {cart_to_checkout_dropoff:.2f}%")
print(f"Checkout to Purchase Drop-off: {checkout_to_purchase_dropoff:.2f}%")

# Identify the weakest step
weakest_step = max(visit_to_cart_dropoff, cart_to_checkout_dropoff, checkout_to_purchase_dropoff)

if weakest_step == visit_to_cart_dropoff:
    print("The weakest step is from Visit to Cart.")
elif weakest_step == cart_to_checkout_dropoff:
    print("The weakest step is from Cart to Checkout.")
else:
    print("The weakest step is from Checkout to Purchase.")

all_data['avg_time_for_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data['avg_time_for_purchase'])

print(all_data['avg_time_for_purchase'].mean())
