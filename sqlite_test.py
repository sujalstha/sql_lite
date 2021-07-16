import sqlite3

con = sqlite3.connect('employee.db')
c = con.cursor()
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay int,
    )""")

con.commit()
con.close()