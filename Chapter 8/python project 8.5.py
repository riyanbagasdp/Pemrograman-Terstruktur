def kuadrat(*myData):
    lenData=len(myData)
    for i in range (lenData):
        temp=myData[i]*myData[i]
        print('myData(',myData[i],')','pangkat myData(',myData[i],')=',temp)

kuadrat(2,4,5,6)