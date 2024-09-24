# Program to check if the given character is an alphabet
char = input("Enter a character: ")

if char.isalpha():
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet.")