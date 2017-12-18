# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, which should be
# separated by an ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# returns 'Bart'

# namelist([])
# returns ''

# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
    nuevaLista = []
    for valor in names:
        nuevaLista.append(valor["name"])
    stringValores = ', '.join(nuevaLista)
    return ' &'.join(stringValores.rsplit(',', 1))


assert (namelist([])) == '', "Debería funcionar con una lista vacía"
assert (namelist([{'name': 'Bart'}])) == "Bart", "Error para el formateo de un solo nombre"
assert (namelist([{'name': 'Bart'},{'name': 'Lisa'}])) == "Bart & Lisa", "Error para el formateo de más de un nombre"
assert (namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}])) == "Bart, Lisa & Maggie", "Error para el formateo de tres nombres"
assert (namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])) == "Bart, Lisa, Maggie, Homer & Marge", "Error para el formateo de más de tres nombres"