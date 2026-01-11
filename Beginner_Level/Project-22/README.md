# Currency Converter 💱 ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)
![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

A comprehensive **Currency Converter** written in Python with static exchange rates.  
Convert between 20 major world currencies quickly and easily!

---

## 📌 Features

- 💱 **20 Major Currencies** - USD, EUR, GBP, INR, JPY, and 15 more
- ⚡ **Quick Convert** - Fast single currency conversion
- 📊 **Batch Convert** - Compare one currency against multiple others
- 🔄 **Reverse Conversion** - Calculate inverse amounts
- 📈 **Exchange Rate Tables** - View all rates at once
- 💾 **Clean Interface** - Easy-to-use menu system
- 🎯 **Accurate Calculations** - Precise decimal handling
- 📝 **Formatted Output** - Beautiful currency symbols and formatting

---

## 💰 Supported Currencies

| Code | Currency | Symbol | Region |
|------|----------|--------|--------|
| **USD** | US Dollar | $ | United States |
| **EUR** | Euro | € | European Union |
| **GBP** | British Pound | £ | United Kingdom |
| **INR** | Indian Rupee | ₹ | India |
| **JPY** | Japanese Yen | ¥ | Japan |
| **AUD** | Australian Dollar | A$ | Australia |
| **CAD** | Canadian Dollar | C$ | Canada |
| **CHF** | Swiss Franc | CHF | Switzerland |
| **CNY** | Chinese Yuan | ¥ | China |
| **SEK** | Swedish Krona | kr | Sweden |
| **NZD** | New Zealand Dollar | NZ$ | New Zealand |
| **MXN** | Mexican Peso | Mex$ | Mexico |
| **SGD** | Singapore Dollar | S$ | Singapore |
| **HKD** | Hong Kong Dollar | HK$ | Hong Kong |
| **NOK** | Norwegian Krone | kr | Norway |
| **KRW** | South Korean Won | ₩ | South Korea |
| **TRY** | Turkish Lira | ₺ | Turkey |
| **RUB** | Russian Ruble | ₽ | Russia |
| **BRL** | Brazilian Real | R$ | Brazil |
| **ZAR** | South African Rand | R | South Africa |

---

## 🚀 How to Run

### 1. Make sure you have Python 3 installed
Check using:
```bash
python --version
```
or
```bash
python3 --version
```

### 2. Run the program
```bash
python currency_converter.py
```
or
```bash
python3 currency_converter.py
```

### 3. Choose Your Conversion Mode
```
======================================================================
           💱 CURRENCY CONVERTER 💱
======================================================================

Convert between 20 major world currencies!
Note: Using static exchange rates (not live data)

----------------------------------------------------------------------
MENU:
  1. Quick Convert (single conversion)
  2. Batch Convert (compare multiple currencies)
  3. Reverse Conversion
  4. View All Currencies
  5. Exchange Rate Table
  6. Exit
----------------------------------------------------------------------
```

---

## 📝 Usage Examples

### Example 1: Quick Convert (Single Conversion)

```
Select option (1-6): 1

======================================================================
⚡ QUICK CONVERT
======================================================================
Enter amount: 100
From currency: USD
To currency: EUR

======================================================================
💱 CONVERSION RESULT
======================================================================

$100.00 USD (US Dollar)
                           ↓
€92.00 EUR (Euro)

======================================================================
Exchange Rate: 1 USD = 0.9200 EUR
======================================================================
```

### Example 2: Batch Convert (Multiple Currencies)

```
Select option (1-6): 2

======================================================================
📊 BATCH CONVERT
======================================================================
Enter amount: 1000
Base currency: USD

Convert to:
  1. All currencies
  2. Select specific currencies
Select option (1-2): 2

Enter currency codes separated by commas (e.g., EUR,GBP,JPY)
Available: AUD, BRL, CAD, CHF, CNY, EUR, GBP, HKD, INR, JPY, ...
Currency codes: EUR,GBP,INR,JPY

======================================================================
💰 CURRENCY COMPARISON
======================================================================
Base: $1,000.00 USD (US Dollar)
----------------------------------------------------------------------
Currency Amount              Full Name
----------------------------------------------------------------------
EUR             €920.00    Euro
GBP             £790.00    British Pound
INR          ₹83,120.00    Indian Rupee
JPY         ¥149,500.00    Japanese Yen
======================================================================
```

### Example 3: Reverse Conversion

```
Select option (1-6): 3

======================================================================
🔄 REVERSE CONVERSION
======================================================================
Find: How much Currency A equals X amount of Currency B?

Target currency (B): EUR
Enter amount: 100
Source currency (A): USD

======================================================================
🔄 REVERSE RESULT
======================================================================

$108.70 USD
                  equals
€100.00 EUR
======================================================================
```

**Explanation:** You need $108.70 USD to get €100 EUR.

### Example 4: View All Currencies

```
Select option (1-6): 4

======================================================================
AVAILABLE CURRENCIES
======================================================================
Code   Name                           Symbol   Rate (to USD)
----------------------------------------------------------------------
AUD    Australian Dollar              A$       1 USD = 1.5200 AUD
BRL    Brazilian Real                 R$       1 USD = 4.9700 BRL
CAD    Canadian Dollar                C$       1 USD = 1.3600 CAD
CHF    Swiss Franc                    CHF      1 USD = 0.8800 CHF
CNY    Chinese Yuan                   ¥        1 USD = 7.2400 CNY
EUR    Euro                           €        1 USD = 0.9200 EUR
GBP    British Pound                  £        1 USD = 0.7900 GBP
...
======================================================================
```

### Example 5: Exchange Rate Table

```
Select option (1-6): 5

======================================================================
📈 EXCHANGE RATE TABLE (Base: USD)
======================================================================
Enter base currency (default: USD): GBP

Base Currency: British Pound (GBP)
----------------------------------------------------------------------
Currency 1 GBP =        1 XXX =
----------------------------------------------------------------------
AUD          1.9241 AUD            0.5197 GBP
BRL          6.2911 BRL            0.1589 GBP
CAD          1.7215 CAD            0.5809 GBP
CHF          1.1139 CHF            0.8978 GBP
EUR          1.1646 EUR            0.8587 GBP
INR        105.2152 INR            0.0095 GBP
JPY        189.2405 JPY            0.0053 GBP
USD          1.2658 USD            0.7900 GBP
...
======================================================================
```

---

## 📂 Folder Structure

```
Currency-Converter/
   ├── currency_converter.py    # Main Python script
   ├── README.md                # Documentation
   └── currency_beginner.py     # Beginner Level
```

---

## 🎯 Conversion Modes Explained

### 1. Quick Convert
- **Use:** Convert a specific amount from one currency to another
- **Best for:** Single, straightforward conversions
- **Example:** "How much is $100 USD in Euros?"

### 2. Batch Convert
- **Use:** Compare one currency against multiple others simultaneously
- **Best for:** Shopping across borders, travel planning
- **Example:** "How much is $1000 USD worth in EUR, GBP, and JPY?"

### 3. Reverse Conversion
- **Use:** Find out how much of Currency A you need to get X amount of Currency B
- **Best for:** Budgeting, target amount planning
- **Example:** "How many USD do I need to get €1000 EUR?"

### 4. View All Currencies
- **Use:** See all available currencies with their exchange rates
- **Best for:** Reference, learning currency codes

### 5. Exchange Rate Table
- **Use:** View comprehensive rate comparison from any base currency
- **Best for:** Financial analysis, rate comparison

---

## 💡 How Exchange Rates Work

### Base Currency System
This converter uses **USD (US Dollar)** as the base currency:
- All rates are stored relative to USD
- Conversions between other currencies go through USD

### Conversion Formula
```
Amount in Target = (Amount in Source / Rate of Source) × Rate of Target
```

**Example:** Convert $100 USD to EUR
1. Amount in USD: $100 (already in base)
2. Multiply by EUR rate: 100 × 0.92 = €92

**Example:** Convert €100 EUR to GBP
1. Convert EUR to USD: 100 / 0.92 = $108.70 USD
2. Convert USD to GBP: 108.70 × 0.79 = £85.87 GBP

---

## 🎓 Learning Concepts

This project demonstrates:
- **Dictionary Data Structures** - Nested dictionaries for currency data
- **Mathematical Operations** - Exchange rate calculations
- **Functions** - Modular code organization
- **Input Validation** - Error handling and data validation
- **String Formatting** - Currency symbols and number formatting
- **User Interface Design** - Menu-driven program flow
- **Data Organization** - Structured information storage

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Built-in Libraries Only** - No external dependencies required

---

## ✅ Purpose

- Convert between major world currencies
- Learn exchange rate calculations
- Practice Python dictionary operations
- Useful tool for travel and shopping
- Educational project for beginners

---

## 📊 Static vs Live Rates

### Static Rates (This Project)
✅ **Pros:**
- No internet required
- Instant calculations
- No API dependencies
- Always works offline
- Free to use

❌ **Cons:**
- Rates don't update automatically
- Not suitable for real trading
- Approximate values only

### When to Use Static Rates
- Learning and practice
- Rough estimates
- Offline environments
- Historical comparisons
- Educational purposes

---

## 🔮 Future Enhancements

### Planned Features
- [ ] Live API integration (real-time rates)
- [ ] Historical rate tracking
- [ ] Currency charts and graphs
- [ ] Favorite currency pairs
- [ ] Conversion history with timestamps
- [ ] Export to CSV/Excel
- [ ] Mobile app version
- [ ] Cryptocurrency support
- [ ] Multi-language support
- [ ] GUI version using Tkinter

### API Integration Options
For live rates, consider:
- **ExchangeRate-API** (free tier available)
- **Fixer.io** (reliable rates)
- **Open Exchange Rates** (comprehensive)
- **CurrencyLayer** (easy to use)

---

## 💡 Tips for Using the Converter

### Best Practices
1. **Check Rates Regularly**: Static rates may become outdated
2. **Use for Estimates**: Not for actual financial transactions
3. **Round Appropriately**: Consider rounding for practical amounts
4. **Batch Convert for Travel**: Compare multiple destinations at once
5. **Save Important Conversions**: Keep notes of key amounts

### Practical Use Cases
- 📱 **Online Shopping**: Compare prices across countries
- ✈️ **Travel Planning**: Budget for international trips
- 💼 **Business Estimates**: Quick cost calculations
- 📚 **Education**: Learn about exchange rates
- 🎓 **Homework Helper**: Currency conversion problems

---

## 🌍 Real-World Applications

### Personal Finance
- Planning international vacations
- Comparing prices on global websites
- Understanding foreign salary offers
- Calculating remittance amounts

### Business
- International pricing strategies
- Cost estimation for imports/exports
- Budget planning for foreign markets
- Quick reference for negotiations

### Education
- Economics and finance courses
- Mathematics word problems
- Geography and cultural studies
- International business classes

---

## 📚 Educational Value

### What You Learn
1. **Exchange Rate Math** - Understanding currency conversion
2. **Data Structures** - Working with nested dictionaries
3. **User Input** - Validation and error handling
4. **Formatting** - Professional output display
5. **Program Design** - Menu-driven interfaces

### Skills Developed
- Python programming fundamentals
- Financial calculations
- User interface design
- Error handling techniques
- Code organization and modularity

---

## ⚠️ Important Notes

### Disclaimer
- **Not Financial Advice**: This tool is for educational purposes only
- **Static Rates**: Exchange rates are fixed and may not reflect current market values
- **No Guarantees**: Always verify with official sources for actual transactions
- **Educational Use**: Best suited for learning and rough estimates

### Rate Updates
The static rates in this program are approximate values. To update:
1. Open `currency_converter.py`
2. Find the `EXCHANGE_RATES` dictionary
3. Update rate values based on current market rates
4. Save and run

---

## 👨‍💻 Author

**Developed by Debanga**

---

## 📝 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Want to add more features or currencies? Feel free to fork and submit a pull request!

### How to Add a Currency:
```python
EXCHANGE_RATES = {
    # Existing currencies...
    "XXX": {"name": "Currency Name", "symbol": "Symbol", "rate": 0.00},
}
```

---

**Convert Currencies Easily! 💱✨**