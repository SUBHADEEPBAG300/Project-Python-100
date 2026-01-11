# Advanced Level

"""
Email Slicer
Extract and analyze email components: username, domain, and more.
"""

import re


def validate_email(email):
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def slice_email(email):
    """Slice email into username and domain."""
    if '@' not in email:
        return None, None
    
    parts = email.split('@')
    if len(parts) != 2:
        return None, None
    
    username = parts[0]
    domain = parts[1]
    
    return username, domain


def get_domain_info(domain):
    """Extract detailed domain information."""
    if not domain:
        return None
    
    parts = domain.split('.')
    
    info = {
        'full_domain': domain,
        'domain_name': '.'.join(parts[:-1]) if len(parts) > 1 else domain,
        'tld': parts[-1] if len(parts) > 1 else '',
        'subdomain': parts[0] if len(parts) > 2 else '',
        'main_domain': parts[-2] if len(parts) > 1 else parts[0]
    }
    
    return info


def identify_email_provider(domain):
    """Identify popular email providers."""
    providers = {
        'gmail.com': 'Google Gmail',
        'yahoo.com': 'Yahoo Mail',
        'outlook.com': 'Microsoft Outlook',
        'hotmail.com': 'Microsoft Hotmail',
        'icloud.com': 'Apple iCloud',
        'protonmail.com': 'ProtonMail',
        'aol.com': 'AOL Mail',
        'zoho.com': 'Zoho Mail',
        'mail.com': 'Mail.com',
        'yandex.com': 'Yandex Mail',
        'gmx.com': 'GMX Mail',
        'tutanota.com': 'Tutanota'
    }
    
    domain_lower = domain.lower()
    for provider_domain, provider_name in providers.items():
        if domain_lower == provider_domain or domain_lower.endswith('.' + provider_domain):
            return provider_name
    
    return 'Custom/Business Domain'


def analyze_username(username):
    """Analyze username patterns and characteristics."""
    if not username:
        return None
    
    analysis = {
        'length': len(username),
        'has_numbers': bool(re.search(r'\d', username)),
        'has_dots': '.' in username,
        'has_underscores': '_' in username,
        'has_hyphens': '-' in username,
        'starts_with_number': username[0].isdigit() if username else False,
        'all_lowercase': username.islower(),
        'all_uppercase': username.isupper(),
        'mixed_case': not username.islower() and not username.isupper()
    }
    
    return analysis


def display_email_analysis(email):
    """Display complete email analysis."""
    # Validate email
    if not validate_email(email):
        print("\n❌ Invalid email format!")
        return
    
    # Slice email
    username, domain = slice_email(email)
    
    if not username or not domain:
        print("\n❌ Could not parse email!")
        return
    
    # Get domain info
    domain_info = get_domain_info(domain)
    provider = identify_email_provider(domain)
    username_analysis = analyze_username(username)
    
    # Display results
    print("\n" + "="*70)
    print("📧 EMAIL ANALYSIS")
    print("="*70)
    print(f"\nFull Email:        {email}")
    print("\n" + "-"*70)
    print("COMPONENTS:")
    print("-"*70)
    print(f"Username:          {username}")
    print(f"Domain:            {domain}")
    print(f"Provider:          {provider}")
    
    print("\n" + "-"*70)
    print("DOMAIN DETAILS:")
    print("-"*70)
    if domain_info:
        print(f"Full Domain:       {domain_info['full_domain']}")
        print(f"Main Domain:       {domain_info['main_domain']}")
        print(f"TLD (Extension):   {domain_info['tld']}")
        if domain_info['subdomain']:
            print(f"Subdomain:         {domain_info['subdomain']}")
    
    print("\n" + "-"*70)
    print("USERNAME ANALYSIS:")
    print("-"*70)
    if username_analysis:
        print(f"Length:            {username_analysis['length']} characters")
        print(f"Contains numbers:  {'Yes' if username_analysis['has_numbers'] else 'No'}")
        print(f"Contains dots:     {'Yes' if username_analysis['has_dots'] else 'No'}")
        print(f"Contains underscores: {'Yes' if username_analysis['has_underscores'] else 'No'}")
        print(f"Case type:         ", end="")
        if username_analysis['all_lowercase']:
            print("All lowercase")
        elif username_analysis['all_uppercase']:
            print("All uppercase")
        elif username_analysis['mixed_case']:
            print("Mixed case")
        else:
            print("N/A")
    
    print("="*70)


def batch_slice_emails(email_list):
    """Process multiple emails at once."""
    print("\n" + "="*70)
    print("📊 BATCH EMAIL PROCESSING")
    print("="*70)
    print(f"\nProcessing {len(email_list)} emails...\n")
    print("-"*70)
    print(f"{'Email':<30} {'Username':<15} {'Domain':<20} {'Provider'}")
    print("-"*70)
    
    valid_count = 0
    invalid_count = 0
    
    for email in email_list:
        email = email.strip()
        if validate_email(email):
            username, domain = slice_email(email)
            provider = identify_email_provider(domain)
            
            # Truncate long values for display
            email_display = email[:27] + "..." if len(email) > 30 else email
            username_display = username[:12] + "..." if len(username) > 15 else username
            domain_display = domain[:17] + "..." if len(domain) > 20 else domain
            provider_display = provider[:30]
            
            print(f"{email_display:<30} {username_display:<15} {domain_display:<20} {provider_display}")
            valid_count += 1
        else:
            print(f"{email:<30} {'INVALID EMAIL'}")
            invalid_count += 1
    
    print("-"*70)
    print(f"\nValid emails: {valid_count}")
    print(f"Invalid emails: {invalid_count}")
    print("="*70)


