kode= input("Masukkan Kode Karyawan :")
nama= input("Masukkan Nama Karyawan :")
if(True):
    gol= str(input("Masukkan Golongan      :"))
    status= str(input("Masukkan Status        :"))
    if  (status=="1" or status=="menikah"):
        anak= str(input("Masukkan Jumlah Anak   :"))
    if (status=="2" or status=="belum"):
        print (" ")
    if (gol=="A") or (gol=="a")and (status=="1") or (status=="menikah") :
        gjp= 3500000
        pot= 2.5
        pothasil = round(3.5/100*3500000)
        gb = (gjp-pothasil)
        tunjmnkh = round(10/100*3500000)
        tunjanak = round(5/100*3500000)
    if (gol=="B") or (gol=="b")and(status=="1") or (status=="menikah") :
        gjp= 3000000
        pot= 2.0
        pothasil = round(3.0/100*3000000)
        gb = (gjp-pothasil)
        tunjmnkh = round(8/100*3000000)
        tunjanak = round(4/100*3000000)
    if (gol=="C") or (gol=="c")and(status=="1") or (status=="menikah") :
        gjp= 2500000
        pot= 1.5
        pothasil = round(2.5/100*2500000)
        gb = (gjp-pothasil)
        tunjmnkh = round(6/100*2500000)
        tunjanak = round(3/100*2500000)
    if (gol=="D") or (gol=="d")and(status=="1") or (status=="menikah") :
        gjp= 2000000
        pot= 1.0
        pothasil = round(2.0/100*2000000)
        gb = (gjp-pothasil)
        tunjmnkh = round(4/100*2000000)
        tunjanak = round(2/100*2000000)
print (" ")
if (status=="2" or status =="belum"):
    tunjmnkh = 0
if (anak=="0"):
    tunjanak = 0
gjk = round(gjp + tunjmnkh + tunjanak)
gjbrsh = round(gjk-pothasil)
print ("="*35) 
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("-"*35)
print (" ") 
input ("Nama Karyawan         :")
input ("Golongan              :")
input ("Status Menikah        :")
if (status=="1" or status=="menikah"):
    input ("Jumlah Anak           :")
print ("-"*35)
print ("Gaji Pokok            : Rp " + str(gjp))
print ("Tunjangan Istri/Suami : Rp " + str (tunjmnkh))
if (status=="1" or status=="menikah"):
    print ("Tunjangan Anak        : Rp " + str(tunjanak*int(anak)))
print ("-"*35)
print ("Gaji Kotor            : Rp " + str(gjk))
print ("Potongan (" + str(pot) + "%)       : Rp " + str(pothasil))
print ("-"*35)
print ("Gaji Bersih           : Rp " + str(gjbrsh))
