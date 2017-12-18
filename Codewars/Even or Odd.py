# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


assert (even_or_odd(2)) == "Even", "Debe devolver Even"
assert (even_or_odd(0)) == "Even", "Debe devolver Even"
assert (even_or_odd(7)) == "Odd", "Debe devolver Odd"
assert (even_or_odd(1)) == "Odd", "Debe devolver Odd"