# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in
# descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:

# Input: 21445 Output: 54421

# Input: 145263 Output: 654321

# Input: 1254859723 Output: 9875543221

def descending_order(num):
    listaSeparadora = list(str(num))
    return int(''.join(sorted(listaSeparadora)[::-1]))


assert (descending_order(0)) == 0, "Tendría que devolver 0"
assert (descending_order(15)) == 51, "Tendría que devolver 51"
assert (descending_order(123456789)) == 987654321, "Tendría que devolver 987654321"