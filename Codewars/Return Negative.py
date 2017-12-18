# In this simple assignment you are given a number and have to make it negative. But maybe the number is already
# negative?

# Example:

# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0

# Notes:

# The number can be negative already, in which case no change is required.
# Zero (0) can't be negative, see examples above.

def make_negative(number):
    if number == 0:
        return 0
    elif number < 0:
        return number
    elif number > 0:
        return -number
    else:
        pass


assert (make_negative(0)) == 0, "Debería devolver 0"
assert (make_negative(42)) == -42, "Debería devolver el número en negativo"
assert (make_negative(-9)) == -9, "Debería devolver el número negativo igual"