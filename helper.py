def inser_emp(cursor, emp):
    # Another Safer Way:
    cursor.execute("""INSERT INTO employees VALUES (:first, :last, :pay)""",{
            'first': emp.first, 'last': emp.last, 'pay': emp.pay
        })

def get_emps_by_name(cursor, lastname):
    cursor.execute("""SELECT * FROM employees WHERE last=:last""",{
            'last': lastname
        })
    return cursor.fetchall()

def update_pay(cursor, emp, pay):
    cursor.execute("""UPDATE employees SET pay = :pay WHERE last = :last AND first = :first""",{
            'last': emp.last, 'first': emp.first, 'pay': pay
        })
    
def remove_emp(cursor, emp):
    cursor.execute("""DELETE FROM employees WHERE last = :last AND first = :first""",{
            'last': emp.last, 'first': emp.first
        })