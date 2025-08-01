import requests as r
from datetime import datetime
import json

print('Welcome to the Exchange Rate Tracker!')
currency = input('Enter the base currency (e.g., USD): ')

url = r.get(f'https://open.er-api.com/v6/latest/{currency}')
response = url.json()

with open('currency-exchange-rate-tracker/output.txt', 'w') as file:
    file.write(json.dumps(response, indent=2))
    file.close

print('Available currencies: USD, EUR, GBP')

target_currencies = input('Enter target currencies (comma-seprated, e.g., EUR, GBP): ')
target_currencies = target_currencies.split(", ")

amount = float(input(f'Enter the amount to exchange in {currency}: '))

def convert_currency(currency, target_currencies, amount):
    for target_currency in target_currencies:
        target_currency_amount = response['rates'][target_currency]
        converted_rate = float(target_currency_amount) * amount
        print(f'Conversion Results for {target_currency}:\n{amount} {currency} = {round(converted_rate, 2)} {target_currency}')
        
        conversion_results = f"Base currency: {currency}\nAmount: {amount} {currency}\n{amount} {currency} = {round(converted_rate, 2)} {target_currency}\nTimestamp: {datetime.now()}\n\n"

        filename = 'currency-exchange-rate-tracker/conversion_results.txt'                   
        with open(filename, 'a') as file:
            file.write(conversion_results)
            file.close()
    print(f'Results saved to {filename}.')


convert_currency(currency, target_currencies, amount)