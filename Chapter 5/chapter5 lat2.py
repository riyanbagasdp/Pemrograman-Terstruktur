nilaiBhsIndo = -5
print("Masukkan nilai Bhs Indonesia :" + str(nilaiBhsIndo))
nilaiIPA = 92
print("Masukkan nilai IPA           :" + str(nilaiIPA))
nilaiMAT = 87
print("Masukkan nilai Matematika    :"  + str(nilaiMAT))
print (" ")
if (nilaiIPA >= 60) and (nilaiMAT > 70) and (nilaiBhsIndo >= 60):
    print ("Status Kelulusan             : LULUS")
elif (nilaiIPA < 0) or (nilaiMAT < 0) or (nilaiBhsIndo < 0):
     print ("Maaf input ada yang tidak valid")
else :
    print ("Status Kelulusan             : TIDAK LULUS")
