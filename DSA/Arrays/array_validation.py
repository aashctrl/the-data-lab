#Check if an Array is Sorted
arr = [2, 5, 8, 10, 15]
sorted_array = True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted_array = False
        break
if sorted_array:
    print("Array is sorted")
else:
    print("Array is not sorted")

#Move All Zeros to the End
arr = [0,1,0,3,12]
arr2=[]
for i in arr:
    if i!=0:
        arr2.append(i)
zeros=len(arr)-len(arr2)
for j in range(zeros):
    arr2.append(0)
print(arr2)
