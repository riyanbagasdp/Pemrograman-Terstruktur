from datetime import *
def diffDate(a,b,c):
    # mengambil tanggal dari today()
    sakpuniki = date.today()
    sakmeniko = date(year=a,month=b,day=c)
    tgl = str(sakpuniki.year) + '-' + str(sakpuniki.month) + '-' + str(sakpuniki.day) 
    tgl2 = str(sakmeniko.year) + '-' + str(sakmeniko.month) + '-' + str(sakmeniko.day) 
    x = datetime.strptime(str(tgl), '%Y-%m-%d')
    y = datetime.strptime(str(tgl2), '%Y-%m-%d')
    z = y-x
    print(z)
    return z
    


diffDate(2021,12,9)

