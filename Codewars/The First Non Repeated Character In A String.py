# You need to write a function, that returns the first non-repeated character in the given string.

# For example for string "test" function should return 'e'.
# For string "teeter" function should return 'r'.

# If a string contains all unique characters, then return just the first character of the string.
# Example: for input "trend" function should return 't'

# You can assume, that the input string has always non-zero length.

def first_non_repeated(s):
    for elemento in s:
        if s.count(elemento) == 1:
            return elemento


assert (first_non_repeated("test")) == 'e', "Tiene que devolver la letra e"
assert (first_non_repeated("teeter")) == 'r', "Tiene que devolver la letra r"
assert (first_non_repeated("1122321235121222")) == '5', "Tiene que devolver el string 5"