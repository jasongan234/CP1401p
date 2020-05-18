"""https://github.com/jasongan234/CP1401p/blob/master/prac08/taxi_simulator.py"""
from prac08.car import Car
from prac08.taxi import Taxi
from prac08.silver_service_taxi import SilverServiceTaxi

Menu = "(Q)uit, (C)hoose Taxi, (D)rive"

def main():
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Lets Drive!")
    print(Menu)
    menu_choice = input("...").lower()
    while menu_choice != "":
        if menu_choice == "c":
            print("Taxis: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose your taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(total_cost))

        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("How far do you wish to drive? "))
            current_taxi.drive(int(distance_to_drive))
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
            total_cost += trip_cost
            print("Bill to date: ${:.2f}".format(total_cost))

        elif menu_choice == "q":
            print("Total trip cost: ${:.2f}".format(total_cost))
            print("Taxis are now: ")
            display_taxis(taxis)
            break

        print(Menu)
        menu_choice = input("...").lower()

    else:
        print("Invalid Input")


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()