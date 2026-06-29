# 🐍 Object-Oriented Programming (OOP) in Python

## 📖 What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects**. Objects represent real-world entities and contain both data (attributes) and functions (methods).
## 📚 Topics Covered
- Classes
- Objects
- Constructor (`__init__`)
- `self` keyword
- `__str__()` method
## 📝 Example
```python
class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject
    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade}, Subject: {self.subject}"
```
## 💡 Key Learnings
- A class acts as a blueprint for creating objects.
- `__init__()` initializes object attributes.
- `self` refers to the current object.
- `__str__()` provides a readable string representation of an object.

# 🧪 Practice Examples
## Example 1: Student Class
Concepts Learned:
- Creating a class
- Constructors (`__init__`)
- Object creation
- `__str__()` method
## Example 2: Employee Class
Concepts Learned:
- Class Variables
- Instance Variables
- Methods
- Updating Object Attributes
- `__dict__`
- Difference between Class and Instance Variables
### Key Concepts
**Class Variable**
A class variable is shared among all instances of a class.
```python
raise_amount = 1.04
```
**Instance Variable**
Each object has its own copy.
```python
self.first
self.last
self.pay
```
**Method**
```python
apply_raise()
```
Updates an employee's salary using the current raise percentage.
## Progress
- ✅ Student Class
- ✅ Employee Class
## Next:
- Class Methods
- Static Methods
- Inheritance

## Example 3: Class Methods & Static Methods
### Concepts Learned
- `@classmethod`
- `@staticmethod`
- Alternative Constructors
- Using the `datetime` module
### Class Method
A class method works with the class itself instead of an individual object. It receives `cls` as its first parameter.
Example:
```python
@classmethod
def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)
```
### Static Method
A static method behaves like a normal function but is grouped inside the class because it logically belongs there.
Example:
```python
@staticmethod
def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    return True
```
### Progress
- ✅ Class Methods
- ✅ Static Methods
### Next Topic
- Inheritance
## 🚀 Next Topics
- Methods
- Encapsulation
- Inheritance
- Polymorphism
