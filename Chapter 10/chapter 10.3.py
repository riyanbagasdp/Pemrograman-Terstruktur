# program input data mahasiswa

buka = open('datamhs.txt','r')
listmhs = []
datamhs = buka.readlines()
for i in range(len(datamhs)):
    pemisahan = datamhs[i].split('|')
    kalimat = {'nim':pemisahan[0],'nama':pemisahan[1],'alamat':pemisahan[2].replace('\n',' ')}
    listmhs.append(kalimat)
    
print(listmhs)
buka.close()
