# Iterators & Iterables

## Overview
Iteration is the process of accessing elements of a collection one at a time. Python uses the iterator protocol to make objects iterable.

## Iterable
An iterable is any object capable of returning an iterator using the `iter()` function.
Examples:
- List
- Tuple
- String
- Dictionary
- Set
Example:
```python
nums = [1, 2, 3]
for num in nums:
    print(num)
```

## Iterator
An iterator is an object that keeps track of its current position and returns one element at a time using `next()`.
Example:
```python
nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
```
Output:
```
1
2
3
```
Calling `next()` after all elements are consumed raises a `StopIteration` exception.

## StopIteration
When an iterator has no more elements, Python raises a `StopIteration` exception.
Example:
```python
try:
    print(next(it))
except StopIteration:
    print("Iteration Complete")
```
## Custom Iterator
A custom iterator is created by implementing two special methods:
- `__iter__()`
- `__next__()`
Example:
```python
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
```

## Concepts Covered
- Iterable
- Iterator
- iter()
- next()
- StopIteration
- while loop iteration
- Custom Iterators
- __iter__()
- __next__()

## Files
- `iterators_iterables.py`
