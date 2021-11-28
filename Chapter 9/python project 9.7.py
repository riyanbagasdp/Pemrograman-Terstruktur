def mhs():    
    mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
        'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
        'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
    
    # memecah list
    x = mhs[0].split(':')
    y = mhs[1].split(':')
    z = mhs[2].split(':')

    # mengurutkan ttl lahir rosihan ari
    ttl  = (x[2])
    ttlros = ttl.split('-')
    ttlros[0] = '01'
    ttlros[1] = '09'
    ttlros[2] = '1979'
    ttlrosihan = '/'.join(ttlros)
    # mengurutkan ttl lahir dwi amalia fitriani
    ttl  = (y[2])
    ttldwi = ttl.split('-')
    ttldwi[0] = '17'
    ttldwi[1] = '09'
    ttldwi[2] = '1979'
    ttldwiamalia = '/'.join(ttldwi)
    # mengurutkan ttl lahir faza fauzan
    ttl  = (z[2])
    ttlfaza = ttl.split('-')
    ttlfaza[0] = '28'
    ttlfaza[1] = '01'
    ttlfaza[2] = '2005'
    ttlfazafauzan = '/'.join(ttlfaza)

    print("===============================================================")
    print("NIM        NAMA MAHASISWA        TGL LAHIR     TEMPAT LAHIR")
    print("===============================================================")   
    print(x[0].ljust(11), end='')
    print(x[1].ljust(11), end='')
    print(ttlrosihan.rjust(21), end='')
    print(x[3].rjust(8))
    print(y[0].ljust(11), end='')
    print(y[1].ljust(11), end='')
    print(ttldwiamalia.rjust(13), end='')
    print(y[3].rjust(9)) 
    print(z[0].ljust(11), end='')
    print(z[1].ljust(11), end='')
    print(ttlfazafauzan.rjust(21), end='')
    print(z[3].rjust(15))
    print("--------------------------------------------------------------")


mhs()



 