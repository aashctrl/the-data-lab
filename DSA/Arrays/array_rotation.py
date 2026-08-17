#left rotation
arr = [1, 2, 3, 4, 5]
arr1=arr[0]
arr2=[]
for i in range(1,len(arr)):
    arr2.append(arr[i])
arr2.append(arr1)
print(arr2)

#right rotation
arr = [1, 2, 3, 4, 5]
arr1=arr[4]
arr2=[]
arr2.append(arr1)
for i in range(0,len(arr-1)):
    arr2.append(arr[i])
print(arr2)
