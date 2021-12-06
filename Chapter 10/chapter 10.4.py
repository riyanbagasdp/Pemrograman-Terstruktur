search = input("Masukan NIM yang ingin dicari : ")

file = open('datamhs.txt','r')


for i in file:
    a = i.split("|").copy()
    nim = i.split("|")[0]
    hasil = 0
    if(nim == search):
        hasil = a
        break
        

if(hasil):
    print("Data Mahasiswa")
    print("NIM         :", hasil[0])
    print("Nama        :", hasil[1])
    print("Alamat      :", hasil[2])
if search not in a:
    print("Data mahasiswa tidak ditemukan")
