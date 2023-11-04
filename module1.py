# def sum_num(n1,n2):
#     sum = n1 + n2 + 10
#     return sum
#
# def greetings(name):
#     return 'Hi my name is {}'.format(name)
#
#
# welcome = 'Hi welcome to th epython module'
#
#
# sum_num(4,5)
# greetings('devc')



class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return 'full name is {} {}'. format(self.first, self.last)

    def salary(self):
        self.pay = int(self.pay)

