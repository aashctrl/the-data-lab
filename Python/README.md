# Iterators & Iterables & Generators

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

# Python Generators
## Overview
Generators allow values to be produced one at a time instead of storing all values in memory at once. They are memory efficient and are commonly used when working with large datasets or streams of data.

## Topics Covered
- Generator Functions
- yield keyword
- next() function
- Generator Objects
- Generator Expressions
- List Comprehensions vs Generator Expressions

## Generator Function
A generator function uses the `yield` keyword to return values one at a time.
Example:
```python
def sqno(num):
    for i in num:
        yield i * i
```

## next()
The `next()` function retrieves the next value produced by a generator.

## Generator Expression
Example:
```python
(x*x for x in [1,2,3,4,5])
```
Generator expressions work similarly to list comprehensions but generate values lazily.

## Advantages
- Memory efficient
- Faster for large datasets
- Generates values only when needed

## Key Difference
List Comprehension:
```python
[x*x for x in nums]
```
Generator Expression:
```python
(x*x for x in nums)
```

## Time Complexity
Traversing all generated values: **O(n)**

## Learning Outcome
Learned how generators produce values lazily, how `yield` differs from `return`, and how generator expressions improve memory efficiency.
