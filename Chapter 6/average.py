def function(*myData):
    # init values
    sum = 0
    i = 0

    # menjumlahkan semua data dalam myData
    for data in myData:
        sum += data
        i += 1
    print (sum)

    # hitung rata-rata
    rata2 = sum/i
    print('Rata-ratanya: ',rata2)

function(3, 5, 6, 7)
