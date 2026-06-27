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

## 🚀 Next Topics
- Methods
- Encapsulation
- Inheritance
- Polymorphism
