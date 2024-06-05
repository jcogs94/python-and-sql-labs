import os
import psycopg2
from Database import Database

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


db = Database(connection, cursor)
os.system('clear')
print('Welcome to the app.')
db.print_prompt()

running = True
while running:
    user_input = input('> ')
    match user_input:
        case '1':
            db.view_employees(False)
        case '2':
            db.view_companies()
        case '3':
            db.add_employee_prompt()
        case '4':
            db.add_company_prompt()
        case '5':
            db.update_company_prompt()
        case '6':
            print('6')
        case '7':
            print('7')
        case '8':
            print('8')
        case '9':
            running = False
        case _:
            print('Please enter a valid input.\n')

# # Commit for table creation
# connection.commit()

cursor.close()
connection.close()
