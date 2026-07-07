#count even and odd elements
arr = [10, 15, 8, 21, 30, 7]
even = 0
odd = 0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even:", even)
print("Odd:", odd)

#find second largest element
arr = [10, 25, 8, 40, 15]
largest=arr[0]
second_largest=arr[0]
for i in arr:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i<largest:
        second_largest=i
print("Largest:",largest)
print("Second Largest:",second_largest)

#find second smallest element
arr = [-10, -2, -30, -5]
smallest=arr[0]
second_smallest=arr[0]
for i in arr:
    if i<smallest:
        second_smallest=smallest
        smallest=i
    elif i<second_smallest and i>smallest:
        second_smallest=i
print("Smallest:",smallest)
print("Second Smallest:",second_smallest)
