import requests as r
import datetime



print('Welcome to the Exchange Rate Tracker!')
currency = input('Enter the base currency (e.g., USD): ')

url = r.get(f'https://open.er-api.com/v6/latest/{currency}')
response = url.json()

print('Available currencies: USD, EUR, GBP')
target_currency = input('Enter target currencies (comma-seprated, e.g., EUR, GBP): ')
amount = int(input(f'Enter the amount in {currency}'))

# def convert_currency(currency, target_currency, amount):
#     print('Conversion Results:\n ')


# convert_currency()