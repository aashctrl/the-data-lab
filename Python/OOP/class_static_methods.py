class Employee:  
    def __init__(self,first,last,pay):  
        self.firts,self.last,self.pay=first,last,pay
    @classmethod 
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_str1='John-Doe-70000'
emp_str2='Jane-Doe-90000'
new_emp1=Employee.from_string(emp_str1)
new_emp2=Employee.from_string(emp_str2)
print(new_emp1.last)
print(new_emp1.pay)

import datetime
my_date1=datetime.date(2026,7,10)
my_date2=datetime.date(2016,7,10)
print(Employee.is_workday(my_date1))
print(Employee.is_workday(my_date2))
