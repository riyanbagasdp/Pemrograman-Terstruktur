buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
i = 0
j = 0
while True:
    nama = input('Nama buah yang dibeli : ')
    kg = input('Berapa Kg             : ')
    print('-'*33)
    a=buah[nama]
    print(a)
    i+=nama
    j+=1 
    b= int(kg)*int(a)
    ans = input('Input lagi (y/n) ? ')
    if ans in ('N', 'n'):
        total = input('Total harga           : Rp ' + str(b))
        break



