class Employee:
    num_of_employes = 0
    amount = 5
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + '@gmail.com'
        self.pay = pay
        Employee.num_of_employes +=1 #use Employee here because this doesnt need to ever be changed for one instance
    #@property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    #@property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # @fullname.setter
    # def fullname(self, name):
    #     first, last = name.split(' ')
    #     self.first = first
    #     self.last = last

    def raiseamount(self):
        self.pay = int(self.pay * self.amount)
        return self.pay
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = [] 
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev1 = Developer("tai", "font", 5,'Python')
dev2 = Developer("f", "b", 10,'Java')
emp1 = Employee("bob","lee",1000)
mgr1 = Manager('Sue','smith',90000,[dev1])




