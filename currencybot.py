from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    # Create a CurrencyRates object
    currency_rates = CurrencyRates()

    try:
        # Convert the amount from the source currency to the target currency
        converted_amount = currency_rates.convert(from_currency, to_currency, amount)
        return converted_amount
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    # Example usage
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency (3-letter code, e.g., USD): ").upper()
    to_currency = input("Enter the target currency (3-letter code, e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")