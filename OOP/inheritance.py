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
        self.pay = int(self.pay * self.raise_amount)
    
class Developer(Employee):
    
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang  = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('Current employee under supervision -->', emp.fullname())


dev_1 = Developer('Omkar', 'More', 2000000, 'Python')
dev_2 = Developer('Test', 'User', 10000, 'GO')

mgr_1 = Manager('John', 'Wick', 90000, [dev_1])

print(mgr_1.email)
mgr_1.print_emps()

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()


print(isinstance(mgr_1, Employee)) # true
print(issubclass(Employee, Developer)) # false 
print(issubclass(Developer, Employee)) # true 

"""
1. What is inheritence?
It is a method that allows us to create a new class that shares the same attributes and method with the original function, and add some extra functionality to the new class. It also does not disturb the original class.


2. How to make a class inherit from another class?
class Developer(Employee):


3. Structure of classes and subclasses.
When we input a function to a subclass, python follows the 'method resolution order', which is the chain of classes that it goes through to find what the method is. All classes have the built-in group of methods and attributes as their primary order.


4. How to initiate the subclass so that it can handle more information than its original class can?
There are 2 ways.
first, using the super method as follows and pass in the arguments in interest.
super.__init__()


Second, call the parent's init method explicitly and pass in the arguments in interest.
Employee.init(self, first, last, )


5. Useful tools when exploring the inheritance system.
.isinstance(instance, class)
This method returns the boolean value of whether an instance belongs to a calss
.issubclass(subclass, class)
This method returns the boolean value of whether a class has inherited from the second class.


6. Example of class inheritance
Whisky library 
"""


