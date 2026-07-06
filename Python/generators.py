def sq_no(nums):
    result=[]
    for i in nums:
        result.append(i*i)
    return result
mynums=sq_no([1,2,3,4,5])
print (mynums)

def sqno(num):
    for i in num:
        yield (i*i)
mynum=sqno([1,2,3,4,5])
print (mynum)  
print(next(mynum))
print(next(mynum))
print(next(mynum))

mynums=[x*x for x in [1,2,3,4,5]]
print(mynums)
for num in mynums:
    print(num)

mynums=(x*x for x in [1,2,3,4,5])
print(mynums)
for num in mynums:
    print(num)
