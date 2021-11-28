input('Menu :')
A = input('A. Tambah data buah')
B = input('B. Beli buah')
print('')
daftar={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
ans = input('Pilihan menu : ')
print('')
data = []
tuple=(data)
while True :
    if ans in ('A', 'a'):
        nama = input ('Massukkan nama buah: ')
        if (nama in daftar):
            print('Buah', nama, 'sudah ada dalam data')
        if (nama not in daftar):
            harga = int(input('Harganya (Rp): '))
            daftar[nama]=harga

    if ans in ('B', 'b'):
        nama = input('Nama buah yang dibeli : ')
        if (nama not in daftar):
            print('Buah', nama, 'tidak ada dalam data')
            continue
        kg = input('Berapa Kg             : ')
        print('-'*33)
        a=daftar[nama]
        print(a)
        b= int(kg)*int(a)
        data.append(b)
        total = input('Total harga           : Rp ' + str(b))
        print('')
        tanya=input('Beli buah yang lain (y/n)?')
        if (tanya == "y"):
            continue
        elif (tanya=="n"):
            print(data)
            hitung=sum(data)
            print (hitung)
            break
    jwb = input('Mau input lagi (y/n)?')
    if jwb in ('N', 'n'):
        print('Data buah:')
        for key, value in daftar.items():
            print(key,': Rp', value)
        break
    
