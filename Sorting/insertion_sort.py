num = int(input("how many elements: "))
array = []

for i in range(num):
    element = int(input("enter the number: "))
    array.append(element)

for i in range(1, num):
    key = array[i]
    j = i - 1

    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1

    array[j + 1] = key

print("sorted array:", array)