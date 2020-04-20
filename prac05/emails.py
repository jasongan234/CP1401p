""" Get names from emails using dictionary"""
"""https://github.com/jasongan234/CP1401p/blob/master/emails.py"""
def main():
    email_to_code = {}
    email = input("Enter your email: ")
    while email !="":
        name = get_name(email)
        to_confirm = input("Is your name {}? (Y/N) ".format(name))
        if to_confirm.upper() != "Y":
            name=input("Enter your name: ")
        email_to_code[email] = name
        email = input("Enter your email (Enter nothing to list out all emails): ")

    for email, name in email_to_code .items():
        print("{} ({})" .format(name, email))

def get_name(email):
    prefix = email .split('@')[0]
    parts = prefix.split('.')
    name = " ". join(parts).title()

    return name


main()