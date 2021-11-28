# membuka dan mau membaca file d:/aku.txt
buka=input("Masukkan nama file: ")
print("Isi file " + buka + " adalah:")
file=open (buka, "r")
print (file.read())