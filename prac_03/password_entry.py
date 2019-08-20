"""
Program that asks the user for a password
and prints asterisks based on its length.
"""

MIN_LENGTH = 6


def main():
    """Get password and print asterisks."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """"Print number of asterisks equal to password length."""
    print("*" * len(password))


def get_password():
    """Get password and check length is valid."""
    password = input("Enter password that contains {} or more characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Invalid password!")
        password = input("Enter password that contains {} or more characters: ".format(MIN_LENGTH))
    return password


main()
