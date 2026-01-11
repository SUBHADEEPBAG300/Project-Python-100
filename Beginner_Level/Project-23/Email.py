import re

def parse_email(email):
    email = email.lower()
    pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    
    if re.match(pattern, email):
        username, domain = email.split('@')
        parts = domain.split('.')
        provider = parts[0]
        extensions = parts[1:] 
        return {
            "Email": email,
            "Username": username,
            "Domain Provider": provider,
            "Extensions": extensions
        }
    else:
        return {"Error": "Invalid email format"}

emails = [
    "suman251@gmail.com",
    "arindam456@yahoo.com",
    "student.brainware@university.edu",
    "data_analyst@banking.gov.in"
]

for e in emails:
    print(parse_email(e))