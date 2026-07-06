#Linear Search
arr=[15,8,27,42,9]
target=42
found= False
for i,v in enumerate(arr):
    if v==target: found= True
if found: print("Element found at index:",i)
else: print("Element not found")

#Largest Number
arr = [-5,-2,-9,-1]
largest = arr[0]
for i in arr:
    if i>=largest:
        largest=i

print("Largest element is", largest)

#Smallest Number
arr = [15,8,27,42,19]
smallest = arr[0]
for i in arr:
    if i<smallest:
        smallest=i

print("Smallest element is", smallest)

#Reversed Array
arr=[10,20,30,40,50]
left=0
right=len(arr)-1
while left<right:
    arr[left], arr[right] = arr[right], arr[left]
    left+=1
    right-=1
print("Reversed array:",arr)
