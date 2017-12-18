# Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number
# of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
# True,  True,  True,  True ,
# True,  False, True,  False,
# True,  False, False, True ,
# True,  True,  True,  True ,
# False, False, True,  True]

# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(arrayOfSheeps):
    contador = 0
    for elemento in arrayOfSheeps:
        if elemento == True:
            contador += 1
    return contador


assert (count_sheeps([True, True, True, False,
                      True, True, True, True,
                      True, False, True, False,
                      True, False, False, True,
                      True, True, True, True,
                      False, False, True, True])) == 17, "Debería contar 17"