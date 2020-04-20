"""
CP1404/CP5632 Practical
State names in a dictionary
Program that uses a dictionary to store and display the australian state name and the abbreviations for the state
"""
"""https://github.com/jasongan234/CP1401p/blob/master/state_name.py"""
def main():
    CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT" : "Northern Territory",
                "WA" : "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania"}
    print(CODE_TO_NAME)


    for state in CODE_TO_NAME: # A loop that prints all the states
         print("{} " "is"" {}". format(state, CODE_TO_NAME[state]))

    state_code = input("Enter short state: ").upper() # input that gets the name of state can be inputted lower and upper cases
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ")

if __name__=='__main__':
    main()


