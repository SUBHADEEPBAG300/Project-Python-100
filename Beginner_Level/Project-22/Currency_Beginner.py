# Beginner Level

def currency_converter(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0,
        'AUD': 1.35
    }
    
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Currency not supported")
    
    # Convert amount to USD
    amount_in_usd = amount / exchange_rates[from_currency]
    
    # Convert USD to target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount

# Example usage
amount = 100
from_currency = 'USD'
to_currency = 'EUR'
converted = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is {converted:.2f} {to_currency}")
