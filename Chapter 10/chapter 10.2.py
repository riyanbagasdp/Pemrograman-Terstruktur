# program input data mahasiswa

buka = open('datamhs.txt','a')

while True :
    nim = input('Masukkan NIM : ')
    nama = input('Masukkan Nama Mahasiswa : ')
    alamat = input('Masukkan Alamat : ')

    kalimat = (nim + '|' + nama + '|' + alamat + '\n')
    buka.write(kalimat)

    jwb = input('Mau input data lagi (y/n) ?')
    if (jwb == 'Y') or (jwb == 'y'):
        continue
    if (jwb == 'N') or (jwb == 'n'):
        break

buka.close()
