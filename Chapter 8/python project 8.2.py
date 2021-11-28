def dataStat(*myData):
    x = len(myData)
    y = sum(myData)
    a = y/x
    b = max(myData)
    c = min(myData)
    list = [a,b,c]
    print(list)

dataStat(1,2,3,3,1)