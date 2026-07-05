# Iterating using a for loop
nums = [1, 2, 3]
for num in nums:
    print(num)  
print(dir(nums))
print(iter(nums))

# Creating an iterator
nums = [1, 2, 3]
i_nums = iter(nums)
print(i_nums)
print(dir(i_nums))
print(iter(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))

# Handling StopIteration
nums = [1, 2, 3]
i_nums = iter(nums)
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

# Custom Iterator
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
