data = []
huh = []
tuple=(data)
while True :
    nama = input('Data Mahasiswa :')
    data.append(nama)
    hahh = set(nama)
    huh.append(hahh)
    jwb = input('Mau input lagi (y/n)?')
    if jwb in ('N', 'n'):
        data.sort()
        print(data)
        print(huh)
        lenData = len(data)
        for i in data:
            print(i + ' ( ' + str(len(i)) + ' karakter )') 
 

