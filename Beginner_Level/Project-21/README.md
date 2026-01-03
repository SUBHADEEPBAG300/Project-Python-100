# QR Code Generator 🔲 ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)
![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

A versatile **QR Code Generator** written in Python.  
Create QR codes for URLs, WiFi, emails, contacts, and more with custom styles and colors!

---

## 📌 Features

- 🌐 **URL/Website Links** - Generate QR codes for any website
- 📝 **Plain Text** - Encode any text message
- 📶 **WiFi Networks** - Share WiFi credentials instantly
- 📧 **Email Addresses** - Pre-filled email with subject and body
- 📱 **Phone Numbers** - Direct call QR codes
- 💬 **SMS Messages** - Pre-composed text messages
- 👤 **Contact Cards (vCard)** - Share contact information
- 🎨 **Custom Styles** - Rounded, circle, or gapped patterns
- 🌈 **Custom Colors** - Choose from 6 different colors
- 💾 **Save as PNG** - High-quality image output

---

## 🎯 QR Code Types

| Type | Description | Use Case |
|------|-------------|----------|
| **URL** | Website links | Share websites, social media, portfolios |
| **Text** | Plain text | Messages, instructions, information |
| **WiFi** | Network credentials | Easy WiFi sharing for guests |
| **Email** | Email with subject/body | Contact forms, feedback requests |
| **Phone** | Phone number | Business cards, customer support |
| **SMS** | Pre-written message | Quick responses, surveys |
| **vCard** | Complete contact info | Digital business cards |

---

## 📦 Installation

### Required Library
This project uses the `qrcode` library with PIL support.

Install dependencies:
```bash
pip install qrcode[pil]
```

Or install individually:
```bash
pip install qrcode
pip install pillow
```

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install qrcode[pil]
```

### 2. Run the Program
```bash
python qr_generator.py
```
or
```bash
python3 qr_generator.py
```

### 3. Choose Your QR Code Type
```
============================================================
           🔲 QR CODE GENERATOR 🔲
============================================================

QR CODE TYPES:
  1. URL/Website Link
  2. Plain Text
  3. WiFi Network
  4. Email Address
  5. Phone Number
  6. SMS Message
  7. Contact Card (vCard)

CUSTOMIZATION:
  8. Styled QR Code (rounded/circle/gapped)
  9. Colored QR Code

  0. Exit
============================================================
```

---

## 📝 Usage Examples

### Example 1: Website URL
```
Select option (0-9): 1

📱 URL/WEBSITE LINK
------------------------------------------------------------
Enter URL (e.g., https://example.com): https://github.com/debanga
Filename (default: url_qrcode.png): github_qr.png

✅ QR Code saved as 'github_qr.png'
```

### Example 2: WiFi Network
```
Select option (0-9): 3

📶 WIFI NETWORK
------------------------------------------------------------
WiFi Name (SSID): MyHomeNetwork
Password: SecurePass123

Security Type:
  1. WPA/WPA2 (default)
  2. WEP
  3. None
Select (1-3): 1
Filename (default: wifi_qrcode.png): home_wifi.png

✅ QR Code saved as 'home_wifi.png'
📶 WiFi QR Code created for network: MyHomeNetwork
```

**Result:** Scanning this QR code will automatically connect to the WiFi network!

### Example 3: Email Contact
```
Select option (0-9): 4

📧 EMAIL ADDRESS
------------------------------------------------------------
Email address: support@example.com
Subject (optional): Customer Inquiry
Message (optional): Hello, I have a question about...
Filename (default: email_qrcode.png): contact_email.png

✅ QR Code saved as 'contact_email.png'
📧 Email QR Code created for: support@example.com
```

### Example 4: Contact Card (vCard)
```
Select option (0-9): 7

👤 CONTACT CARD (vCard)
------------------------------------------------------------
Full name: Debanga Kumar
Phone number (optional): +91-1234567890
Email (optional): debanga@example.com
Filename (default: vcard_qrcode.png): my_contact.png

✅ QR Code saved as 'my_contact.png'
👤 Contact QR Code created for: Debanga Kumar
```

**Result:** Scanning adds contact directly to phone!

### Example 5: Styled QR Code
```
Select option (0-9): 8

✨ STYLED QR CODE
------------------------------------------------------------
Enter data (URL/text): https://portfolio.com

Style options:
  1. Rounded (default)
  2. Circle
  3. Gapped Square
Select style (1-3): 2

Available colors:
  1. Black
  2. Blue
  3. Red
  4. Green
  5. Purple
  6. Orange
Select color (1-6, default=1): 4
Filename (default: styled_qrcode.png): portfolio_green.png

✅ Styled QR Code saved as 'portfolio_green.png'
```

### Example 6: Colored QR Code
```
Select option (0-9): 9

🎨 COLORED QR CODE
------------------------------------------------------------
Enter data (URL/text): https://example.com

Foreground color:
Available colors:
  1. Black
  2. Blue
  3. Red
  4. Green
  5. Purple
  6. Orange
Select color (1-6, default=1): 2

Background color:
Select color (1-6, default=1): 1
Filename (default: colored_qrcode.png): blue_qr.png

✅ Colored QR Code saved as 'blue_qr.png'
```

---

## 📂 Folder Structure

```
QR-Code-Generator/
   ├── qr_generator.py          # Main Python script
   ├── README.md                # Documentation
   ├── requirements.txt         # Dependencies
   └── generated_qrcodes/       # Output folder (optional)
       ├── url_qrcode.png
       ├── wifi_qrcode.png
       ├── email_qrcode.png
       └── ...
```

---

## 🎨 Customization Options

### Styles Available
1. **Rounded** - Smooth rounded squares (modern look)
2. **Circle** - Circular dots (elegant design)
3. **Gapped** - Squares with gaps (unique pattern)

### Colors Available
- Black (default)
- Blue
- Red
- Green
- Purple
- Orange

### Error Correction Levels
The QR codes use different error correction levels:
- **Basic QR Codes**: LOW (L) - 7% damage tolerance
- **Styled QR Codes**: HIGH (H) - 30% damage tolerance

---

## 🎯 Practical Use Cases

### Personal Use
- 📱 Share social media profiles
- 🏠 Guest WiFi access at home
- 📧 Business email signature
- 👤 Digital business cards

### Business Use
- 🏢 Restaurant menus (contactless)
- 🎫 Event tickets and registrations
- 📦 Product information and tracking
- 💳 Payment links and invoices

### Marketing
- 📰 Print advertisements
- 🎨 Posters and flyers
- 📺 Video content (link to more info)
- 🎁 Promotional campaigns

### Education
- 📚 Assignment submission links
- 🎓 Course material access
- 📝 Feedback forms
- 🔗 Resource sharing

---

## 🎓 Learning Concepts

This project demonstrates:
- **QR Code Generation** - Using `qrcode` library
- **Image Processing** - PIL/Pillow for styling
- **String Formatting** - Special formats (WiFi, vCard, mailto)
- **User Input Handling** - Menu-driven interface
- **File I/O Operations** - Saving PNG images
- **Functions** - Modular code organization
- **Customization** - Styles and colors

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **qrcode** - QR code generation library
- **Pillow (PIL)** - Image processing
- **StyledPilImage** - Custom QR code styles

---

## ✅ Purpose

- Generate QR codes quickly and easily
- Share information without typing
- Create professional-looking QR codes
- Learn Python image processing
- Practical tool for daily use

---

## 📋 Requirements File

Create a `requirements.txt` file:
```
qrcode[pil]
pillow
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔮 Future Enhancements

- [ ] Add logo/image in center of QR code
- [ ] Batch QR code generation from CSV
- [ ] QR code scanner/reader
- [ ] Export to SVG format
- [ ] Generate QR codes for calendar events
- [ ] Location/GPS coordinates QR codes
- [ ] Social media profile QR codes
- [ ] Dynamic QR codes with tracking
- [ ] GUI version using Tkinter
- [ ] Web interface using Flask

---

## 💡 Tips for Best QR Codes

### Scanning Tips
1. **High Contrast**: Use dark foreground on light background
2. **Size Matters**: Larger QR codes scan easier
3. **Don't Overdecorate**: Too much styling reduces scannability
4. **Test Before Printing**: Always test with multiple devices
5. **Error Correction**: Use HIGH level for printed materials

### Data Tips
1. **URLs**: Use URL shorteners for long links
2. **WiFi**: Test on multiple devices before sharing
3. **Text**: Keep messages concise and clear
4. **Contact**: Include essential info only

### Design Tips
1. **Border/Quiet Zone**: Always maintain the 4-unit border
2. **Colors**: Ensure good contrast for scanning
3. **Size**: Minimum 2cm x 2cm for printing
4. **Format**: PNG provides best quality

---

## 📱 How to Scan QR Codes

### iOS (iPhone/iPad)
- Open native **Camera** app
- Point at QR code
- Tap the notification banner

### Android
- Open **Google Lens** or **Camera** app
- Point at QR code
- Tap to open link/action

### Dedicated Apps
- **QR Code Reader** (App Store/Play Store)
- **Barcode Scanner**
- Various free options available

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
- Add more QR code styles
- Implement logo embedding
- Add batch generation
- Create web interface

---

## ⚠️ Troubleshooting

### ModuleNotFoundError: qrcode
**Solution:**
```bash
pip install qrcode[pil]
```

### Image doesn't save
**Solution:** Check write permissions in the directory

### QR code won't scan
**Solutions:**
- Ensure good contrast (dark on light)
- Increase box_size for larger QR codes
- Reduce data amount
- Use higher error correction level

---

**Generate QR Codes Easily! 🔲✨**