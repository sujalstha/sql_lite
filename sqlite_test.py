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
con.close()