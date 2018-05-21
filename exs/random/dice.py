import random
import math

class dice():
    def __init__(self, sides = 6):
        self.sides = sides
    
    def __str__(self):
        return self.roll()

    def roll(self, times = 1):
        rolls = []
        for i in range(times):
            rolls.append(random.randint(1, self.sides))
        return rolls