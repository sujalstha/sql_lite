class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def emp_pay(self):
        tax_cut = self.pay/.05
        self.pay = self.pay-tax_cut
        return '{} {} pay is {}'.format(self.first, self.last, self.pay)
