array=[6,2,9,1,5]
def bubble_sort(array):
    for k in range(0,len(array)):
        for i in range(0,len(array)-k-1):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
    return array
print(bubble_sort(array))


