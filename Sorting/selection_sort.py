num=int(input("how many elements"))
arr=[]
for i in range(num):
    element=int(input("enter the number"))
    arr.append(element)
print(arr)

for j in range(num-1):
    min_element=j
    for k in range(j+1,num):
        if(arr[k]<arr[min_element]):
            min_element=k
    temp=arr[j]
    arr[j]=arr[min_element]
    arr[min_element]=temp
print("sorted array: ",arr)