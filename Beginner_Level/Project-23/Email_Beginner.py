# Beginner Level

def email_slicer(email):
    username, domain = email.split('@')
    return username, domain

email = "john@gmail.com"
username, domain = email_slicer(email)
print("Username:", username)
print("Domain:", domain)
