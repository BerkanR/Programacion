# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest
# value.

# For example:

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5

import math


def litres(time):
    resultado = time * 0.5
    return math.trunc(resultado)


assert (litres(2)) == 1, "Debería devolver 1 litros"
assert (litres(1.4)) == 0, "Debería devolver 0 litros"
assert (litres(12.3)) == 6, "Debería devolver 6 litros"
assert (litres(0.82)) == 0, "Debería devolver 0 litros"
assert (litres(11.8)) == 5, "Debería devolver 5 litros"
assert (litres(1787)) == 893, "Debería devolver 893 litros"
assert (litres(0)) == 0, "Debería devolver 0 litros"