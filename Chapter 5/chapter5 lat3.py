nilaiBhsIndo = 55
print("Masukkan nilai Bhs Indonesia :" + str(nilaiBhsIndo))
nilaiIPA = 92
print("Masukkan nilai IPA           :" + str(nilaiIPA))
nilaiMAT = 67
print("Masukkan nilai Matematika    :" + str(nilaiMAT))
kkmbi = 60
kkmmat = 70
kkmipa = 60
print (" ")
if (nilaiIPA >= 60) and (nilaiMAT > 70) and (nilaiBhsIndo >= 60):
    print ("Status Kelulusan             : LULUS")
elif (nilaiIPA < 0) or (nilaiMAT < 0) or (nilaiBhsIndo < 0):
    print ("Maaf input ada yang tidak valid")
else :
    print ("Status Kelulusan             : TIDAK LULUS")
print ("Sebab                        :")
if (nilaiBhsIndo < 60):
    print ("- Nilai bahasa indonesia kurang dari",str(kkmbi))
if (nilaiIPA < 60):
    print ("- IPA kurang dari",str(kkmipa))
if (nilaiMAT < 70):
    print ("- Nilaimatematikanya kurang dari",str(kkmmat))
