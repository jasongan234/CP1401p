"""https://github.com/jasongan234/CP1401p/blob/master/prac08/taxi_test.py"""
from prac08.taxi import Taxi


def main():

    new_taxi = Taxi(100)
    new_taxi.change_car_name("Prius 1")
    new_taxi.drive(40)
    print(new_taxi)
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)


main()

