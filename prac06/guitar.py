
current_year = 2020

class Guitar:

    def __init__(self,name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return int(current_year) - int(self.year)

    def __str__(self):
        return "{} ({}): ${}" .format(self.name, self.year, self.cost)

    def is_vintage(self):
        return self.get_age() >= 50

