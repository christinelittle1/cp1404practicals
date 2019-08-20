"""
Christine
"""

MIN_LENGTH = 6


def main():
    """Get user's password and count length."""
    password = input("Enter password that contains {} or more characters: ".format(MIN_LENGTH))
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("Enter password that contains {} or more characters: ".format(MIN_LENGTH))
    print("*" * len(password))


def is_valid_password(password):
    """Check if password is valid."""
    if len(password) < MIN_LENGTH:
        return False
    return True


main()