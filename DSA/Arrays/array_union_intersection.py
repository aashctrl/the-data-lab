# Union of 2 Arrays
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
result = []
# traverse arr1
for i in arr1:
    result.append(i)
# traverse arr2
for j in arr2:
    if j not in result:
        result.append(j)
print(result)

# Intersection of 2 Arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
result = []
# traverse an array
for i in arr1:
# check whether element exists in the other array
    if i in arr2:
        # add unique matching elements
        result.append(i)
print(result)
