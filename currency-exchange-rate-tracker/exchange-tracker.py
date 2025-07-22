import requests as r
import datetime
import json



print('Welcome to the Exchange Rate Tracker!')
currency = input('Enter the base currency (e.g., USD): ')

url = r.get(f'https://open.er-api.com/v6/latest/{currency}')
response = url.json()

with open('currency-exchange-rate-tracker/output.txt', 'w') as file:
    file.write(json.dumps(response, indent=2))
    file.close

print('Available currencies: USD, EUR, GBP')
target_currency = input('Enter target currencies (comma-seprated, e.g., EUR, GBP): ')
amount = float(input(f'Enter the amount to exchange in {currency}: '))

def convert_currency(currency, target_currency, amount):
    target_currency_amount = response['rates'][target_currency]
    converted_rate = float(target_currency_amount) * amount
    print(f'Conversion Results:\n{round(converted_rate, 2)}')


convert_currency(currency, target_currency, amount)