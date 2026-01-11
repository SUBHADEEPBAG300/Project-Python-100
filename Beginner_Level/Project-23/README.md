# Email Parser

A Python script that validates and parses email addresses, extracting the username, domain provider, and extensions.

## Description

This project provides a simple email parsing utility that:
- Validates email format using regular expressions
- Extracts and returns email components (username, domain provider, extensions)
- Handles invalid email formats gracefully

## Features

- ✅ Email format validation using regex
- ✅ Automatic lowercase conversion
- ✅ Extracts username, domain provider, and extensions
- ✅ Error handling for invalid email formats

## Requirements

- Python 3.x
- No external dependencies (uses built-in `re` module)

## Usage

### Function: `parse_email(email)`

Parses an email address and returns a dictionary with its components.

**Parameters:**
- `email` (str): The email address to parse

**Returns:**
- `dict`: A dictionary containing:
  - `"Email"`: The normalized (lowercase) email address
  - `"Username"`: The part before the `@` symbol
  - `"Domain Provider"`: The main domain name (first part after `@`)
  - `"Extensions"`: List of domain extensions (e.g., `['com']`, `['edu']`, `['gov', 'in']`)
- If invalid: `{"Error": "Invalid email format"}`

### Example

```python
from Email import parse_email

# Valid email
result = parse_email("user@example.com")
print(result)
# Output: {'Email': 'user@example.com', 'Username': 'user', 'Domain Provider': 'example', 'Extensions': ['com']}

# Email with multiple extensions
result = parse_email("data_analyst@banking.gov.in")
print(result)
# Output: {'Email': 'data_analyst@banking.gov.in', 'Username': 'data_analyst', 'Domain Provider': 'banking', 'Extensions': ['gov', 'in']}

# Invalid email
result = parse_email("invalid-email")
print(result)
# Output: {'Error': 'Invalid email format'}
```

## Running the Script

Simply run the script to see example outputs:

```bash
python Email.py
```

### Sample Output

```
{'Email': 'suman251@gmail.com', 'Username': 'suman251', 'Domain Provider': 'gmail', 'Extensions': ['com']}
{'Email': 'arindam456@yahoo.com', 'Username': 'arindam456', 'Domain Provider': 'yahoo', 'Extensions': ['com']}
{'Email': 'student.brainware@university.edu', 'Username': 'student.brainware', 'Domain Provider': 'university', 'Extensions': ['edu']}
{'Email': 'data_analyst@banking.gov.in', 'Username': 'data_analyst', 'Domain Provider': 'banking', 'Extensions': ['gov', 'in']}
```

## Email Validation Pattern

The script uses the following regex pattern for validation:
```
^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$
```

This pattern ensures:
- Username can contain letters, numbers, dots, underscores, percent signs, plus signs, and hyphens
- Domain must contain at least one dot
- Extension must be at least 2 characters long

## Project Structure

```
Project-23/
├── Email.py      # Main email parser script
└── README.md     # This file
```

## Author

Part of the Python 100 Projects series - Beginner Level

