# use pandas to read customer data from a csv file
import pandas as pd

CSV_FILE = 'customers.csv'

df = pd.read_csv(CSV_FILE)

print(F"Loading customer data from '{CSV_FILE}'")
print(f"Total customers loaded: {len(df)}")

# filter customers based on purchase amount (e.g. customers who spend over $1000)
print("Applying filters:")
print("- Purchase amount > $1000")
print("- Country: USA")

# filters by customer location (e.g. amount, country)
filtered_results = df[(df['Purchase_Amount'] > 1000.00) & (df['Country'] == 'USA')]

# displays the filtered results in the console
print("Filtered Results:")
print(filtered_results)
print("Summary:")

purchase_total = 0
number_of_purchases = len(filtered_results['Purchase_Amount'])
for i in filtered_results['Purchase_Amount']:
    purchase_total = i + purchase_total

average_purchase = purchase_total / number_of_purchases
average_purchase = round(average_purchase, 2)

print(f"Total customers found: {number_of_purchases}")
print(f"Average purchase amount: ${average_purchase}")

# exports the filtered data to a new CSV file
EXPORT_FILE = 'filtered_results.csv'

print(f"Exporting to '{EXPORT_FILE}'")
filtered_results.to_csv(EXPORT_FILE, index=False)
print(f"Export complete!")