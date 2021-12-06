fileasal = open('pythonlima.txt','r')
filehasil = open('pythonlima2.txt','w')

moco = fileasal.readlines()
for a in range(len(moco)):
    x = moco[a].split('|')
    hasil = int(x[0])+ int(x[1])
    print(hasil)
    filehasil.write(str(hasil)+'\n')
fileasal.close()
filehasil.close()
