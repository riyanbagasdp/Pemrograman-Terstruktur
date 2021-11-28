nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print("===============================================================")
print("NIM        NAMA        N.MID     N.UAS      N.AKHIR    STATUS")
print("===============================================================")
for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(11), end='')
    print(nilai[i]['nama'].ljust(11), end='')
    print(str(nilai[i]['mid']).rjust(7), end='')
    print(str(nilai[i]['uas']).rjust(9), end='')
    y = ((nilai[i]['mid'])+(2*(nilai[i]['uas'])))/3
    x  = round(y)
    print(str(x).rjust(13),end='')
    if (x >= 60):
        print('LULUS'.rjust(10))
    else : 
        print('TIDAK LULUS'.rjust(10))
    
print("--------------------------------------------------------------")