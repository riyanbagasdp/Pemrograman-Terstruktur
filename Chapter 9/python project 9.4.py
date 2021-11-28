def ulangi(nama,n):   
    import random
    nm = (nama)
    l = list(nm)
    s = 0
    hsl = []
    for s in range(n):
        import random
        y = random.shuffle(l)
        x= result = ''.join(l)
        hsl.append(x)
    print(hsl,end='')

ulangi('aku',4)