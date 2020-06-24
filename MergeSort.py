arrA=[43,6,3,23,878,1]
length= len(arrA)
halfLen=int(length/2)
arrB=arrA[0 : halfLen]
arrC=arrA[halfLen : ]

'''now i should sort arrB and sort arrC'''
i=0
while (i+1<=(halfLen-1)):
    if arrB[i]>arrB[i+1]:
        swap(arrB[i],arrB[i+1])
        i+=1    
        
print(arrB)