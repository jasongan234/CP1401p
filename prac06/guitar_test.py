
from prac06.guitar import Guitar

def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2013, 2000)

    print("{} get_age() - Expected 98. Got {}".format(guitar.name, guitar.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another_guitar.name,  another_guitar.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(guitar.name, guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


main()



