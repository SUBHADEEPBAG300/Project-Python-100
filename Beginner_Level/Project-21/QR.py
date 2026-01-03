# Advanced Level

"""
QR Code Generator
Generate QR codes for URLs, text, WiFi, emails, and more.
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, GappedSquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
import os


def create_basic_qr(data, filename="qrcode.png"):
    """Create a basic black and white QR code."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as '{filename}'")


def create_styled_qr(data, filename="styled_qrcode.png", style="rounded", color="black"):
    """Create a styled QR code with custom shapes and colors."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Choose module drawer based on style
    module_drawer = RoundedModuleDrawer()
    if style == "circle":
        module_drawer = CircleModuleDrawer()
    elif style == "gapped":
        module_drawer = GappedSquareModuleDrawer()
    
    # Create styled image
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=module_drawer,
        color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=color)
    )
    img.save(filename)
    print(f"✅ Styled QR Code saved as '{filename}'")


def create_colored_qr(data, filename="colored_qrcode.png", fg_color="black", bg_color="white"):
    """Create a QR code with custom colors."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save(filename)
    print(f"✅ Colored QR Code saved as '{filename}'")


def create_wifi_qr(ssid, password, security="WPA", filename="wifi_qrcode.png"):
    """Create a QR code for WiFi connection."""
    wifi_string = f"WIFI:T:{security};S:{ssid};P:{password};;"
    create_basic_qr(wifi_string, filename)
    print(f"📶 WiFi QR Code created for network: {ssid}")


def create_email_qr(email, subject="", body="", filename="email_qrcode.png"):
    """Create a QR code for email."""
    email_string = f"mailto:{email}?subject={subject}&body={body}"
    create_basic_qr(email_string, filename)
    print(f"📧 Email QR Code created for: {email}")


def create_phone_qr(phone_number, filename="phone_qrcode.png"):
    """Create a QR code for phone number."""
    phone_string = f"tel:{phone_number}"
    create_basic_qr(phone_string, filename)
    print(f"📱 Phone QR Code created for: {phone_number}")


def create_sms_qr(phone_number, message="", filename="sms_qrcode.png"):
    """Create a QR code for SMS."""
    sms_string = f"smsto:{phone_number}:{message}"
    create_basic_qr(sms_string, filename)
    print(f"💬 SMS QR Code created for: {phone_number}")


def create_vcard_qr(name, phone="", email="", filename="vcard_qrcode.png"):
    """Create a QR code for contact (vCard)."""
    vcard_string = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""
    create_basic_qr(vcard_string, filename)
    print(f"👤 Contact QR Code created for: {name}")


def get_color_choice():
    """Get color choice from user."""
    print("\nAvailable colors:")
    colors = {
        "1": ("black", "Black"),
        "2": ("blue", "Blue"),
        "3": ("red", "Red"),
        "4": ("green", "Green"),
        "5": ("purple", "Purple"),
        "6": ("orange", "Orange")
    }
    
    for key, (_, name) in colors.items():
        print(f"  {key}. {name}")
    
    choice = input("Select color (1-6, default=1): ").strip()
    return colors.get(choice, ("black", "Black"))[0]


def display_menu():
    """Display main menu."""
    print("\n" + "="*60)
    print("           🔲 QR CODE GENERATOR 🔲")
    print("="*60)
    print("\nQR CODE TYPES:")
    print("  1. URL/Website Link")
    print("  2. Plain Text")
    print("  3. WiFi Network")
    print("  4. Email Address")
    print("  5. Phone Number")
    print("  6. SMS Message")
    print("  7. Contact Card (vCard)")
    print("\nCUSTOMIZATION:")
    print("  8. Styled QR Code (rounded/circle/gapped)")
    print("  9. Colored QR Code")
    print("\n  0. Exit")
    print("="*60)


