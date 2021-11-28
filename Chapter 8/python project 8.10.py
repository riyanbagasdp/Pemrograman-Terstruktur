def new_func():
    buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
    while True:
        nama = input('Nama buah yang dibeli : ')
        kg = input('Berapa Kg             : ')
        print('-'*33)
        a=buah[nama]
        print(a)
        b= int(kg)*int(a)
        data.append(b)
        total = input('Total harga           : Rp ' + str(b))
        print('')
        tanya=input('Beli buah yang lain (y/n)?')
        if (tanya == "y"):
            continue
        elif (tanya=="n"):
            hitung=sum(data)
            print (hitung)
            break

data = []
tuple=(data)
new_func()




