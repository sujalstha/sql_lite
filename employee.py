class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        tax = pay / 0.5  # Oklahoma Tax Cut
        self.pay = pay - tax

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def emp_real_pay(self):
        return "{} {}'s pay is {}".format(self.first, self.last, self.pay)

    def __repr__(self):
        return "Employee( '{}', '{}', '{}')".format(self.first, self.last, self.pay)
