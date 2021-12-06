buka = open('ilikepiton.txt','r')
buka2 = open('pitonacak.txt','a')

# membaca file
a = buka.read()
# menjadikan set
b = set(a)
# menghapus tanda ' '
b.remove(' ')
# menjadikan list
c = list(b)
# membalik string
c.sort(reverse=True)
d = 2
hasil = a.replace(c[0], chr(ord(c[0])+d))
e = 1
while True:
    hasil = hasil.replace(c[e], chr(ord(c[e])+d))
    e = e + 1

    if (e!=10):
        continue
    elif (e==10):
        break

hasil = hasil.replace(chr(91), chr(65))
hasil = hasil.replace(chr(92), chr(66))

x = print(hasil)
buka2.write(hasil)
buka.close()
buka2.close()
