# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    return s[1:-1]


assert (remove_char("eloquent")) == "loquen", "Error en la operación"
assert (remove_char("country")) == "ountr", "Error en la operación"
assert (remove_char("person")) == "erso", "Error en la operación"
assert (remove_char("place")) == "lac", "Error en la operación"
assert (remove_char("ok")) == '', "Tiene que poder devolver un string vacío"