def main():
    """Main program execution."""
    print("="*60)
    print("           🔲 QR CODE GENERATOR 🔲")
    print("="*60)
    print("\nGenerate QR codes for URLs, WiFi, contacts, and more!")
    
    while True:
        display_menu()
        choice = input("\nSelect option (0-9): ").strip()
        
        if choice == '1':
            print("\n📱 URL/WEBSITE LINK")
            print("-"*60)
            url = input("Enter URL (e.g., https://example.com): ").strip()
            if url:
                filename = input("Filename (default: url_qrcode.png): ").strip()
                if not filename:
                    filename = "url_qrcode.png"
                create_basic_qr(url, filename)
            else:
                print("⚠️  URL cannot be empty!")
        
        elif choice == '2':
            print("\n📝 PLAIN TEXT")
            print("-"*60)
            text = input("Enter text: ").strip()
            if text:
                filename = input("Filename (default: text_qrcode.png): ").strip()
                if not filename:
                    filename = "text_qrcode.png"
                create_basic_qr(text, filename)
            else:
                print("⚠️  Text cannot be empty!")
        
        elif choice == '3':
            print("\n📶 WIFI NETWORK")
            print("-"*60)
            ssid = input("WiFi Name (SSID): ").strip()
            password = input("Password: ").strip()
            print("\nSecurity Type:")
            print("  1. WPA/WPA2 (default)")
            print("  2. WEP")
            print("  3. None")
            security_choice = input("Select (1-3): ").strip()
            
            security_map = {"1": "WPA", "2": "WEP", "3": ""}
            security = security_map.get(security_choice, "WPA")
            
            filename = input("Filename (default: wifi_qrcode.png): ").strip()
            if not filename:
                filename = "wifi_qrcode.png"
            
            if ssid:
                create_wifi_qr(ssid, password, security, filename)
            else:
                print("⚠️  SSID cannot be empty!")
        
        elif choice == '4':
            print("\n📧 EMAIL ADDRESS")
            print("-"*60)
            email = input("Email address: ").strip()
            subject = input("Subject (optional): ").strip()
            body = input("Message (optional): ").strip()
            filename = input("Filename (default: email_qrcode.png): ").strip()
            if not filename:
                filename = "email_qrcode.png"
            
            if email:
                create_email_qr(email, subject, body, filename)
            else:
                print("⚠️  Email cannot be empty!")
        
        elif choice == '5':
            print("\n📱 PHONE NUMBER")
            print("-"*60)
            phone = input("Phone number: ").strip()
            filename = input("Filename (default: phone_qrcode.png): ").strip()
            if not filename:
                filename = "phone_qrcode.png"
            
            if phone:
                create_phone_qr(phone, filename)
            else:
                print("⚠️  Phone number cannot be empty!")
        
        elif choice == '6':
            print("\n💬 SMS MESSAGE")
            print("-"*60)
            phone = input("Phone number: ").strip()
            message = input("Message (optional): ").strip()
            filename = input("Filename (default: sms_qrcode.png): ").strip()
            if not filename:
                filename = "sms_qrcode.png"
            
            if phone:
                create_sms_qr(phone, message, filename)
            else:
                print("⚠️  Phone number cannot be empty!")
        
        elif choice == '7':
            print("\n👤 CONTACT CARD (vCard)")
            print("-"*60)
            name = input("Full name: ").strip()
            phone = input("Phone number (optional): ").strip()
            email = input("Email (optional): ").strip()
            filename = input("Filename (default: vcard_qrcode.png): ").strip()
            if not filename:
                filename = "vcard_qrcode.png"
            
            if name:
                create_vcard_qr(name, phone, email, filename)
            else:
                print("⚠️  Name cannot be empty!")
        
        elif choice == '8':
            print("\n✨ STYLED QR CODE")
            print("-"*60)
            data = input("Enter data (URL/text): ").strip()
            if data:
                print("\nStyle options:")
                print("  1. Rounded (default)")
                print("  2. Circle")
                print("  3. Gapped Square")
                style_choice = input("Select style (1-3): ").strip()
                
                style_map = {"1": "rounded", "2": "circle", "3": "gapped"}
                style = style_map.get(style_choice, "rounded")
                
                color = get_color_choice()
                filename = input("Filename (default: styled_qrcode.png): ").strip()
                if not filename:
                    filename = "styled_qrcode.png"
                
                create_styled_qr(data, filename, style, color)
            else:
                print("⚠️  Data cannot be empty!")
        
        elif choice == '9':
            print("\n🎨 COLORED QR CODE")
            print("-"*60)
            data = input("Enter data (URL/text): ").strip()
            if data:
                print("\nForeground color:")
                fg_color = get_color_choice()
                
                print("\nBackground color:")
                bg_color = get_color_choice()
                
                filename = input("Filename (default: colored_qrcode.png): ").strip()
                if not filename:
                    filename = "colored_qrcode.png"
                
                create_colored_qr(data, filename, fg_color, bg_color)
            else:
                print("⚠️  Data cannot be empty!")
        
        elif choice == '0':
            print("\n" + "="*60)
            print("Thanks for using QR Code Generator!")
            print("="*60)
            print("Goodbye! 👋\n")
            break
        
        else:
            print("❌ Invalid option. Please enter 0-9.")


if __name__ == "__main__":
    main()