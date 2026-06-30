class Employee:
  raise_amount = 1.04
  def __init__(self, first, last, pay): 
    self.first = first self.last = last self.pay = pay 
  def apply_raise(self): 
    self.pay = self.pay * self.raise_amount
  def fullname(self): 
    return '{} {}'.format(self.first,self.last)
    
class Developer(Employee): 
  raise_amount=1.10 
  def __init__(self, first,last,pay,prog): 
    super().__init__(first,last,pay) 
    self.prog=prog 
    
class Manager(Employee):
  def __init__(self, first,last,pay,employees=None): 
    super().__init__(first,last,pay) 
    if employees is None: 
      self.employees=[]
    else: 
      self.employees=employees 
  def add_emp(self,emp):
    if emp not in self.employees: 
      self.employees.append(emp) 
  def remove_emp(self,emp): 
    if emp in self.employees: 
      self.employees.remove(emp)
  def print_emp(self): 
    for emp in self.employees: 
      print(emp.fullname()) 
      
dev1 = Developer('Coher', 'Schafer', 50000,'Python') 
dev11 = Employee('Coher', 'Schafer', 50000) 
dev2 = Developer('Richie', 'Garfield', 60000,'Java') 
mgr1=Manager('Sue','Smith',90000,[dev1])

print(dev1.prog) 
print(dev11.raise_amount) 
print(dev1.raise_amount)  

print(mgr1.pay) 
mgr1.print_emp() 
mgr1.add_emp(dev2) 
mgr1.print_emp() 
mgr1.remove_emp(dev1) 
mgr1.print_emp() 

print(isinstance(mgr1,Manager)) 
print(isinstance(mgr1,Developer)) 
print(issubclass(Manager,Employee)) 
print(issubclass(Manager,Developer))
