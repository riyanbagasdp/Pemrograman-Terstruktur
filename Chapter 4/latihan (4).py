jarakab = 125
kecepatanab = 62
waktuab = int(jarakab/kecepatanab)*60
istirahatb = 45
jarakbc = 256
kecepatanbc = 70
waktubc = int(jarakbc/kecepatanbc)*60
totalwaktumenit = waktuab + istirahatb + waktubc
totalwaktujam = totalwaktumenit/60
print ("waktu yang dibutuhkan dalam menit = " + str(totalwaktumenit))
print ("waktu yang dibutuhkan dalam jam = " + str(totalwaktujam))
print ("perkiraan waktu pak amr sampai = " + str(6 + totalwaktujam) + " / 12.15")

