
def isPythagoras(a, b, c):
    x = (a**2) + (b**2)
    y = (c**2) - (b**2)
    z = (c**2) - (a**2)

    while True:
        if (c**2 == x)or(a**2 == y)or(b**2 == z):
            print('True')
        else:
            print('False')
        break

isPythagoras(3, 4, 5)
