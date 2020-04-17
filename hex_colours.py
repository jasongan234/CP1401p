
colours_to_code = {"aliceblue": "#f0f8ff",
                   "antiquewhite": "#faebd7",
                   "beige": "#f5f5dc",
                   "bisque1": "#ffe4c4",
                   "CadetBlue": "#5f9ea0",
                   "chartreuse1": "	#7fff00",
                   "DarkGoldenrod": "#b8860b",
                   "DarkGreen": "#006400",
                   "firebrick": "#b22222",
                   "FloralWhite": "#fffaf0"}
def main():
    colour_name = input("Enter Colour: ").lower()
    while colour_name !="":
        if colour_name in colours_to_code:
            print("The colour code for {} is {}".format(colour_name, colours_to_code[colour_name]))
        else:
            print("Invalid Colour")
        colour_name= input("Enter colour:").lower()


main()