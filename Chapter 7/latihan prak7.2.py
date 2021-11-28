buka=input("Masukkan nama file: ")
file = open(buka, "a")
while True:
    data=input("Data yang mau ditambahkan: ")
    file.write(data)
    hasil=input("Mau lagi (y/n): ")
    if (hasil=="y"):
        continue
    if (hasil=="n"):
        file.close()
        break