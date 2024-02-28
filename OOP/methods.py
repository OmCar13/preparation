class Employee: 
    
    num_of_emps = 0 
    raise_amount = 1.04  
     
    def __init__(self, first, last, pay) -> None:
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com' 

        Employee.num_of_emps += 1 
  
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 
    
    def apply_raise(self):
        return (self.pay * self.raise_amount) 
    
    @classmethod
    def set_raise_amount(cls, amount): 
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 

   
emp_1 = Employee('Omkar', 'More', 2000000)
emp_2 = Employee('Test', 'User', 10000)

emp_1_str = 'John-Doe-70000'
emp_2_str = 'Steve-Smith-30000'
emp_3_str = 'Jane-Doe-40000'

new_emp_1 = Employee.from_string(emp_1_str)

import datetime
my_date = datetime.date(2024, 2, 24)

print(Employee.is_workday(my_date))

print(emp_1.raise_amount)
print(emp_1.apply_raise())
print(Employee.num_of_emps)
print(new_emp_1.email, new_emp_1.pay)    

