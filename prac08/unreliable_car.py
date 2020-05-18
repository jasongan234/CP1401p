"""https://github.com/jasongan234/CP1401p/blob/master/prac08/unreliable_car.py"""
from random import randint
from prac08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_numbers = randint(1, 100)
        if random_numbers >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

