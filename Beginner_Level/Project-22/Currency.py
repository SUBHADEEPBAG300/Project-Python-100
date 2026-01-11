# Advanced Level

"""
Currency Converter
Convert between multiple currencies using static exchange rates.
"""

# Static exchange rates (base currency: USD)
EXCHANGE_RATES = {
    "USD": {"name": "US Dollar", "symbol": "$", "rate": 1.0},
    "EUR": {"name": "Euro", "symbol": "€", "rate": 0.92},
    "GBP": {"name": "British Pound", "symbol": "£", "rate": 0.79},
    "INR": {"name": "Indian Rupee", "symbol": "₹", "rate": 83.12},
    "JPY": {"name": "Japanese Yen", "symbol": "¥", "rate": 149.50},
    "AUD": {"name": "Australian Dollar", "symbol": "A$", "rate": 1.52},
    "CAD": {"name": "Canadian Dollar", "symbol": "C$", "rate": 1.36},
    "CHF": {"name": "Swiss Franc", "symbol": "CHF", "rate": 0.88},
    "CNY": {"name": "Chinese Yuan", "symbol": "¥", "rate": 7.24},
    "SEK": {"name": "Swedish Krona", "symbol": "kr", "rate": 10.37},
    "NZD": {"name": "New Zealand Dollar", "symbol": "NZ$", "rate": 1.64},
    "MXN": {"name": "Mexican Peso", "symbol": "Mex$", "rate": 17.08},
    "SGD": {"name": "Singapore Dollar", "symbol": "S$", "rate": 1.34},
    "HKD": {"name": "Hong Kong Dollar", "symbol": "HK$", "rate": 7.83},
    "NOK": {"name": "Norwegian Krone", "symbol": "kr", "rate": 10.68},
    "KRW": {"name": "South Korean Won", "symbol": "₩", "rate": 1308.50},
    "TRY": {"name": "Turkish Lira", "symbol": "₺", "rate": 32.15},
    "RUB": {"name": "Russian Ruble", "symbol": "₽", "rate": 92.50},
    "BRL": {"name": "Brazilian Real", "symbol": "R$", "rate": 4.97},
    "ZAR": {"name": "South African Rand", "symbol": "R", "rate": 18.65}
}


def convert_currency(amount, from_currency, to_currency):
    """Convert amount from one currency to another."""
    # Convert to USD first (base currency)
    amount_in_usd = amount / EXCHANGE_RATES[from_currency]["rate"]
    
    # Convert from USD to target currency
    converted_amount = amount_in_usd * EXCHANGE_RATES[to_currency]["rate"]
    
    return converted_amount


def display_currencies():
    """Display all available currencies."""
    print("\n" + "="*70)
    print("AVAILABLE CURRENCIES")
    print("="*70)
    print(f"{'Code':<6} {'Name':<30} {'Symbol':<8} {'Rate (to USD)'}")
    print("-"*70)
    
    for code, info in sorted(EXCHANGE_RATES.items()):
        rate_display = f"1 USD = {info['rate']:.4f} {code}"
        print(f"{code:<6} {info['name']:<30} {info['symbol']:<8} {rate_display}")
    
    print("="*70)


def display_conversion_result(amount, from_curr, to_curr, result):
    """Display conversion result in formatted output."""
    from_info = EXCHANGE_RATES[from_curr]
    to_info = EXCHANGE_RATES[to_curr]
    
    print("\n" + "="*70)
    print("💱 CONVERSION RESULT")
    print("="*70)
    print(f"\n{from_info['symbol']}{amount:,.2f} {from_curr} ({from_info['name']})")
    print("                           ↓")
    print(f"{to_info['symbol']}{result:,.2f} {to_curr} ({to_info['name']})")
    print("\n" + "="*70)
    
    # Display exchange rate used
    rate = EXCHANGE_RATES[to_curr]["rate"] / EXCHANGE_RATES[from_curr]["rate"]
    print(f"Exchange Rate: 1 {from_curr} = {rate:.4f} {to_curr}")
    print("="*70)


def compare_currency(amount, base_currency, currencies_list=None):
    """Compare base currency against multiple currencies."""
    if currencies_list is None:
        currencies_list = list(EXCHANGE_RATES.keys())
    
    print("\n" + "="*70)
    print(f"💰 CURRENCY COMPARISON")
    print("="*70)
    base_info = EXCHANGE_RATES[base_currency]
    print(f"Base: {base_info['symbol']}{amount:,.2f} {base_currency} ({base_info['name']})")
    print("-"*70)
    print(f"{'Currency':<8} {'Amount':<20} {'Full Name'}")
    print("-"*70)
    
    for currency in sorted(currencies_list):
        if currency != base_currency:
            converted = convert_currency(amount, base_currency, currency)
            info = EXCHANGE_RATES[currency]
            print(f"{currency:<8} {info['symbol']}{converted:>15,.2f}    {info['name']}")
    
    print("="*70)


