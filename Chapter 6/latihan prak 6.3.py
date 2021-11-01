def faktorial(a, b):
    import math

    faktorial = math.factorial(a)
    faktorial1 = math.factorial(b)
    x = a - b
    faktorial2 = math.factorial(x)
    rumus = faktorial/(faktorial2 * faktorial1)

    print(f'{(a, b)}! = {rumus}')

faktorial(5, 3)
