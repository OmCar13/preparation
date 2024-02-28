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
   
emp_1 = Employee('Omkar', 'More', 2000000)
emp_2 = Employee('Test', 'User', 10000)

print(emp_1.raise_amount)
print(emp_1.apply_raise())
print(Employee.num_of_emps)