def get_currency_choice(prompt="Enter currency code: "):
    """Get valid currency choice from user."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in EXCHANGE_RATES:
            return choice
        else:
            print(f"❌ Invalid currency code. Please enter a valid code.")
            print(f"   Available codes: {', '.join(sorted(EXCHANGE_RATES.keys()))}")


def get_amount():
    """Get valid amount from user."""
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            if amount <= 0:
                print("⚠️  Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")


def quick_convert():
    """Quick conversion mode."""
    print("\n" + "="*70)
    print("⚡ QUICK CONVERT")
    print("="*70)
    
    amount = get_amount()
    from_curr = get_currency_choice("From currency: ")
    to_curr = get_currency_choice("To currency: ")
    
    if from_curr == to_curr:
        print("⚠️  Source and target currencies are the same!")
        return
    
    result = convert_currency(amount, from_curr, to_curr)
    display_conversion_result(amount, from_curr, to_curr, result)


def batch_convert():
    """Convert one amount to multiple currencies."""
    print("\n" + "="*70)
    print("📊 BATCH CONVERT")
    print("="*70)
    
    amount = get_amount()
    base_currency = get_currency_choice("Base currency: ")
    
    print("\nConvert to:")
    print("  1. All currencies")
    print("  2. Select specific currencies")
    choice = input("Select option (1-2): ").strip()
    
    if choice == "1":
        compare_currency(amount, base_currency)
    elif choice == "2":
        print("\nEnter currency codes separated by commas (e.g., EUR,GBP,JPY)")
        print(f"Available: {', '.join(sorted(EXCHANGE_RATES.keys()))}")
        codes_input = input("Currency codes: ").strip().upper()
        codes = [c.strip() for c in codes_input.split(",")]
        
        valid_codes = [c for c in codes if c in EXCHANGE_RATES]
        if valid_codes:
            compare_currency(amount, base_currency, valid_codes)
        else:
            print("❌ No valid currency codes entered.")
    else:
        print("❌ Invalid option.")


def reverse_conversion():
    """Show how much of currency A equals specific amount of currency B."""
    print("\n" + "="*70)
    print("🔄 REVERSE CONVERSION")
    print("="*70)
    print("Find: How much Currency A equals X amount of Currency B?")
    
    to_curr = get_currency_choice("\nTarget currency (B): ")
    amount = get_amount()
    from_curr = get_currency_choice("Source currency (A): ")
    
    # Calculate reverse
    reverse_amount = convert_currency(amount, to_curr, from_curr)
    
    to_info = EXCHANGE_RATES[to_curr]
    from_info = EXCHANGE_RATES[from_curr]
    
    print("\n" + "="*70)
    print("🔄 REVERSE RESULT")
    print("="*70)
    print(f"\n{from_info['symbol']}{reverse_amount:,.2f} {from_curr}")
    print("                  equals")
    print(f"{to_info['symbol']}{amount:,.2f} {to_curr}")
    print("="*70)


def exchange_rate_table():
    """Display exchange rate comparison table."""
    print("\n" + "="*70)
    print("📈 EXCHANGE RATE TABLE (Base: USD)")
    print("="*70)
    
    base = input("Enter base currency (default: USD): ").strip().upper()
    if not base:
        base = "USD"
    
    if base not in EXCHANGE_RATES:
        print("❌ Invalid currency code.")
        return
    
    print(f"\nBase Currency: {EXCHANGE_RATES[base]['name']} ({base})")
    print("-"*70)
    print(f"{'Currency':<8} {'1 {base} =':<15} {'1 XXX ='}")
    print("-"*70)
    
    for code in sorted(EXCHANGE_RATES.keys()):
        if code != base:
            # 1 base = X target
            rate_to = convert_currency(1, base, code)
            # 1 target = X base
            rate_from = convert_currency(1, code, base)
            
            print(f"{code:<8} {rate_to:>12,.4f} {code:<8} {rate_from:>12,.4f} {base}")
    
    print("="*70)


def save_conversion_history(amount, from_curr, to_curr, result, filename="conversion_history.txt"):
    """Save conversion to history file."""
    try:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(filename, "a") as f:
            from_info = EXCHANGE_RATES[from_curr]
            to_info = EXCHANGE_RATES[to_curr]
            f.write(f"{timestamp} | {from_info['symbol']}{amount:,.2f} {from_curr} → "
                   f"{to_info['symbol']}{result:,.2f} {to_curr}\n")
        
        print(f"\n✅ Conversion saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving history: {e}")


def main():
    """Main program execution."""
    print("="*70)
    print("           💱 CURRENCY CONVERTER 💱")
    print("="*70)
    print("\nConvert between 20 major world currencies!")
    print("Note: Using static exchange rates (not live data)")
    
    while True:
        print("\n" + "-"*70)
        print("MENU:")
        print("  1. Quick Convert (single conversion)")
        print("  2. Batch Convert (compare multiple currencies)")
        print("  3. Reverse Conversion")
        print("  4. View All Currencies")
        print("  5. Exchange Rate Table")
        print("  6. Exit")
        print("-"*70)
        
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == '1':
            quick_convert()
            
            # Option to save
            save_opt = input("\nSave this conversion? (y/n): ").lower()
            if save_opt == 'y':
                # Last conversion would need to be stored - simplified here
                print("💾 Conversion history feature available in full version.")
        
        elif choice == '2':
            batch_convert()
        
        elif choice == '3':
            reverse_conversion()
        
        elif choice == '4':
            display_currencies()
        
        elif choice == '5':
            exchange_rate_table()
        
        elif choice == '6':
            print("\n" + "="*70)
            print("Thanks for using Currency Converter!")
            print("="*70)
            print("Goodbye! 👋\n")
            break
        
        else:
            print("❌ Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()