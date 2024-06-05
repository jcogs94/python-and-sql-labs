import os
from prettytable import PrettyTable

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

    def view_employees (self):
        os.system('clear')
        print('==============')
        print('View Employees')
        print('==============\n')

        self.cursor.execute('SELECT * FROM employees')
        data = self.cursor.fetchall()

        output_table = PrettyTable(['First', 'Last', 'Age', 'Email'])
        for entry in data:
            output_table.add_row([entry[1], entry[2], entry[3], entry[4]])
        
        print(output_table, '\n')
        input('[Enter] to go back to menu. ')

        os.system('clear')
        self.print_prompt()
    
    def view_companies (self):
        os.system('clear')
        print('==============')
        print('View Companies')
        print('==============\n')

        self.cursor.execute('SELECT * FROM companies')
        data = self.cursor.fetchall()

        output_table = PrettyTable(['Name', 'State'])
        for entry in data:
            output_table.add_row([entry[1], entry[2]])
        
        print(output_table, '\n')
        input('[Enter] to go back to menu. ')

        os.system('clear')
        self.print_prompt()
    
    def add_employee (self, first, last, age, email):
        self.cursor.execute('''INSERT INTO employees 
                ( first_name, last_name, age, email )
            VALUES
                (%s, %s, %s, %s)
            ''', [first, last, age, email])
        self.connection.commit()
        
        os.system('clear')
        print('New employee added...')
        self.print_prompt()
    
    def add_employee_prompt (self):
        os.system('clear')
        print('================')
        print('Add New Employee')
        print('================\n')
        
        valid_first, valid_last, valid_age, valid_email = [False, False, False, False]

        while valid_first == False:
            first_name = input('First name: ')
            if len(first_name) <= 20:
                valid_first = True
            else:
                print('Invalid input. Try again.\n')
        
        while valid_last == False:
            last_name = input('Last name: ')
            if len(last_name) <= 20:
                valid_last = True
            else:
                print('Invalid input. Try again.\n')
        
        while valid_age == False:
            age = input('Age: ')
            try:
                age = int(age)
                valid_age = True
            except ValueError:
                print('Invalid input. Try again.\n')

        while valid_email == False:
            email = input('Email: ')
            if len(email) <= 32:
                valid_email = True
            else:
                print('Invalid input. Try again.\n')
        
        self.add_employee(first_name, last_name, age, email)
    
    def add_company (self, name, state):
        self.cursor.execute('''INSERT INTO companies 
                ( name, state )
            VALUES
                (%s, %s)
            ''', [name, state])
        self.connection.commit()
        
        os.system('clear')
        print('New company added...')
        self.print_prompt()
    
    def add_company_prompt (self):
        os.system('clear')
        print('===============')
        print('Add New Company')
        print('===============\n')
        
        valid_name, valid_state = [False, False]

        while valid_name == False:
            name = input('Company name: ')
            if len(name) <= 20:
                valid_name = True
            else:
                print('Invalid input. Try again.\n')
        
        while valid_state == False:
            state = input("Company state (2 character abbreviation, ex. 'NY'): ")
            if len(state) == 2:
                valid_state = True
            else:
                print('Invalid input. Try again.\n')
        
        self.add_company(name, state)
    
    def __init__ (self, connection, cursor):
        self.connection = connection
        self.cursor = cursor


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
