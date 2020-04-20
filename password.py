"""https://github.com/jasongan234/CP1401p/blob/master/password.py"""
def main():
    """Getting and printing password with the use of functions"""
    minimum_length=2
    password=get_password(minimum_length)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, ensure it is above minimum lenght"""
    password=input("Enter your password of at least {} characters: ". format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter your password of at least {} characters: ".format(minimum_length))
    return password
def print_asterisks(sequence):
    print('*' * len(sequence))
main()