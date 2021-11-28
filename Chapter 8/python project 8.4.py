data = ['bayam','kangkung','wortel','selada']
print(data)
print('Menu : ')
a = print('A. Tambah data sayur')
b = print('B. Hapus data sayur')
c = print('C. Tampilkan data sayur')
try:
    while (True):
        pil = input('Pilihan Anda :')
        if (pil == 'a'):
            x = input ('Sayur Tambahan :')
            data.append(x)
        if (pil == 'b'):
            y = input('Data yang dihapus : ')
            data.remove(y)
        if (pil == 'c'):
            print(data)
            break
except ValueError:
    print('Data tidak ditemukan')
