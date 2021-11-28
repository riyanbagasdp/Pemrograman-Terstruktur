# inisialisasi variable a dan b
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

# sisipkan data baru ditengah-tengah list
a.insert(3, 10)
a[len(a):]= [4]
b.insert(2, 15)
b[len(b):]= [8]
suba=sorted(a)
subb=sorted(b)
print(suba)
print(subb)
c = suba[0:7]
print(c)
d = subb[2:9]
print(d)
lenData = len(c)
e = []
i = 0
for i in range (lenData):
    temp = c[i]+d[i]
    e.append(temp)
hm = tuple(e)
print(hm)   
x = min(hm)
y = max(hm)
z = sum(hm)
print('Nilai terkecil : ' + str(x))
print('Nilai terbesar : ' + str(y))
print('Jumlah nilai  : ' + str(z))
myString = 'python adalah bahasa pemrograman yang menyenangkan'
oke = list(myString)
print(oke)
ya = set(oke)
print(ya)

