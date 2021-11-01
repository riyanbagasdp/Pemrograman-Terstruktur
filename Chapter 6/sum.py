def function(*myData):
    # init values
    sum = 0
    i = 0

    # menjumlahkan semua data dalam myData
    for data in myData:
        sum += data
        i += 1
    print (sum)

function(3,5,6,7)
function(1,0,0,2,4)
