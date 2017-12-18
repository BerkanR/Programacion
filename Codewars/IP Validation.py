# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if
# they consist of four octets, with values between 0..255 (included).

# Input to the function is guaranteed to be a single string.

# Examples

# // valid inputs:
# 1.2.3.4
# 123.45.67.89

# // invalid inputs:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089

# Note: leading zeros (e.g. 01.02.03.04) are considered not valid in this kata!

import string


def is_valid_IP(strng):
    if strng == '':
        return False
    lista = strng.split(".")
    if len(lista) != 4:
        return False
    for elemento in lista:
        if elemento[0] in string.ascii_letters:
            return False
        elif ' ' in elemento:
            return False
        elif int(elemento) not in range(0, 256):
            return False
        elif int(elemento[0]) == 0 and len(elemento) > 1:
            return False
    return True


assert (is_valid_IP("12.255.56.1")) == True, "Es una IP correcta, devuelve True"
assert (is_valid_IP('')) == False, "Es una IP incorrecta, devuelve False"
assert (is_valid_IP("abc.def.ghi.jkl")) == False, "Es una IP incorrecta, devuelve False"
assert (is_valid_IP("123.456.789.0")) == False, "Es una IP incorrecta, devuelve False"
assert (is_valid_IP("12.34.56")) == False, "Es una IP incorrecta, devuelve False"
assert (is_valid_IP("12.34.56 .1")) == False, "Es una IP incorrecta, devuelve False"
assert (is_valid_IP("12.34.56.-1")) == False, "Es una IP incorrecta, devuelve False"
assert (is_valid_IP("123.045.067.089")) == False, "Es una IP incorrecta, devuelve False"
assert (is_valid_IP("127.1.1.0")) == True, "Es una IP correcta, devuelve True"
assert (is_valid_IP("0.0.0.0")) == True, "Es una IP correcta, devuelve True"
assert (is_valid_IP("0.34.82.53")) == True, "Es una IP correcta, devuelve True"
assert (is_valid_IP("192.168.1.300")) == False, "Es una IP incorrecta, devuelve False"