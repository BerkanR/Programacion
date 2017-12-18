# Is Prime

# Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False depending on
# if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than
# 1 and itself.

# Example

# isPrime(5)
# => true

# Assumptions

# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).

def is_prime(num):
    if num < 2:
        return False
    for numero in range(2, num):
        if num % numero == 0:
            return False
    return True


assert (is_prime(0)) == False, "0 No es primo"
assert (is_prime(1)) == False, "1 No es primo"
assert (is_prime(2)) == True, "2 Es primo"
assert (is_prime(7)) == True, "7 Es primo"
assert (is_prime(-3)) == False, "No hay números negativos primos"