def extract_domain_from_list(email_list):
    """Extract and count unique domains."""
    domains = {}
    
    for email in email_list:
        email = email.strip()
        if validate_email(email):
            _, domain = slice_email(email)
            if domain:
                domains[domain] = domains.get(domain, 0) + 1
    
    print("\n" + "="*70)
    print("🌐 DOMAIN STATISTICS")
    print("="*70)
    print(f"\nTotal unique domains: {len(domains)}\n")
    print("-"*70)
    print(f"{'Domain':<40} {'Count'}")
    print("-"*70)
    
    # Sort by count (descending)
    sorted_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)
    
    for domain, count in sorted_domains:
        provider = identify_email_provider(domain)
        print(f"{domain:<40} {count:>5}  ({provider})")
    
    print("="*70)


def generate_variations(username, domain):
    """Generate email variations."""
    print("\n" + "="*70)
    print("🔄 EMAIL VARIATIONS")
    print("="*70)
    print(f"\nBase: {username}@{domain}\n")
    print("Possible variations:")
    
    variations = [
        f"{username}@{domain}",
        f"{username.replace('.', '')}@{domain}",
        f"{username.replace('_', '.')}@{domain}",
        f"{username}.work@{domain}",
        f"{username}.personal@{domain}",
        f"{username}1@{domain}",
        f"{username}2024@{domain}"
    ]
    
    for i, var in enumerate(variations, 1):
        print(f"  {i}. {var}")
    
    print("="*70)


def mask_email(email, mask_char='*'):
    """Mask email for privacy."""
    username, domain = slice_email(email)
    
    if not username or not domain:
        return email
    
    # Mask username (show first and last char)
    if len(username) <= 2:
        masked_username = mask_char * len(username)
    else:
        masked_username = username[0] + mask_char * (len(username) - 2) + username[-1]
    
    # Mask domain (show only TLD)
    domain_parts = domain.split('.')
    if len(domain_parts) > 1:
        masked_domain = mask_char * len(domain_parts[0]) + '.' + domain_parts[-1]
    else:
        masked_domain = mask_char * len(domain)
    
    return f"{masked_username}@{masked_domain}"


def main():
    """Main program execution."""
    print("="*70)
    print("           📧 EMAIL SLICER 📧")
    print("="*70)
    print("\nExtract and analyze email components!")
    
    while True:
        print("\n" + "-"*70)
        print("MENU:")
        print("  1. Slice Single Email (detailed analysis)")
        print("  2. Quick Slice (simple username/domain)")
        print("  3. Batch Process (multiple emails)")
        print("  4. Domain Statistics (from list)")
        print("  5. Generate Email Variations")
        print("  6. Mask Email (privacy)")
        print("  7. Exit")
        print("-"*70)
        
        choice = input("\nSelect option (1-7): ").strip()
        
        if choice == '1':
            print("\n" + "="*70)
            print("📧 DETAILED EMAIL ANALYSIS")
            print("="*70)
            email = input("Enter email address: ").strip()
            if email:
                display_email_analysis(email)
            else:
                print("⚠️  Email cannot be empty!")
        
        elif choice == '2':
            print("\n" + "="*70)
            print("⚡ QUICK SLICE")
            print("="*70)
            email = input("Enter email address: ").strip()
            
            if email:
                if validate_email(email):
                    username, domain = slice_email(email)
                    print("\n" + "-"*70)
                    print(f"Username:  {username}")
                    print(f"Domain:    {domain}")
                    print("-"*70)
                else:
                    print("\n❌ Invalid email format!")
            else:
                print("⚠️  Email cannot be empty!")
        
        elif choice == '3':
            print("\n" + "="*70)
            print("📋 BATCH PROCESSING")
            print("="*70)
            print("Enter email addresses (one per line).")
            print("Press Enter twice when done.\n")
            
            emails = []
            empty_count = 0
            
            while True:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count >= 2:
                        break
                else:
                    empty_count = 0
                    emails.append(line)
            
            if emails:
                batch_slice_emails(emails)
            else:
                print("⚠️  No emails entered!")
        
        elif choice == '4':
            print("\n" + "="*70)
            print("📊 DOMAIN STATISTICS")
            print("="*70)
            print("Enter email addresses (one per line).")
            print("Press Enter twice when done.\n")
            
            emails = []
            empty_count = 0
            
            while True:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count >= 2:
                        break
                else:
                    empty_count = 0
                    emails.append(line)
            
            if emails:
                extract_domain_from_list(emails)
            else:
                print("⚠️  No emails entered!")
        
        elif choice == '5':
            print("\n" + "="*70)
            print("🔄 EMAIL VARIATIONS")
            print("="*70)
            email = input("Enter base email address: ").strip()
            
            if email:
                if validate_email(email):
                    username, domain = slice_email(email)
                    generate_variations(username, domain)
                else:
                    print("\n❌ Invalid email format!")
            else:
                print("⚠️  Email cannot be empty!")
        
        elif choice == '6':
            print("\n" + "="*70)
            print("🔒 MASK EMAIL")
            print("="*70)
            email = input("Enter email address: ").strip()
            
            if email:
                if validate_email(email):
                    masked = mask_email(email)
                    print("\n" + "-"*70)
                    print(f"Original:  {email}")
                    print(f"Masked:    {masked}")
                    print("-"*70)
                else:
                    print("\n❌ Invalid email format!")
            else:
                print("⚠️  Email cannot be empty!")
        
        elif choice == '7':
            print("\n" + "="*70)
            print("Thanks for using Email Slicer!")
            print("="*70)
            print("Goodbye! 👋\n")
            break
        
        else:
            print("❌ Invalid option. Please enter 1-7.")


if __name__ == "__main__":
    main()