import random
from statistics import mode, median

class RandomNumbers:
    def __init__(self, count):
        self.count = count
        self.numbers = []

    def generate_numbers(self):
        self.numbers = [random.randint(0, 100) for _ in range(self.count)]

    def get_max(self):
        return max(self.numbers)

    def get_min(self):
        return min(self.numbers)

    def get_mode(self):
        return mode(self.numbers)

    def get_median(self):
        return median(self.numbers)

n = 100

random_numbers = RandomNumbers(n)
random_numbers.generate_numbers()

maximum = random_numbers.get_max()
minimum = random_numbers.get_min()
modus = random_numbers.get_mode()
median = random_numbers.get_median()

print("cisilka:", random_numbers.numbers)
print("max:", maximum)
print("min:", minimum)
print("Modus:", modus)
print("Median:", median)
