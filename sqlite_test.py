import sqlite3

from employee import Employee

con = sqlite3.connect('employee.db')
c = con.cursor()

'''c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay int,
    )""")'''


def insert_emp(emp):
    with con:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first,
                                                                         'last': emp.last,
                                                                         'pay': emp.pay})


def get_emp_by_name(last):
    c.execute("SELECT * FROM employees WHERE last =:last", {
        'last': last
    })
    return c.fetchall()


def update_pay(emp, pay):
    with con:
        c.execute("""Update employees SET pay = :pay"
                   WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def remove_emp(emp):
    with con:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp1 = Employee('Sujal', 'Shrestha', '50000')
emp2 = Employee('Rajen', 'Bajgain', '60000')

c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp1.first, emp1.last, emp1.pay))

con.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#          {'first': emp2.first, 'last': emp2.last, 'pay': emp2.pay})

con.commit()

c.execute("SELECT * FROM employees WHERE last='?' ", {'last': emp2.last})

print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last='Smith'")

print(c.fetchall())

con.close()
