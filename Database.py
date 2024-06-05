import os
import psycopg2

connection = psycopg2.connect(
    database = 'python_sql_lab'
)

cursor = connection.cursor()

# # CREATE TABLES FOR APP
# # Create employees table
# cursor.execute('''CREATE TABLE employees (
#     id SERIAL, first_name VARCHAR(20),
#     last_name VARCHAR(20), age INT, email VARCHAR(32)
# )''')

# # Create companies table
# cursor.execute('''CREATE TABLE companies (
#     id SERIAL, name VARCHAR(20),
#     state VARCHAR(2)
# )''')

# # Create roles table
# cursor.execute('''CREATE TABLE roles (
#     employee_id INT, company_id INT
# )''')

class Database:
    def print_prompt (self):
        print('''
Please select what you would like to do:
    1. View all employees
    2. View all companies
    3. Add new employee
    4. Add new company
    5. Update employee
    6. Update company
    7. Delete employee
    8. Delete company
    9. Quit
''')

    def add_employee (self):
        os.system('clear')
        print('New employee added...')
        self.print_prompt()
    
    def add_employee_prompt (self):
        os.system('clear')
        print('================')
        print('Add New Employee')
        print('================')
        
        valid_first, valid_last, valid_age, valid_email = [False, False, False, False]

        while valid_first == False:
            first_name = input('\nFirst name: ')
            if len(first_name) <= 20:
                valid_first = True
            else:
                print('Invalid input. Try again.')
        
        while valid_last == False:
            last_name = input('\nLast name: ')
            if len(last_name) <= 20:
                valid_last = True
            else:
                print('Invalid input. Try again.')
        
        while valid_age == False:
            age = input('\nAge: ')
            try:
                age = int(age)
                valid_age = True
            except ValueError:
                print('Invalid input. Try again.')

        while valid_email == False:
            email = input('\nEmail: ')
            if len(email) <= 32:
                valid_email = True
            else:
                print('Invalid input. Try again.')
        
        self.add_employee()
    
    def __init__ (self):
        print('created...')


# # SHOW ALL ENTRIES FOR TESTING
# # Show all employee entries
# cursor.execute('SELECT * FROM employees')
# print(cursor.fetchall())

# # Show all company entries
# cursor.execute('SELECT * FROM companies')
# print(cursor.fetchall())

# # Show all role entries
# cursor.execute('SELECT * FROM roles')
# print(cursor.fetchall())

cursor.close()
connection.close()
