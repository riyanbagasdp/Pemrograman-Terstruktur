from datetime import *
try:
    file = open('dataperpustakaan.txt','r')
    kode = input('Masukkan Kode Member : ')
    for i in file:
        a = i.split("|").copy()
        nim = i.split("|")[0]
        hasil = 0
        if(nim == kode):
            hasil = a
            break
    harini = date.today()
    thn,bln,hr = hasil[4].split('-')
    tenggat = date(int(thn), int(bln), int(hr))
    final = harini - tenggat
    beda = final.days
    if (hasil):
        print('Data Peminjaman Buku')
        print("Kode Member                   :", hasil[0])
        print("Nama Member                   :", hasil[1])
        print("Judul Buku                    :", hasil[2])
        print("Tanggal Mulai Peminjaman      :", hasil[3])
        print("Tanggal Maks Peminjaman       :", hasil[4])
        print("Tanggal pengembalian          :", harini)
        print("Terlambat                     :", str(beda) + ' hari')
        if (beda >= 0):
            denda = beda*2000
            denda2 = denda * -1
            print("Denda                         :", 'Rp ' + str(denda2))
        if (beda <= 0):
            print("Denda                         :", 'Rp 0')
    if kode not in a:
        print("Data mahasiswa tidak ditemukan")
except TypeError :
    print ('Data tidak ditemukan')

