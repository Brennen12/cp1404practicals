from random import randint

from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        if randint(0, 100) < self.reliability:
            return super().drive(distance)
