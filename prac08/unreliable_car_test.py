
from prac08.unreliable_car import UnreliableCar


def main():

    good_car = UnreliableCar(100, "Mostly Good", 90)
    good_car.change_car_name("Good Car")
    bad_car = UnreliableCar(100, "Quite bad", 9)
    bad_car.change_car_name("Bad Car")

    for i in range(1, 12):
        drive_good_car = good_car.drive(i)
        drive_bad_car = bad_car.drive(i)
        print("Driving {}km:".format(i))
        print("{} drove {}km".format(good_car.name, drive_good_car))
        print("{} drove {}km".format(bad_car.name, drive_bad_car))

    print(good_car)
    print(bad_car)


main()