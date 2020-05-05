"""https://github.com/jasongan234/CP1401p/blob/master/prac06/guitars.py"""
from prac06.guitar import Guitar


def main():
    guitars = []

    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: $")
        add_guitars = Guitar(name, year, cost)
        guitars.append(Guitar(name, year, cost))
        print(add_guitars, "added")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:10}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))
        else:
            print("Guitar {}: {:>20} ({}), worth ${:10}".format(i + 1, guitar.name, guitar.year, guitar.cost))



main()
