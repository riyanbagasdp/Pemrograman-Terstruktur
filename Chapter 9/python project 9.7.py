def mhs():    
    mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
        'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
        'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
    x = mhs[0].split(':')
    y = mhs[1].split(':')
    z = mhs[2].split(':')
    print(x[2].sort()) 
    print("===============================================================")
    print("NIM        NAMA MAHASISWA        TGL LAHIR     TEMPAT LAHIR")
    print("===============================================================")   
    print(x[0].ljust(11), end='')
    print(x[1].ljust(11), end='')
    print(x[2].rjust(21), end='')
    print(x[3].rjust(16))
    print(y[0].ljust(11), end='')
    print(y[1].ljust(11), end='')
    print(y[2].rjust(13), end='')
    print(y[3].rjust(16)) 
    print(z[0].ljust(11), end='')
    print(z[1].ljust(11), end='')
    print(z[2].rjust(21), end='')
    print(z[3].rjust(16))
    print("--------------------------------------------------------------")


mhs()



 