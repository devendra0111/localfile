class Employee:
    apply_raise = 2
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def salary(self):
        self.pay = int(self.pay*self.apply_raise)

    @classmethod
    def new_salary(cls, amount):
        cls.apply_raise=amount


e1 = Employee('dev', 'Pathak', 80000)
e2 = Employee('sulekha', 'kumari', 900000)
print(e1.pay)
e1.salary()
print(e1.pay,'is the salary after the increment')

e1.salary()
Employee.new_salary(4)
print(e1.pay)