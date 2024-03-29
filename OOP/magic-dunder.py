class Employee: 

    def __init__(self, first, last, pay) -> None:
            self.first = first 
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@company.com' 

            
    def fullname(self):
            return '{} {}'.format(self.first, self.last) 
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
          return "Employee('{}, {}, {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
          return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
          return self.pay + other.pay


emp_1 = Employee('Omkar', 'More', 2000000)
emp_2 = Employee('Test', 'User', 10000)

print(emp_1 + emp_2)


print(emp_1.__repr__())
print(emp_1.__str__())