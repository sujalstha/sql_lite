import sqlite3
from employee import Employee

con = sqlite3.connect('employee.db')
c = con.cursor()
'''c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay int,
    )""")'''

emp1 = Employee('Sujal', 'Shrestha', '50000')
emp2 = Employee('Rajen', 'Bajgain', '60000')

c.execute("INSERT INTO employees VALUES ('Sujal', 'Shrestha', 50000)")

con.commit()

c.execute()

con.commit()

c.execute("SELECT * FORM employees WHERE last='Shrestha' ")

print(c.fetchall())

con.commit()

con.close()