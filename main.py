import sqlite3
from employee import Employee
from helper import *

conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Creating Table
cur.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
            )""")


# adding data to table
cur.execute("INSERT INTO employees VALUES ('Saadman','Sakib',3000)")
cur.execute("INSERT INTO employees VALUES ('Rahmat','Sakib',4000)")
cur.execute("INSERT INTO employees VALUES ('Karim','Ullah',6000)")

# adding data to table with ORM
emp1 = Employee('Ikmam','Abir',2000)
emp2 = Employee('Jahangir','Abir',8000)
emp3 = Employee('Jahangir','Masud',500)

# !!!! VERY DANGEROUS WAY !!!!
cur.execute(f"INSERT INTO employees VALUES ('{emp1.first}','{emp1.last}',{emp1.pay})")

# Safer Way:
cur.execute(f"INSERT INTO employees VALUES (?, ?, ?)",(emp2.first, emp2.last, emp2.pay))

# Another Safer Way:
cur.execute(f"INSERT INTO employees VALUES (:first, :last, :pay)", {
        'first': emp3.first, 'last': emp3.last, 'pay': emp3.pay
    })

# querying data from table
# cur.execute("SELECT * FROM employees WHERE last=?",('Abir',))
# cur.execute("SELECT * FROM employees WHERE last=:last",('Abir',))
cur.execute("SELECT * FROM employees WHERE True")





# cur.fetchone()
# cur.fetchmany(2)
from pprint import pprint
pprint(cur.fetchall())

conn.commit()
conn.close()