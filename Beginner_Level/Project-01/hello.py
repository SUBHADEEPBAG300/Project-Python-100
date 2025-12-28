# Type to print any text in terminal using Python
# Direct Print
print('Hello World')
print("Hello World")
print("""Hello World""")

# Using variable Method
a = 'Hello World'
print(a)

# By taking user input
a = input("Type your message :-")
print(a)

# Printing with seperating
print("Hello", "World" , sep="-")

# Print Without print() by using libraries

# Using sys.stdout.write()
import sys
sys.stdout.write("Hello World!\n")

#using os.write()
import os
os.write(1, b"Hello World!\n") # 1 = stdout

# Type same message using looping system
a = input("Type your message :-")
b = int(input("Enter Repetation Time :-"))
for i in range(b):
    print(a)