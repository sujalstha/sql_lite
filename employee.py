class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        tax = self.pay/0.5
        self.pay = self.pay - tax

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def emp_real_pay(self):
        tax_cut = self.pay/.05
        self.pay = self.pay-tax_cut
        return "{} {}'s pay is {}".format(self.first, self.last, self.pay)

    def __repr__(self):
        return "Employee( '{}', '{}', '{}')".format(self.first, self.last, self.pay)