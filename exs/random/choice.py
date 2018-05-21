import random

def choose(k, l, n):  
    n = 1000
    x = 0
    for i in range(n):
        if random.choice(l) == 1:
            x += 1
    return (x/n)*100, x

