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
# mengurutkan string
c.sort(reverse=True)
d = 0
hasil = a.replace(c[0], chr(ord(c[0])-d))
e = 1
while True:
    hasil = hasil.replace(c[e], chr(ord(c[e])-d))
    e = e + 1

    if (e!=10):
        continue
    elif (e==10):
        break

hasil = hasil.replace(chr(63), chr(89))
hasil = hasil.replace(chr(64), chr(90))

x = print(hasil)
buka2.write(hasil)
buka.close()
buka2.close()
