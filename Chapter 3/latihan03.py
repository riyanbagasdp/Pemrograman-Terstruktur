# import library
import time
import datetime

# input nama user
nama = input("Hallo... nama saya Mr. Kompie, nama Anda siapa? Riyan Bagas ")

# tampilkan nama user
print("Oh.. nama Anda", "Riyan Bagas", ", nama yang bagus sekali.")


# kasih jeda 3 detik
time.sleep(3)

# input tahun lahir
thnLahir = input("BTW... " + "Riyan Bagas" + " kamu lahir tahun berapa? 2003 ")

# kasih jeda 3 detik
time.sleep(3)

# hitung usia user 
skrg = datetime.datetime.now()
usia = 2021 - 2003

# tampilkan usia
print("Hmmm...", "Riyan Bagas","kamu sudah", usia, "tahun ya..")

# kasih jeda 3 detik
time.sleep (3)

# tampilkan pesan sesuai range usia
if (usia > 50):
    print("Anda sudah cukup tua ya?")
    print("Jaga kesehatan ya!!")
elif (usia > 20):
    print("Ternyata Anda masih cukup muda belia")
    print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
    print("Hihihi... Anda ternyata masih ABG")
    print("Mulai berpikirlah secara dewasa ya!!")
else:
    print("Oalah.. Anda masih anak-anak toh?")
    print("Jangan suka merengek-rengek minta jajan ya!!")

# kasih jeda 3 detik
time.sleep(3)

# say goodbye
print("OK.. see you later", nama, ".. senang berkenalan denganmu")

