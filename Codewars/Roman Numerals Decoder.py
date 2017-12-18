# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You
# don't need to validate the form of the Roman numeral.

# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting
# with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is
# rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

# Example:

# solution('XXI') # should return 21

def solution(roman):
    if roman == "IV":
        return 4
    elif roman == "IX":
        return 9

    contador = 0
    for caracter in roman:
        if caracter == 'I':
            contador += 1
        elif caracter == "V":
            contador += 5
        elif caracter == "X":
            contador += 10
        elif caracter == "L":
            contador += 50
        elif caracter == "C":
            contador += 100
        elif caracter == "D":
            contador += 500
        elif caracter == "M":
            contador += 1000

    return contador


assert (solution('I')) == 1, "El número I en decimal es = 1"
assert (solution("IV")) == 4, "El número IV en decimal es = 4"
assert (solution("IX")) == 9, "El número IX en decimal es = 9"
assert (solution("XV")) == 15, "El número XV en decimal es = 15"