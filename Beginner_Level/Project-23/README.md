# Email Slicer 📧 ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)
![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

A powerful **Email Analysis and Slicer Tool** written in Python.  
Extract username, domain, provider info, and analyze email patterns!

---

## 📌 Features

- ✂️ **Email Slicing** - Separate username and domain
- 🔍 **Email Validation** - Check valid email format
- 📊 **Detailed Analysis** - Username patterns, domain info
- 🌐 **Provider Detection** - Identify Gmail, Yahoo, Outlook, etc.
- 📋 **Batch Processing** - Process multiple emails at once
- 📈 **Domain Statistics** - Count and analyze domains
- 🔄 **Email Variations** - Generate alternative emails
- 🔒 **Email Masking** - Privacy protection
- 💾 **No Dependencies** - Pure Python, no external libraries

---

## 🎯 What It Does

| Feature | Description | Example |
|---------|-------------|---------|
| **Basic Slice** | Split into username & domain | john.doe@gmail.com → john.doe + gmail.com |
| **Validation** | Check if email is valid | user@domain.com ✅ / user@domain ❌ |
| **Provider ID** | Identify email service | gmail.com → Google Gmail |
| **Username Analysis** | Check patterns in username | Has numbers? Dots? Case? |
| **Domain Info** | Extract TLD, subdomain | mail.company.com → TLD: com, Sub: mail |
| **Batch Process** | Handle multiple emails | Process 10, 50, 100+ emails |
| **Statistics** | Count unique domains | How many @gmail.com, @yahoo.com? |
| **Masking** | Hide for privacy | john@gmail.com → j**n@*****.com |

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
python email_slicer.py
```
or
```bash
python3 email_slicer.py
```

### 3. Choose Your Operation
```
======================================================================
           📧 EMAIL SLICER 📧
======================================================================

Extract and analyze email components!

----------------------------------------------------------------------
MENU:
  1. Slice Single Email (detailed analysis)
  2. Quick Slice (simple username/domain)
  3. Batch Process (multiple emails)
  4. Domain Statistics (from list)
  5. Generate Email Variations
  6. Mask Email (privacy)
  7. Exit
----------------------------------------------------------------------
```

---

## 📝 Usage Examples

### Example 1: Detailed Email Analysis

```
Select option (1-7): 1

======================================================================
📧 DETAILED EMAIL ANALYSIS
======================================================================
Enter email address: john.doe123@gmail.com

======================================================================
📧 EMAIL ANALYSIS
======================================================================

Full Email:        john.doe123@gmail.com

----------------------------------------------------------------------
COMPONENTS:
----------------------------------------------------------------------
Username:          john.doe123
Domain:            gmail.com
Provider:          Google Gmail

----------------------------------------------------------------------
DOMAIN DETAILS:
----------------------------------------------------------------------
Full Domain:       gmail.com
Main Domain:       gmail
TLD (Extension):   com

----------------------------------------------------------------------
USERNAME ANALYSIS:
----------------------------------------------------------------------
Length:            11 characters
Contains numbers:  Yes
Contains dots:     Yes
Contains underscores: No
Case type:         All lowercase
======================================================================
```

### Example 2: Quick Slice

```
Select option (1-7): 2

======================================================================
⚡ QUICK SLICE
======================================================================
Enter email address: alice_smith@company.co.uk

----------------------------------------------------------------------
Username:  alice_smith
Domain:    company.co.uk
----------------------------------------------------------------------
```

### Example 3: Batch Processing

```
Select option (1-7): 3

======================================================================
📋 BATCH PROCESSING
======================================================================
Enter email addresses (one per line).
Press Enter twice when done.

john@gmail.com
sarah@yahoo.com
mike@outlook.com
admin@company.com
invalid-email

[Press Enter twice]

======================================================================
📊 BATCH EMAIL PROCESSING
======================================================================

Processing 5 emails...

----------------------------------------------------------------------
Email                          Username        Domain               Provider
----------------------------------------------------------------------
john@gmail.com                 john            gmail.com            Google Gmail
sarah@yahoo.com                sarah           yahoo.com            Yahoo Mail
mike@outlook.com               mike            outlook.com          Microsoft Outlook
admin@company.com              admin           company.com          Custom/Business Domain
invalid-email                  INVALID EMAIL
----------------------------------------------------------------------

Valid emails: 4
Invalid emails: 1
======================================================================
```

### Example 4: Domain Statistics

```
Select option (1-7): 4

======================================================================
📊 DOMAIN STATISTICS
======================================================================
Enter email addresses (one per line).
Press Enter twice when done.

user1@gmail.com
user2@gmail.com
user3@gmail.com
user4@yahoo.com
user5@yahoo.com
user6@outlook.com

[Press Enter twice]

======================================================================
🌐 DOMAIN STATISTICS
======================================================================

Total unique domains: 3

----------------------------------------------------------------------
Domain                                   Count
----------------------------------------------------------------------
gmail.com                                    3  (Google Gmail)
yahoo.com                                    2  (Yahoo Mail)
outlook.com                                  1  (Microsoft Outlook)
======================================================================
```

### Example 5: Email Variations

```
Select option (1-7): 5

======================================================================
🔄 EMAIL VARIATIONS
======================================================================
Enter base email address: john.doe@gmail.com

======================================================================
🔄 EMAIL VARIATIONS
======================================================================

Base: john.doe@gmail.com

Possible variations:
  1. john.doe@gmail.com
  2. johndoe@gmail.com
  3. john.doe@gmail.com
  4. john.doe.work@gmail.com
  5. john.doe.personal@gmail.com
  6. john.doe1@gmail.com
  7. john.doe2024@gmail.com
======================================================================
```

### Example 6: Mask Email (Privacy)

```
Select option (1-7): 6

======================================================================
🔒 MASK EMAIL
======================================================================
Enter email address: john.doe@company.com

----------------------------------------------------------------------
Original:  john.doe@company.com
Masked:    j******e@*******.com
----------------------------------------------------------------------
```

---

## 📂 Folder Structure

```
Email-Slicer/
   ├── email_slicer.py      # Main Python script
   └── README.md            # Documentation
```

---

## 🔍 Email Components Explained

### Anatomy of an Email Address

**Example:** `john.doe@mail.company.com`

```
john.doe          @          mail.company.com
   ↓                              ↓
Username                      Domain
(Local Part)                  
                              ↙         ↓        ↘
                         Subdomain  Main Name   TLD
                           (mail)   (company)  (.com)
```

### Components Breakdown

1. **Username (Local Part)**
   - Everything before the `@` symbol
   - Can contain: letters, numbers, dots, underscores, hyphens
   - Examples: john, john.doe, john_smith123

2. **Domain**
   - Everything after the `@` symbol
   - Contains the mail server address
   - Examples: gmail.com, company.co.uk, mail.business.org

3. **Subdomain** (Optional)
   - Part of domain before main name
   - Often: mail, smtp, webmail
   - Example: `mail` in mail.company.com

4. **Main Domain**
   - Primary domain name
   - Example: `company` in mail.company.com

5. **TLD (Top-Level Domain)**
   - Domain extension
   - Examples: .com, .org, .co.uk, .edu

---

## 🌐 Supported Email Providers

The tool can identify these popular email providers:

| Provider | Domain | Service Name |
|----------|--------|--------------|
| Gmail | gmail.com | Google Gmail |
| Yahoo | yahoo.com | Yahoo Mail |
| Outlook | outlook.com | Microsoft Outlook |
| Hotmail | hotmail.com | Microsoft Hotmail |
| iCloud | icloud.com | Apple iCloud |
| ProtonMail | protonmail.com | ProtonMail |
| AOL | aol.com | AOL Mail |
| Zoho | zoho.com | Zoho Mail |
| Mail.com | mail.com | Mail.com |
| Yandex | yandex.com | Yandex Mail |
| GMX | gmx.com | GMX Mail |
| Tutanota | tutanota.com | Tutanota |

Any other domain is classified as "Custom/Business Domain"

---

## 🎓 Learning Concepts

This project demonstrates:
- **String Manipulation** - Splitting, slicing, parsing
- **Regular Expressions** - Email validation patterns
- **Dictionaries** - Data organization and lookup
- **Functions** - Modular code design
- **Input Validation** - Error handling
- **Batch Processing** - Handling multiple inputs
- **Data Analysis** - Statistics and counting
- **Conditional Logic** - Decision making

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **re (regex)** - Email validation
- **Built-in Functions** - String operations, split()

---

## ✅ Purpose

- Learn email structure and components
- Validate email addresses
- Extract information from emails
- Process email lists efficiently
- Practice Python string manipulation
- Useful for data cleaning and analysis

---

## 🎯 Practical Use Cases

### Personal Use
- 📧 Organize email contacts
- 🔍 Verify email formats
- 📊 Analyze your contact list
- 🔒 Mask emails for privacy

### Business Use
- 📋 Clean mailing lists
- 📈 Analyze customer email domains
- ✅ Validate user registrations
- 📊 Domain-based statistics

### Development
- 🧪 Test email validation
- 🔧 Parse email data
- 📝 Extract contact information
- 🗃️ Database cleaning

### Data Analysis
- 📊 Count email providers
- 📈 Domain distribution analysis
- 🔍 Pattern recognition
- 📉 Data quality checks

---

## 💡 Email Validation Rules

### Valid Email Format
An email is considered valid if it matches this pattern:

```
username @ domain . tld
   ↓       ↓    ↓     ↓
Required  Required  Required
```

**Requirements:**
- Must have exactly one `@` symbol
- Username before `@`
- Domain after `@`
- At least one dot in domain
- Valid TLD (2+ letters)

### Valid Examples
✅ `john@gmail.com`
✅ `john.doe@company.com`
✅ `user123@mail.company.co.uk`
✅ `first_last@domain.org`

### Invalid Examples
❌ `john` (no @ or domain)
❌ `john@` (no domain)
❌ `@gmail.com` (no username)
❌ `john@@gmail.com` (double @)
❌ `john@domain` (no TLD)

---

## 📊 Batch Processing Tips

### Best Practices
1. **Clean Your Data**: Remove empty lines before processing
2. **Check Validity**: Invalid emails are flagged
3. **Export Results**: Copy output for further use
4. **Large Lists**: Process in batches if very large

### Use Cases for Batch Processing
- **Mailing List Cleanup**: Find and remove invalid emails
- **Domain Analysis**: See which providers are most common
- **Data Migration**: Convert email lists between formats
- **Duplicate Detection**: Identify similar email patterns

---

## 🔮 Future Enhancements

- [ ] Export results to CSV/Excel
- [ ] Import emails from file
- [ ] Check if email exists (MX record lookup)
- [ ] Suggest alternative emails if invalid
- [ ] Detect disposable email addresses
- [ ] Check for common typos (gmial.com → gmail.com)
- [ ] Extract emails from text/documents
- [ ] Advanced pattern detection
- [ ] GUI version using Tkinter
- [ ] Integration with email APIs

---

## 🔒 Privacy & Security Notes

### Privacy Features
- **Email Masking**: Hide sensitive information
- **No Storage**: Tool doesn't save any data
- **Offline Operation**: No internet required
- **Local Processing**: All analysis done locally

### Security Best Practices
- Don't process sensitive emails on shared computers
- Clear terminal history after processing sensitive data
- Be cautious with batch processing of confidential lists
- Use masking feature when sharing examples

---

## 💡 Tips and Tricks

### For Better Results
1. **Copy-Paste Lists**: Easier than typing manually
2. **Check Validity First**: Use quick slice to verify format
3. **Use Variations**: Generate alternatives for taken usernames
4. **Domain Stats**: Analyze your contact distribution
5. **Masking**: Share examples without exposing real emails

### Common Patterns
- **Personal Emails**: firstname.lastname@provider.com
- **Business Emails**: firstname@company.com
- **Generic**: info@, support@, admin@
- **Department**: sales@, hr@, contact@

---

## 📚 Educational Value

### What You Learn
1. **Email Structure**: Understanding components
2. **String Methods**: split(), find(), replace()
3. **Regex**: Pattern matching and validation
4. **Data Processing**: Batch operations
5. **Error Handling**: Validation and exceptions

### Skills Developed
- Python string manipulation
- Data validation techniques
- Batch processing logic
- User interface design
- Pattern recognition

---

## 👨‍💻 Author

**Developed by Debanga**

---

## 📝 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Want to add more features? Feel free to fork and submit a pull request!

### Ideas for Contributions:
- Add more email providers
- Implement disposable email detection
- Add email suggestion feature
- Create export functionality
- Build GUI interface

---

**Slice and Analyze Emails Easily! 📧✨**