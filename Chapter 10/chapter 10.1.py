import pathlib
rms = current_dir = str(pathlib.Path(__file__).parent)

bil = open(rms + 'dataC10.txt','r')
ganjil = 0
genap  = 0

for i in bil:
    if int(i) % 2 == 0:
        genap = genap + 1
    else:
        ganjil = ganjil + 1
bil.close()
        

print("Banyaknya bilangan genap  :",genap)
print("Banyaknya bilangan ganjil :",ganjil)
