from random import randint
count = 1
while True:
    bil = randint(0,25) 
    print(bil)
    if bil == 7:
        print("Jumlah perulangan : ", count)
        break
    count += 1
