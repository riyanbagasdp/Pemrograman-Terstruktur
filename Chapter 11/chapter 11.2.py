from datetime import *
buka = open('dataperpustakaan.txt','a')
while True :
    a = input('Masukkan Kode Member : ')
    b = input('Masukkan Nama Member : ')
    c = input('Masukkan Judul Buku : ')
    sakpuniki = date.today()
    enjing = sakpuniki + timedelta(days=7)
    kalimat = (a + '|' + b + '|' + c + '|' + str(sakpuniki) + '|' + str(enjing) + '\n')
    buka.write(kalimat)
    
    tanya = input('Ulangi lagi (y/n) : ')
    if tanya in ('N','n'):
        buka.close()
        break
