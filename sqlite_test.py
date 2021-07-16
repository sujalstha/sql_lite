import sqlite3

con = sqlite3.connect('employee.db')
c = con.cursor()
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay int,
    )""")

c.execute("INSERT INTO employees VALUES ('Sujal', 'Shrestha', 50000)")

con.commit()

c.execute("SELECT * FORM employees WHERE last='Shrestha' ")

print(c.fetchall())

con.commit()

con.close()