kode= input("Masukkan Kode Karyawan :")
nama= input("Masukkan Nama Karyawan :")
while(True):
    gol= str(input("Masukkan Golongan    : "))
    if (gol=="A") or (gol=="a"):
        gjp= 3500000
        pot= 2.5
        pothasil = round(3.5/100*3500000)
        gb = (gjp-pothasil)
        break
    elif (gol=="B") or (gol=="b"):
        gjp= 3000000
        pot= 2.0
        pothasil = round(3.0/100*3000000)
        gb = (gjp-pothasil)
        break
    elif (gol=="C") or (gol=="c"):
        gjp= 2500000
        pot= 1.5
        pothasil = round(2.5/100*2500000)
        gb = (gjp-pothasil)
        break
    elif (gol=="D") or (gol=="d"):
        gjp= 2000000
        pot= 1.0
        pothasil = round(2.0/100*2000000)
        gb = (gjp-pothasil)
        break
print (" ")
print ("="*35)
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("-"*35)
input ("Nama Karyawan   :")
input ("Golongan        :")
print ("-"*35)
print ("Gaji Pokok      : Rp " + str(gjp))
print ("Potongan (" + str(pot) + "%) : Rp " + str(pothasil))
print ("="*35)
print ("Gaji Bersih     : Rp " + str (gb))
