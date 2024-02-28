class Employee:
    def __init__(self, first, last, pay) -> None:
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Omkar', 'More', 2000000)
emp_2 = Employee('Test', 'User', 10000)

print(emp_1.fullname())
print(emp_2.fullname())
