class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def __repr__(self):
        return "Employee('{}','{}')".format(self.first,self.last)
    def __str__(self):
        return '{}'.format(self.fullname())
    def __add__(self,other):
        return self.pay+other.pay
    def __len__(self):
        return len(self.fullname())
        
emp1 = Employee('Coher', 'Schafer', 50000)
emp2 = Employee('Richie', 'Garfield', 60000)

print(repr(emp1))
print(str(emp1))
print(emp1+emp2)
print(len(emp1))
print(len(emp2))
