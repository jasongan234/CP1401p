"""https://github.com/jasongan234/CP1401p/blob/master/prac08/silver_service_taxi_test.py"""
from prac08.silver_service_taxi import SilverServiceTaxi

def main():

    taxi = SilverServiceTaxi(100, "Test Fancy Taxi", 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()