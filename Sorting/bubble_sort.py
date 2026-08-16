num=int(input("how many elements"))
array=[]
for i in range(num):
    element=int(input("enter the number"))
    array.append(element)
print(array)
for j in range(0,num-1):
    for k in range(0,num-1-j):
        if(array[k]>array[k+1]):
            array[k],array[k+1]=array[k+1],array[k]
print("sorted array:",array)