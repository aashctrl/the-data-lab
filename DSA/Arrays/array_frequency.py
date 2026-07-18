#find the frequency of an element
arr = [1, 2, 3, 2, 4, 2]
x = 2
count=0
for i in arr:
    if i==x:
        count+=1
print(count)

#remove duplicates from the sorted array
arr1=[1,1,2,2,3,4,4]
result=[]
for i in arr1:
    if i not in result:
        result.append(i)
print(result)
