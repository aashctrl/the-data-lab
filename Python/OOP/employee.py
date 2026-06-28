class Employee:
    no_of_emp = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.no_of_emp += 1
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

print(Employee.no_of_emp)
emp1 = Employee('Coher', 'Schafer', 50000)
emp2 = Employee('Richie', 'Garfield', 60000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
emp1.raise_amount = 1.05
print(emp1.pay)
print(Employee.no_of_emp)
print(emp1.__dict__)
print(Employee.raise_amount)
