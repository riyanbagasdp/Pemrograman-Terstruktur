print("-"*30)
print("PROGRAM HITUNG RATA-RATA")
print("-"*30)
bilangan = int
i = 0
j = 0
while bilangan == int:
    try:
        bil = int(input('Masukkan bilangan bulat: '))
        lanjut = input('Apakah ingin memasukkan bilangan lagi?(y/n) ')
        i+=bil
        j+=1
        if lanjut == 'y':
            continue
        elif lanjut == 'n':
            print('Nilai rata rata dari data diatas adalah : ', i/j)
            break
        else:
            print('Input Salah !!!')
            lanjut = input('Apakah ingin memasukkan bilangan lagi?(y/n) ')
            if lanjut == 'y':
                continue
            elif lanjut == 'n':
                print('Nilai rata rata dari data diatas adalah : ', i/j)
                break
    except ValueError:
        print('Input harus berupa bilangan')
        continue
